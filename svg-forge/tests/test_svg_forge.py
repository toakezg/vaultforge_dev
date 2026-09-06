from __future__ import annotations

import sys
import tempfile
import unittest
from io import BytesIO
from pathlib import Path

from PIL import Image, ImageDraw


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

import svg_forge  # noqa: E402


class HighQualityMonochromeTests(unittest.TestCase):
    def test_hq_preset_has_explicit_monochrome_contract(self) -> None:
        preset = svg_forge.PRESETS["logo-mono-hq"]

        self.assertTrue(preset.force_bw)
        self.assertEqual(preset.threshold, 128)
        self.assertEqual(preset.supersample, 4)
        self.assertEqual(preset.settings["colormode"], "binary")
        self.assertEqual(preset.settings["length_threshold"], 8.0)

    def test_prepare_input_supersamples_before_thresholding(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            temp_dir = Path(temp)
            source = temp_dir / "source.png"
            image = Image.new("L", (3, 2), 255)
            image.putpixel((0, 0), 0)
            image.save(source)

            prepared = svg_forge.prepare_input(
                source,
                svg_forge.PRESETS["logo-mono-hq"],
                temp_dir,
            )

            self.assertEqual(prepared.source_size, (3, 2))
            self.assertEqual(prepared.trace_size, (12, 8))
            with Image.open(prepared.path) as result:
                self.assertEqual(result.size, (12, 8))
                self.assertEqual(result.mode, "1")
                self.assertEqual(result.getextrema(), (0, 255))

    def test_normalize_supersampled_svg_preserves_display_dimensions(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            svg_path = Path(temp) / "shape.svg"
            svg_path.write_text(
                '<svg xmlns="http://www.w3.org/2000/svg" width="400" height="200">'
                '<path d="M0 0 L400 0 L400 200 Z"/></svg>',
                encoding="utf-8",
            )

            svg_forge.normalize_supersampled_svg(svg_path, (100, 50), (400, 200))
            svg = svg_path.read_text(encoding="utf-8")

            self.assertIn('width="100"', svg)
            self.assertIn('height="50"', svg)
            self.assertIn('viewBox="0 0 400 200"', svg)
            self.assertEqual(svg.count("viewBox="), 1)

    def test_convert_one_writes_normalized_hq_svg(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            temp_dir = Path(temp)
            source = temp_dir / "logo.png"
            destination = temp_dir / "logo.svg"
            image = Image.new("RGB", (32, 24), "white")
            draw = ImageDraw.Draw(image)
            draw.ellipse((5, 3, 27, 21), fill="black")
            image.save(source)

            result = svg_forge.convert_one(
                svg_forge.SourceItem(source, destination),
                svg_forge.PRESETS["logo-mono-hq"],
                skip_existing=False,
            )
            svg = destination.read_text(encoding="utf-8")

            self.assertEqual(result.status, "converted")
            self.assertIn('width="32"', svg)
            self.assertIn('height="24"', svg)
            self.assertIn('viewBox="0 0 128 96"', svg)


class SvgRasterExportTests(unittest.TestCase):
    def test_collect_svg_exports_builds_formats_and_proportional_size_names(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            temp_dir = Path(temp)
            source = temp_dir / "barber-logo.svg"
            source.write_text(
                '<svg xmlns="http://www.w3.org/2000/svg" width="200" height="100"/>',
                encoding="utf-8",
            )

            items = svg_forge.collect_svg_exports(
                [str(source)],
                temp_dir / "exports",
                recursive=False,
                output_formats=["png", "jpg"],
                sizes=[512, 2048],
            )

            self.assertEqual(len(items), 4)
            self.assertEqual(
                {item.destination.name for item in items},
                {
                    "barber-logo-512px.png",
                    "barber-logo-512px.jpg",
                    "barber-logo-2048px.png",
                    "barber-logo-2048px.jpg",
                },
            )
            self.assertEqual({item.size for item in items}, {512, 2048})

    def test_natural_export_does_not_infer_size_from_source_name(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            temp_dir = Path(temp)
            source = temp_dir / "barber-logo-512px.svg"
            source.write_text(
                '<svg xmlns="http://www.w3.org/2000/svg" width="200" height="100"/>',
                encoding="utf-8",
            )

            items = svg_forge.collect_svg_exports(
                [str(source)],
                temp_dir / "exports",
                recursive=False,
                output_formats=["png"],
                sizes=[None],
            )

            self.assertEqual(items[0].destination.name, "barber-logo-512px.png")
            self.assertIsNone(items[0].size)

    def test_render_svg_png_uses_longest_edge_and_preserves_aspect_ratio(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            temp_dir = Path(temp)
            source = temp_dir / "wide-logo.svg"
            source.write_text(
                '<svg xmlns="http://www.w3.org/2000/svg" width="200" height="100">'
                '<rect width="200" height="100" fill="#111111"/></svg>',
                encoding="utf-8",
            )

            png_bytes = svg_forge.render_svg_png(source, 512, {})

            with Image.open(BytesIO(png_bytes)) as rendered:
                self.assertEqual(rendered.size, (512, 256))

    def test_png_is_transparent_and_jpg_uses_white_background(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            temp_dir = Path(temp)
            source = temp_dir / "mark.svg"
            source.write_text(
                '<svg xmlns="http://www.w3.org/2000/svg" width="100" height="50">'
                '<circle cx="50" cy="25" r="20" fill="#000000"/></svg>',
                encoding="utf-8",
            )
            png_destination = temp_dir / "mark-200px.png"
            jpg_destination = temp_dir / "mark-200px.jpg"
            render_cache: dict[tuple[Path, int | None], bytes] = {}
            natural_size_cache: dict[Path, tuple[int, int]] = {}

            for destination in (png_destination, jpg_destination):
                result = svg_forge.convert_svg_one(
                    svg_forge.SourceItem(source, destination, 200),
                    size=200,
                    skip_existing=False,
                    background=None,
                    jpg_quality=95,
                    render_cache=render_cache,
                    natural_size_cache=natural_size_cache,
                )
                self.assertEqual(result.status, "converted")

            self.assertEqual(len(render_cache), 1)
            with Image.open(png_destination) as png:
                self.assertEqual(png.size, (200, 100))
                self.assertEqual(png.convert("RGBA").getpixel((0, 0))[3], 0)
            with Image.open(jpg_destination) as jpg:
                self.assertEqual(jpg.size, (200, 100))
                corner = jpg.convert("RGB").getpixel((0, 0))
                self.assertTrue(all(channel >= 250 for channel in corner))


if __name__ == "__main__":
    unittest.main()
