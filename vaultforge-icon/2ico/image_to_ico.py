#!/usr/bin/env python3
"""Convert one image or a folder of images into Windows .ico files."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

try:
    from PIL import Image, UnidentifiedImageError
except ImportError:  # pragma: no cover - exercised before dependency install
    print(
        "Pillow is required. Run setup_venv.bat, or install with: py -m pip install -r requirements.txt",
        file=sys.stderr,
    )
    raise SystemExit(2)


SUPPORTED_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp", ".bmp", ".gif", ".tif", ".tiff"}
DEFAULT_SIZES = (16, 24, 32, 48, 64, 128, 256)


def parse_sizes(value: str) -> tuple[int, ...]:
    sizes: list[int] = []
    for raw_part in value.split(","):
        part = raw_part.strip().lower()
        if not part:
            continue
        if "x" in part:
            width, height = part.split("x", 1)
            if width != height:
                raise argparse.ArgumentTypeError("ICO sizes must be square, such as 32 or 32x32.")
            part = width
        try:
            size = int(part)
        except ValueError as exc:
            raise argparse.ArgumentTypeError(f"Invalid ICO size: {raw_part!r}") from exc
        if size < 1 or size > 256:
            raise argparse.ArgumentTypeError("ICO sizes must be between 1 and 256.")
        sizes.append(size)
    if not sizes:
        raise argparse.ArgumentTypeError("At least one ICO size is required.")
    return tuple(dict.fromkeys(sizes))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Convert image files to .ico files. Input can be one image file or a directory.",
    )
    parser.add_argument("--input", "-i", required=False, help="Image file or directory containing images.")
    parser.add_argument("--output", "-o", required=False, help="Output .ico file or output directory.")
    parser.add_argument(
        "--batch",
        action="store_true",
        help="Treat --input as batch-capable. Directories batch automatically even without this flag.",
    )
    parser.add_argument(
        "--recursive",
        action="store_true",
        help="When input is a directory, include images in subdirectories and mirror relative folders.",
    )
    parser.add_argument(
        "--sizes",
        type=parse_sizes,
        default=DEFAULT_SIZES,
        help="Comma-separated icon sizes. Default: 16,24,32,48,64,128,256.",
    )
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing .ico files.")
    parser.add_argument(
        "--skip-existing",
        action="store_true",
        help="Skip files whose target already exists instead of creating a numbered name.",
    )
    parser.add_argument("--dry-run", action="store_true", help="Show planned conversions without writing files.")
    parser.add_argument("--list-formats", action="store_true", help="Print supported input file extensions and exit.")
    return parser


def gather_inputs(input_path: Path, recursive: bool) -> list[Path]:
    if input_path.is_file():
        if input_path.suffix.lower() not in SUPPORTED_EXTENSIONS:
            raise ValueError(f"Unsupported input file type: {input_path.suffix}")
        return [input_path]

    if input_path.is_dir():
        pattern = "**/*" if recursive else "*"
        files = [
            path
            for path in input_path.glob(pattern)
            if path.is_file() and path.suffix.lower() in SUPPORTED_EXTENSIONS
        ]
        return sorted(files, key=lambda path: str(path).lower())

    raise FileNotFoundError(f"Input path not found: {input_path}")


def unique_path(path: Path) -> Path:
    if not path.exists():
        return path
    for index in range(1, 10000):
        candidate = path.with_name(f"{path.stem}-{index}{path.suffix}")
        if not candidate.exists():
            return candidate
    raise RuntimeError(f"Could not find a free output name for {path}")


def output_for(input_file: Path, input_root: Path, output_arg: Path | None, recursive: bool) -> Path:
    if output_arg is None:
        return input_file.with_suffix(".ico")

    if input_root.is_file():
        if output_arg.suffix.lower() == ".ico":
            return output_arg
        return output_arg / f"{input_file.stem}.ico"

    relative = input_file.relative_to(input_root) if recursive else Path(input_file.name)
    return output_arg / relative.with_suffix(".ico")


def convert_one(input_file: Path, output_file: Path, sizes: tuple[int, ...], dry_run: bool) -> None:
    if dry_run:
        return

    output_file.parent.mkdir(parents=True, exist_ok=True)
    with Image.open(input_file) as image:
        rgba_image = image.convert("RGBA")
        max_size = max(sizes)
        rgba_image.thumbnail((max_size, max_size), Image.Resampling.LANCZOS)
        canvas = Image.new("RGBA", (max_size, max_size), (0, 0, 0, 0))
        offset = ((max_size - rgba_image.width) // 2, (max_size - rgba_image.height) // 2)
        canvas.alpha_composite(rgba_image, dest=offset)
        canvas.save(output_file, format="ICO", sizes=[(size, size) for size in sizes])


def run(args: argparse.Namespace) -> int:
    if args.list_formats:
        print("Supported input extensions:")
        for extension in sorted(SUPPORTED_EXTENSIONS):
            print(f"  {extension}")
        return 0

    if not args.input:
        raise ValueError("--input is required unless --list-formats is used.")

    input_path = Path(args.input).expanduser().resolve()
    output_path = Path(args.output).expanduser().resolve() if args.output else None
    input_files = gather_inputs(input_path, args.recursive)

    if not input_files:
        print(f"No supported images found in {input_path}")
        return 1

    converted = 0
    skipped = 0
    failed = 0

    for input_file in input_files:
        target = output_for(input_file, input_path, output_path, args.recursive)
        if target.exists() and args.skip_existing:
            print(f"skipped existing: {input_file} -> {target}")
            skipped += 1
            continue
        if target.exists() and not args.overwrite:
            target = unique_path(target)

        print(f"{'planned' if args.dry_run else 'converted'}: {input_file} -> {target}")

        try:
            convert_one(input_file, target, args.sizes, args.dry_run)
            converted += 1
        except (OSError, UnidentifiedImageError, ValueError) as exc:
            print(f"failed: {input_file} ({exc})", file=sys.stderr)
            failed += 1

    if args.dry_run:
        print("Dry run complete. No ICO files were written.")
    print(f"summary: converted={converted} skipped={skipped} failed={failed}")
    return 1 if failed else 0


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    try:
        return run(args)
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
