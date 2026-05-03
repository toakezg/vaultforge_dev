from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


SUPPORTED_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp"}
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
        description="Batch convert PNG/JPG/WebP raster images to SVG with VTracer.",
    )
    parser.add_argument(
        "--input",
        nargs="+",
        help="Input file(s) or folder(s). Folders are scanned for supported raster files.",
    )
    parser.add_argument(
        "--output",
        help="Output folder. Defaults to the config default_output value.",
    )
    parser.add_argument(
        "--preset",
        choices=sorted(PRESETS),
        help="Tracing preset to use. Defaults to the config default_preset value.",
    )
    parser.add_argument(
        "--config",
        default=str(script_dir() / "svg_forge.config.json"),
        help="Path to the JSON config file.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show planned conversions without writing SVGs, folders, or logs.",
    )
    parser.add_argument(
        "--skip-existing",
        action="store_true",
        default=None,
        help="Skip output files that already exist.",
    )
    parser.add_argument(
        "--recursive",
        action="store_true",
        default=None,
        help="Scan input folders recursively and preserve subfolders under output.",
    )
    parser.add_argument(
        "--log",
        help="Conversion log path. Defaults to <output>\\svg-forge.log.",
    )
    parser.add_argument(
        "--open-inkscape",
        "--open-after-convert",
        action="store_true",
        help="Open converted SVG files in Inkscape when Inkscape is available.",
    )
    parser.add_argument(
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
    return path.is_file() and path.suffix.lower() in SUPPORTED_EXTENSIONS


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


def prepare_input(source: Path, preset: Preset, temp_dir: Path) -> Path:
    needs_png_copy = source.suffix.lower() == ".webp" or preset.force_bw
    if not needs_png_copy:
        return source

    Image, ImageOps = require_pillow()
    prepared = temp_dir / f"{source.stem}.prepared.png"

    with Image.open(source) as image:
        if preset.force_bw:
            rgba = image.convert("RGBA")
            background = Image.new("RGBA", rgba.size, "WHITE")
            flattened = Image.alpha_composite(background, rgba)
            grayscale = ImageOps.grayscale(flattened)
            bw = grayscale.point(lambda value: 0 if value < 128 else 255, mode="1")
            bw.save(prepared)
        else:
            image.convert("RGBA").save(prepared)

    return prepared


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
            str(prepared_input),
            str(item.destination),
            *ordered_settings,
        )

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


def write_log(log_path: Path, args: argparse.Namespace, preset_name: str, results: list[Result]) -> None:
    log_path.parent.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(timezone.utc).isoformat(timespec="seconds")
    command = " ".join([Path(sys.executable).name, *sys.argv])

    with log_path.open("a", encoding="utf-8") as file:
        file.write(f"=== SVG-Forge run {timestamp} ===\n")
        file.write(f"command: {command}\n")
        file.write(f"preset: {preset_name}\n")
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
        print("Dry run complete. No folders, SVG files, or logs were written.")
    else:
        print("Conversion run complete.")

    for status in sorted(counts):
        print(f"  {status}: {counts[status]}")

    if log_path and not dry_run:
        print(f"  log: {log_path}")


def main() -> int:
    args = parse_args()

    if args.list_presets:
        print_presets()
        return 0

    config = load_config(Path(args.config).expanduser())
    preset_name = args.preset or str(config.get("default_preset", "icon-clean"))
    if preset_name not in PRESETS:
        print(f"error: unknown preset: {preset_name}", file=sys.stderr)
        print_presets()
        return 2

    if not args.input:
        print("error: --input is required unless --list-presets is used", file=sys.stderr)
        return 2

    output_dir = Path(args.output or str(config.get("default_output", "output"))).expanduser()
    skip_existing = resolve_bool(args.skip_existing, config, "skip_existing")
    recursive = resolve_bool(args.recursive, config, "recursive")
    log_path = Path(args.log).expanduser() if args.log else output_dir / "svg-forge.log"

    items = collect_sources(args.input, output_dir, recursive)
    if not items:
        print("error: no supported input files found", file=sys.stderr)
        return 1

    collisions = detect_destination_collisions(items)
    if collisions:
        print("error: multiple inputs would write the same SVG destination:", file=sys.stderr)
        for collision in collisions:
            print(f"  {collision}", file=sys.stderr)
        return 1

    preset = PRESETS[preset_name]
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
        write_log(log_path, args, preset_name, results)

    print_summary(results, args.dry_run, log_path)
    return 1 if any(result.status == "failed" for result in results) else 0


if __name__ == "__main__":
    raise SystemExit(main())
