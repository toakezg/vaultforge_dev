from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw


ROOT = Path(__file__).resolve().parents[1]
SAMPLES = ROOT / "samples"


def make_icon(path: Path) -> None:
    image = Image.new("RGBA", (256, 256), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    draw.rounded_rectangle((32, 32, 224, 224), radius=44, fill=(32, 104, 168, 255))
    draw.polygon(
        [
            (128, 54),
            (148, 104),
            (202, 108),
            (160, 142),
            (174, 196),
            (128, 166),
            (82, 196),
            (96, 142),
            (54, 108),
            (108, 104),
        ],
        fill=(255, 218, 86, 255),
    )
    image.save(path)


def make_logo(path: Path) -> None:
    image = Image.new("RGB", (360, 220), (250, 250, 246))
    draw = ImageDraw.Draw(image)
    draw.rectangle((34, 54, 144, 166), fill=(26, 31, 44))
    draw.rectangle((120, 76, 228, 188), fill=(214, 76, 64))
    draw.rectangle((204, 34, 326, 146), fill=(44, 140, 112))
    draw.line((34, 188, 326, 188), fill=(26, 31, 44), width=10)
    image.save(path, quality=92)


def make_glyph(path: Path) -> None:
    image = Image.new("RGBA", (240, 240), (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)
    draw.polygon(
        [(124, 20), (58, 130), (116, 130), (88, 220), (184, 96), (130, 96)],
        fill=(14, 14, 14, 255),
    )
    image.save(path)


def main() -> int:
    SAMPLES.mkdir(parents=True, exist_ok=True)
    make_icon(SAMPLES / "icon-star.png")
    make_logo(SAMPLES / "logo-blocks.jpg")
    make_glyph(SAMPLES / "glyph-bolt.webp")
    print(f"wrote samples to {SAMPLES}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
