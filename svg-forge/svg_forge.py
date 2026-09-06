from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass, replace
from datetime import datetime, timezone
from io import BytesIO
from pathlib import Path
from typing import Any


SUPPORTED_RASTER_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp"}
SUPPORTED_SVG_EXTENSIONS = {".svg", ".svgz"}
MAX_EXPORT_SIZE = 16384
VTRACER_PARAMETER_ORDER = (
    "colormode",
    "hierarchical",
    "mode",
    "filter_speckle",
    "color_precision",
    "layer_difference",
    "corner_threshold",
    "length_threshold",
    "max_iterations",
    "splice_threshold",
    "path_precision",
)


@dataclass(frozen=True)
class Preset:
    description: str
    settings: dict[str, Any]
    force_bw: bool = False
    threshold: int = 128
    supersample: int = 1


PRESETS: dict[str, Preset] = {
    "icon-clean": Preset(
        description="Balanced cleanup for small colour icons.",
        settings={
            "colormode": "color",
            "hierarchical": "stacked",
            "mode": "spline",
            "filter_speckle": 8,
            "color_precision": 6,
            "layer_difference": 18,
            "corner_threshold": 60,
            "length_threshold": 4.2,
            "max_iterations": 10,
            "splice_threshold": 45,
            "path_precision": 3,
        },
    ),
    "logo-clean": Preset(
        description="Clean logo marks and brand shapes.",
        settings={
            "colormode": "color",
            "hierarchical": "cutout",
            "mode": "spline",
            "filter_speckle": 12,
            "color_precision": 6,
            "layer_difference": 24,
            "corner_threshold": 70,
            "length_threshold": 4.8,
            "max_iterations": 12,
            "splice_threshold": 50,
            "path_precision": 3,
        },
    ),
    "logo-mono-hq": Preset(
        description="High-quality single-colour logos with smoother sub-pixel contours.",
        settings={
            "colormode": "binary",
            "hierarchical": "cutout",
            "mode": "spline",
            "filter_speckle": 10,
            "corner_threshold": 65,
            "length_threshold": 8.0,
            "max_iterations": 10,
            "splice_threshold": 45,
            "path_precision": 3,
        },
        force_bw=True,
        threshold=128,
        supersample=4,
    ),
    "glyph-bw": Preset(
        description="Black/white glyphs, masks, and simple symbols.",
        settings={
            "colormode": "binary",
            "hierarchical": "cutout",
            "mode": "spline",
            "filter_speckle": 10,
            "corner_threshold": 65,
            "length_threshold": 4.0,
            "max_iterations": 10,
            "splice_threshold": 45,
            "path_precision": 3,
        },
        force_bw=True,
    ),
    "flat-colour": Preset(
        description="Reduced-palette flat colour icons.",
        settings={
            "colormode": "color",
            "hierarchical": "stacked",
            "mode": "spline",
            "filter_speckle": 14,
            "color_precision": 4,
            "layer_difference": 36,
            "corner_threshold": 60,
            "length_threshold": 5.0,
            "max_iterations": 8,
            "splice_threshold": 45,
            "path_precision": 3,
        },
    ),
    "detailed-colour": Preset(
        description="More detailed colour tracing for richer images.",
        settings={
            "colormode": "color",
            "hierarchical": "stacked",
            "mode": "spline",
            "filter_speckle": 2,
            "color_precision": 8,
            "layer_difference": 8,
            "corner_threshold": 55,
            "length_threshold": 3.5,
            "max_iterations": 16,
            "splice_threshold": 40,
            "path_precision": 4,
        },
    ),
}


@dataclass(frozen=True)
class SourceItem:
    source: Path
    destination: Path
    size: int | None = None


@dataclass(frozen=True)
class PreparedImage:
    path: Path
    source_size: tuple[int, int] | None = None
    trace_size: tuple[int, int] | None = None


@dataclass
class Result:
    status: str
    source: Path
    destination: Path
    message: str = ""


def script_dir() -> Path:
    return Path(__file__).resolve().parent


def load_config(path: Path) -> dict[str, Any]:
    defaults: dict[str, Any] = {
        "default_preset": "icon-clean",
        "default_output": "output",
        "skip_existing": False,
        "recursive": False,
    }

    if not path.exists():
        return defaults

    try:
        with path.open("r", encoding="utf-8") as file:
            loaded = json.load(file)
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Config file is invalid JSON: {path} ({exc})") from exc

    if not isinstance(loaded, dict):
        raise SystemExit(f"Config file must contain a JSON object: {path}")

    merged = defaults.copy()
    merged.update(loaded)
    return merged


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="svg_forge",
        description="Batch trace raster images to SVG or render SVG files to PNG/JPG.",
    )
    input_options = parser.add_argument_group("Input Options")
    input_options.add_argument(
        "--input",
        metavar="PATH",
        nargs="+",
        help="Input file(s) or folder(s). File support depends on --to.",
    )

    output_options = parser.add_argument_group("Output Options")
    output_options.add_argument(
        "--output",
        metavar="PATH",
        help="Output folder. Defaults to the config default_output value.",
    )
    output_options.add_argument(
        "--log",
        metavar="PATH",
        help="Conversion log path. Defaults to <output>\\svg-forge.log.",
    )
    output_options.add_argument(
        "--to",
        metavar="FORMAT",
        nargs="+",
        choices=("svg", "png", "jpg", "jpeg"),
        default=["svg"],
        help="Output format(s): svg (default), or png and/or jpg for SVG inputs.",
    )

    export_options = parser.add_argument_group("SVG Export Options")
    export_options.add_argument(
        "--size",
        metavar="PIXELS",
        nargs="+",
        type=int,
        help=(
            "One or more longest-edge pixel sizes. Aspect ratio is preserved. "
            "Without this flag, the SVG's natural dimensions are used."
        ),
    )
    export_options.add_argument(
        "--background",
        metavar="COLOUR",
        help=(
            "Raster background colour, such as white or '#F5F5F5'. "
            "PNG defaults to transparent; JPG defaults to white."
        ),
    )
    export_options.add_argument(
        "--jpg-quality",
        metavar="1-100",
        type=int,
        help="JPEG quality (default: 95). Uses full-colour 4:4:4 subsampling for logos.",
    )

    trace_options = parser.add_argument_group("Trace Options")
    trace_options.add_argument(
        "--preset",
        metavar="NAME",
        choices=sorted(PRESETS),
        help="Tracing preset to use. Defaults to the config default_preset value.",
    )
    trace_options.add_argument(
        "--threshold",
        metavar="0-255",
        type=int,
        help="Override the black/white cutoff for monochrome presets (default: preset value).",
    )
    trace_options.add_argument(
        "--supersample",
        metavar="FACTOR",
        type=int,
        choices=(1, 2, 3, 4, 8),
        help="Override monochrome contour supersampling: 1, 2, 3, 4, or 8.",
    )

    config_options = parser.add_argument_group("Config Options")
    config_options.add_argument(
        "--config",
        metavar="PATH",
        default=str(script_dir() / "svg_forge.config.json"),
        help="Path to the JSON config file.",
    )

    behavior_options = parser.add_argument_group("Behavior Options")
    behavior_options.add_argument(
        "--dry-run",
        action="store_true",
        help="Show planned conversions without writing SVGs, folders, or logs.",
    )
    behavior_options.add_argument(
        "--skip-existing",
        action="store_true",
        default=None,
        help="Skip output files that already exist.",
    )
    behavior_options.add_argument(
        "--recursive",
        action="store_true",
        default=None,
        help="Scan input folders recursively and preserve subfolders under output.",
    )
    behavior_options.add_argument(
        "--open-inkscape",
        "--open-after-convert",
        action="store_true",
        help="Open converted SVG files in Inkscape when Inkscape is available.",
    )
    behavior_options.add_argument(
        "--list-presets",
        action="store_true",
        help="List available presets and exit.",
    )
    return parser.parse_args()


def resolve_bool(cli_value: bool | None, config: dict[str, Any], key: str) -> bool:
    if cli_value is not None:
        return bool(cli_value)
    return bool(config.get(key, False))


def is_supported(path: Path) -> bool:
    return path.is_file() and path.suffix.lower() in SUPPORTED_RASTER_EXTENSIONS


def is_supported_svg(path: Path) -> bool:
    return path.is_file() and path.suffix.lower() in SUPPORTED_SVG_EXTENSIONS


def collect_sources(inputs: list[str], output_dir: Path, recursive: bool) -> list[SourceItem]:
    collected: list[SourceItem] = []

    for raw in inputs:
        path = Path(raw).expanduser()
        if not path.exists():
            print(f"warn: input does not exist: {path}", file=sys.stderr)
            continue

        if path.is_file():
            if is_supported(path):
                collected.append(SourceItem(path.resolve(), output_dir / f"{path.stem}.svg"))
            else:
                print(f"warn: unsupported input skipped: {path}", file=sys.stderr)
            continue

        iterator = path.rglob("*") if recursive else path.iterdir()
        folder_root = path.resolve()
        for candidate in sorted(iterator):
            if not is_supported(candidate):
                continue
            relative = candidate.resolve().relative_to(folder_root)
            destination = output_dir / relative.with_suffix(".svg")
            collected.append(SourceItem(candidate.resolve(), destination))

    return collected


def export_destination(
    output_dir: Path,
    relative_source: Path,
    output_format: str,
    size: int | None,
) -> Path:
    size_suffix = f"-{size}px" if size is not None else ""
    relative_parent = relative_source.parent
    return output_dir / relative_parent / f"{relative_source.stem}{size_suffix}.{output_format}"


def collect_svg_exports(
    inputs: list[str],
    output_dir: Path,
    recursive: bool,
    output_formats: list[str],
    sizes: list[int | None],
) -> list[SourceItem]:
    collected: list[SourceItem] = []

    for raw in inputs:
        path = Path(raw).expanduser()
        if not path.exists():
            print(f"warn: input does not exist: {path}", file=sys.stderr)
            continue

        if path.is_file():
            if is_supported_svg(path):
                for size in sizes:
                    for output_format in output_formats:
                        destination = export_destination(
                            output_dir,
                            Path(path.name),
                            output_format,
                            size,
                        )
                        collected.append(SourceItem(path.resolve(), destination, size))
            else:
                print(f"warn: unsupported input skipped: {path}", file=sys.stderr)
            continue

        iterator = path.rglob("*") if recursive else path.iterdir()
        folder_root = path.resolve()
        for candidate in sorted(iterator):
            if not is_supported_svg(candidate):
                continue
            relative = candidate.resolve().relative_to(folder_root)
            for size in sizes:
                for output_format in output_formats:
                    destination = export_destination(
                        output_dir,
                        relative,
                        output_format,
                        size,
                    )
                    collected.append(SourceItem(candidate.resolve(), destination, size))

    return collected


def detect_destination_collisions(items: list[SourceItem]) -> list[Path]:
    seen: dict[Path, Path] = {}
    collisions: list[Path] = []
    for item in items:
        key = item.destination.resolve() if item.destination.exists() else item.destination.absolute()
        if key in seen and key not in collisions:
            collisions.append(key)
        seen[key] = item.source
    return collisions


def require_vtracer() -> Any:
    try:
        import vtracer
    except ImportError as exc:
        raise SystemExit(
            "Missing dependency: vtracer. Install with: python -m pip install -r requirements.txt"
        ) from exc
    return vtracer


def require_pillow() -> tuple[Any, Any]:
    try:
        from PIL import Image, ImageOps
    except ImportError as exc:
        raise SystemExit(
            "Missing dependency: Pillow. Install with: python -m pip install -r requirements.txt"
        ) from exc
    return Image, ImageOps


def require_resvg() -> Any:
    try:
        import resvg_py
    except ImportError as exc:
        raise SystemExit(
            "Missing dependency: resvg_py. Install with: python -m pip install -r requirements.txt"
        ) from exc
    return resvg_py


def parse_background(colour: str | None) -> tuple[int, int, int, int] | None:
    if colour is None:
        return None

    try:
        from PIL import ImageColor

        return ImageColor.getcolor(colour, "RGBA")
    except (ImportError, ValueError) as exc:
        raise ValueError(f"invalid background colour: {colour}") from exc


def prepare_input(source: Path, preset: Preset, temp_dir: Path) -> PreparedImage:
    needs_png_copy = source.suffix.lower() == ".webp" or preset.force_bw
    if not needs_png_copy:
        return PreparedImage(source)

    Image, ImageOps = require_pillow()
    prepared = temp_dir / f"{source.stem}.prepared.png"

    with Image.open(source) as image:
        source_size = image.size
        if preset.force_bw:
            rgba = image.convert("RGBA")
            background = Image.new("RGBA", rgba.size, "WHITE")
            flattened = Image.alpha_composite(background, rgba)
            grayscale = ImageOps.grayscale(flattened)
            if preset.supersample > 1:
                grayscale = grayscale.resize(
                    (
                        grayscale.width * preset.supersample,
                        grayscale.height * preset.supersample,
                    ),
                    Image.Resampling.LANCZOS,
                )
            bw = grayscale.point(
                lambda value: 0 if value < preset.threshold else 255,
                mode="1",
            )
            bw.save(prepared)
            trace_size = bw.size
        else:
            image.convert("RGBA").save(prepared)
            trace_size = image.size

    return PreparedImage(prepared, source_size, trace_size)


def normalize_supersampled_svg(
    svg_path: Path,
    source_size: tuple[int, int],
    trace_size: tuple[int, int],
) -> None:
    if source_size == trace_size:
        return

    svg = svg_path.read_text(encoding="utf-8")
    root_match = re.search(r"<svg\b[^>]*>", svg, flags=re.IGNORECASE)
    if not root_match:
        raise RuntimeError(f"VTracer output is missing an SVG root element: {svg_path}")

    root = root_match.group(0)
    root = re.sub(
        r'\s(?:width|height|viewBox)="[^"]*"',
        "",
        root,
        flags=re.IGNORECASE,
    )
    source_width, source_height = source_size
    trace_width, trace_height = trace_size
    normalized_root = (
        root[:-1]
        + f' width="{source_width}" height="{source_height}"'
        + f' viewBox="0 0 {trace_width} {trace_height}">'
    )
    svg_path.write_text(
        svg[: root_match.start()] + normalized_root + svg[root_match.end() :],
        encoding="utf-8",
    )


def convert_one(item: SourceItem, preset: Preset, skip_existing: bool) -> Result:
    if item.destination.exists() and skip_existing:
        return Result("skipped", item.source, item.destination, "output exists")

    vtracer = require_vtracer()
    item.destination.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory(prefix="svg-forge-") as temp:
        prepared_input = prepare_input(item.source, preset, Path(temp))
        # The Windows Python binding is stable with positional option values.
        ordered_settings = [preset.settings.get(name) for name in VTRACER_PARAMETER_ORDER]
        vtracer.convert_image_to_svg_py(
            str(prepared_input.path),
            str(item.destination),
            *ordered_settings,
        )
        if prepared_input.source_size and prepared_input.trace_size:
            normalize_supersampled_svg(
                item.destination,
                prepared_input.source_size,
                prepared_input.trace_size,
            )

    return Result("converted", item.source, item.destination)


def render_svg_png(
    source: Path,
    size: int | None,
    natural_size_cache: dict[Path, tuple[int, int]],
) -> bytes:
    resvg_py = require_resvg()
    render_options: dict[str, Any] = {
        "svg_path": str(source),
        "resources_dir": str(source.parent),
        "shape_rendering": "geometric_precision",
        "text_rendering": "geometric_precision",
        "image_rendering": "optimize_quality",
    }

    if size is None:
        return resvg_py.svg_to_bytes(**render_options)

    natural_size = natural_size_cache.get(source)
    if natural_size is None:
        natural_png = resvg_py.svg_to_bytes(**render_options)
        Image, _ = require_pillow()
        with Image.open(BytesIO(natural_png)) as image:
            natural_size = image.size
        natural_size_cache[source] = natural_size

    natural_width, natural_height = natural_size
    if natural_width >= natural_height:
        render_options["width"] = size
    else:
        render_options["height"] = size
    return resvg_py.svg_to_bytes(**render_options)


def write_raster_export(
    item: SourceItem,
    png_bytes: bytes,
    background: tuple[int, int, int, int] | None,
    jpg_quality: int,
) -> None:
    item.destination.parent.mkdir(parents=True, exist_ok=True)
    output_format = item.destination.suffix.lower()

    if output_format == ".png" and background is None:
        item.destination.write_bytes(png_bytes)
        return

    Image, _ = require_pillow()
    with Image.open(BytesIO(png_bytes)) as rendered:
        rgba = rendered.convert("RGBA")
        canvas_colour = background or (255, 255, 255, 255)
        canvas = Image.new("RGBA", rgba.size, canvas_colour)
        canvas.alpha_composite(rgba)

        if output_format == ".png":
            canvas.save(item.destination, format="PNG", optimize=True)
        else:
            canvas.convert("RGB").save(
                item.destination,
                format="JPEG",
                quality=jpg_quality,
                subsampling=0,
                optimize=True,
            )


def convert_svg_one(
    item: SourceItem,
    size: int | None,
    skip_existing: bool,
    background: tuple[int, int, int, int] | None,
    jpg_quality: int,
    render_cache: dict[tuple[Path, int | None], bytes],
    natural_size_cache: dict[Path, tuple[int, int]],
) -> Result:
    if item.destination.exists() and skip_existing:
        return Result("skipped", item.source, item.destination, "output exists")

    cache_key = (item.source, size)
    png_bytes = render_cache.get(cache_key)
    if png_bytes is None:
        png_bytes = render_svg_png(item.source, size, natural_size_cache)
        render_cache[cache_key] = png_bytes

    write_raster_export(item, png_bytes, background, jpg_quality)
    return Result("converted", item.source, item.destination)


def find_inkscape() -> str | None:
    from_path = shutil.which("inkscape")
    if from_path:
        return from_path

    candidates = [
        Path(r"C:\Program Files\Inkscape\bin\inkscape.exe"),
        Path(r"C:\Program Files\Inkscape\inkscape.exe"),
        Path(r"C:\Program Files (x86)\Inkscape\bin\inkscape.exe"),
        Path(r"C:\Program Files (x86)\Inkscape\inkscape.exe"),
    ]
    for candidate in candidates:
        if candidate.exists():
            return str(candidate)
    return None


def open_in_inkscape(results: list[Result]) -> list[str]:
    inkscape = find_inkscape()
    if not inkscape:
        return ["Inkscape was not found; converted files were not opened."]

    warnings: list[str] = []
    for result in results:
        if result.status != "converted":
            continue
        try:
            subprocess.Popen([inkscape, str(result.destination)])
        except OSError as exc:
            warnings.append(f"Could not open {result.destination} in Inkscape: {exc}")
    return warnings


def write_log(
    log_path: Path,
    args: argparse.Namespace,
    operation: str,
    settings: dict[str, Any],
    results: list[Result],
) -> None:
    log_path.parent.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(timezone.utc).isoformat(timespec="seconds")
    command = " ".join([Path(sys.executable).name, *sys.argv])

    with log_path.open("a", encoding="utf-8") as file:
        file.write(f"=== SVG-Forge run {timestamp} ===\n")
        file.write(f"command: {command}\n")
        file.write(f"operation: {operation}\n")
        for key, value in settings.items():
            file.write(f"{key}: {value}\n")
        file.write(f"dry_run: {args.dry_run}\n")
        for result in results:
            file.write(
                f"{result.status}\t{result.source}\t{result.destination}\t{result.message}\n"
            )
        file.write("\n")


def print_presets() -> None:
    print("Available presets:")
    for name in sorted(PRESETS):
        print(f"  {name}: {PRESETS[name].description}")


def print_summary(results: list[Result], dry_run: bool, log_path: Path | None) -> None:
    counts: dict[str, int] = {}
    for result in results:
        counts[result.status] = counts.get(result.status, 0) + 1

    if dry_run:
        print("Dry run complete. No folders, output files, or logs were written.")
    else:
        print("Conversion run complete.")

    for status in sorted(counts):
        print(f"  {status}: {counts[status]}")

    if log_path and not dry_run:
        print(f"  log: {log_path}")


def validate_trace_options(args: argparse.Namespace) -> str | None:
    if args.size:
        return "--size can only be used when exporting SVG to PNG/JPG"
    if args.background:
        return "--background can only be used when exporting SVG to PNG/JPG"
    if args.jpg_quality is not None:
        return "--jpg-quality can only be used when exporting SVG to JPG"
    return None


def run_trace(
    args: argparse.Namespace,
    config: dict[str, Any],
    output_dir: Path,
    skip_existing: bool,
    recursive: bool,
    log_path: Path,
) -> int:
    option_error = validate_trace_options(args)
    if option_error:
        print(f"error: {option_error}", file=sys.stderr)
        return 2

    preset_name = args.preset or str(config.get("default_preset", "icon-clean"))
    if preset_name not in PRESETS:
        print(f"error: unknown preset: {preset_name}", file=sys.stderr)
        print_presets()
        return 2

    items = collect_sources(args.input, output_dir, recursive)
    if not items:
        print("error: no supported raster input files found", file=sys.stderr)
        return 1

    collisions = detect_destination_collisions(items)
    if collisions:
        print("error: multiple inputs would write the same SVG destination:", file=sys.stderr)
        for collision in collisions:
            print(f"  {collision}", file=sys.stderr)
        return 1

    preset = PRESETS[preset_name]
    if args.threshold is not None:
        if not 0 <= args.threshold <= 255:
            print("error: --threshold must be between 0 and 255", file=sys.stderr)
            return 2
        if not preset.force_bw:
            print("error: --threshold can only be used with a monochrome preset", file=sys.stderr)
            return 2
        preset = replace(preset, threshold=args.threshold)
    if args.supersample is not None:
        if not preset.force_bw:
            print("error: --supersample can only be used with a monochrome preset", file=sys.stderr)
            return 2
        preset = replace(preset, supersample=args.supersample)
    results: list[Result] = []

    for item in items:
        if args.dry_run:
            if item.destination.exists() and skip_existing:
                results.append(Result("skipped", item.source, item.destination, "output exists"))
            else:
                results.append(Result("planned", item.source, item.destination))
            print(f"{results[-1].status}: {item.source} -> {item.destination}")
            continue

        try:
            result = convert_one(item, preset, skip_existing)
        except Exception as exc:  # noqa: BLE001 - report every conversion failure and keep batch going.
            result = Result("failed", item.source, item.destination, str(exc))
        results.append(result)
        extra = f" ({result.message})" if result.message else ""
        print(f"{result.status}: {result.source} -> {result.destination}{extra}")

    if args.open_inkscape and not args.dry_run:
        for warning in open_in_inkscape(results):
            print(f"warn: {warning}", file=sys.stderr)

    if not args.dry_run:
        settings: dict[str, Any] = {"preset": preset_name}
        if preset.force_bw:
            settings["threshold"] = preset.threshold
            settings["supersample"] = preset.supersample
        write_log(log_path, args, "raster-to-svg", settings, results)

    print_summary(results, args.dry_run, log_path)
    return 1 if any(result.status == "failed" for result in results) else 0


def run_export(
    args: argparse.Namespace,
    output_formats: list[str],
    output_dir: Path,
    skip_existing: bool,
    recursive: bool,
    log_path: Path,
) -> int:
    if args.preset is not None or args.threshold is not None or args.supersample is not None:
        print("error: tracing presets, threshold, and supersample do not apply to SVG export", file=sys.stderr)
        return 2
    if args.open_inkscape:
        print("error: --open-inkscape only applies to raster-to-SVG conversion", file=sys.stderr)
        return 2

    raw_sizes = args.size or [None]
    sizes: list[int | None] = []
    for size in raw_sizes:
        if size is not None and not 1 <= size <= MAX_EXPORT_SIZE:
            print(
                f"error: --size values must be between 1 and {MAX_EXPORT_SIZE} pixels",
                file=sys.stderr,
            )
            return 2
        if size not in sizes:
            sizes.append(size)

    jpg_quality = args.jpg_quality if args.jpg_quality is not None else 95
    if not 1 <= jpg_quality <= 100:
        print("error: --jpg-quality must be between 1 and 100", file=sys.stderr)
        return 2
    if args.jpg_quality is not None and "jpg" not in output_formats:
        print("error: --jpg-quality requires JPG output", file=sys.stderr)
        return 2

    try:
        background = parse_background(args.background)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    if background is not None and background[3] < 255 and "jpg" in output_formats:
        print("error: JPG output requires an opaque --background colour", file=sys.stderr)
        return 2

    items = collect_svg_exports(
        args.input,
        output_dir,
        recursive,
        output_formats,
        sizes,
    )
    if not items:
        print("error: no supported SVG input files found", file=sys.stderr)
        return 1

    collisions = detect_destination_collisions(items)
    if collisions:
        print("error: multiple inputs would write the same raster destination:", file=sys.stderr)
        for collision in collisions:
            print(f"  {collision}", file=sys.stderr)
        return 1

    results: list[Result] = []
    render_cache: dict[tuple[Path, int | None], bytes] = {}
    natural_size_cache: dict[Path, tuple[int, int]] = {}
    for item in items:
        if args.dry_run:
            if item.destination.exists() and skip_existing:
                result = Result("skipped", item.source, item.destination, "output exists")
            else:
                result = Result("planned", item.source, item.destination)
        else:
            try:
                result = convert_svg_one(
                    item,
                    item.size,
                    skip_existing,
                    background,
                    jpg_quality,
                    render_cache,
                    natural_size_cache,
                )
            except Exception as exc:  # noqa: BLE001 - keep batch conversion moving.
                result = Result("failed", item.source, item.destination, str(exc))
        results.append(result)
        extra = f" ({result.message})" if result.message else ""
        print(f"{result.status}: {item.source} -> {item.destination}{extra}")

    if not args.dry_run:
        settings = {
            "formats": ",".join(output_formats),
            "sizes": ",".join("natural" if size is None else str(size) for size in sizes),
            "background": args.background or "transparent PNG / white JPG",
            "jpg_quality": jpg_quality,
        }
        write_log(log_path, args, "svg-to-raster", settings, results)

    print_summary(results, args.dry_run, log_path)
    return 1 if any(result.status == "failed" for result in results) else 0


def main() -> int:
    args = parse_args()

    if args.list_presets:
        print_presets()
        return 0
    if not args.input:
        print("error: --input is required unless --list-presets is used", file=sys.stderr)
        return 2

    output_formats: list[str] = []
    for output_format in args.to:
        normalized = "jpg" if output_format == "jpeg" else output_format
        if normalized not in output_formats:
            output_formats.append(normalized)
    if "svg" in output_formats and len(output_formats) > 1:
        print("error: SVG output cannot be combined with PNG/JPG output in one run", file=sys.stderr)
        return 2

    config = load_config(Path(args.config).expanduser())
    output_dir = Path(args.output or str(config.get("default_output", "output"))).expanduser()
    skip_existing = resolve_bool(args.skip_existing, config, "skip_existing")
    recursive = resolve_bool(args.recursive, config, "recursive")
    log_path = Path(args.log).expanduser() if args.log else output_dir / "svg-forge.log"

    if output_formats == ["svg"]:
        return run_trace(
            args,
            config,
            output_dir,
            skip_existing,
            recursive,
            log_path,
        )
    return run_export(
        args,
        output_formats,
        output_dir,
        skip_existing,
        recursive,
        log_path,
    )


if __name__ == "__main__":
    raise SystemExit(main())
