# SVG-Forge

SVG-Forge is a small Windows-friendly two-way converter for icon, logo, and
glyph workflows. It uses VTracer to clean and trace raster images into SVG, and
resvg to render finished SVG masters back into high-quality PNG and JPG copies.
Both directions support file or folder batches, dry runs, and logs.

All commands below assume the current folder is `vaultforge\svg-forge`.

## Install

From this folder:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

There is no setup batch helper in this folder yet. Use the commands above when
you need to rebuild the local environment.

If a future `setup_venv.bat` is added, keep it as a thin wrapper around those
same commands.

## Quick Start

```bat
run_svg_forge.bat --input ".\samples" --output ".\output" --preset icon-clean
```

The direct Python form is:

```powershell
.\.venv\Scripts\python.exe .\svg_forge.py --input ".\samples" --output ".\output" --preset icon-clean
```

## Export SVG to PNG and JPG

Keep the SVG as the master and create practical raster copies from it with
`--to`. This example makes three proportional size tiers in both formats:

```bat
run_svg_forge.bat --input ".\output\barber-logo.svg" --output ".\output\barber-raster" --to png jpg --size 512 1024 2048
```

The `--size` value is the longest edge in pixels. SVG-Forge preserves the
logo's aspect ratio, so a 2:1 landscape logo exported at `1024` becomes
`1024x512`; it is never stretched into a square. The generated names are:

```text
barber-logo-512px.png
barber-logo-512px.jpg
barber-logo-1024px.png
barber-logo-1024px.jpg
barber-logo-2048px.png
barber-logo-2048px.jpg
```

Use a transparent PNG as the best raster working copy for editing and quick
variants. JPG cannot store transparency, so it gets a white background by
default and is best treated as a compatibility or delivery copy.

To use the SVG's natural dimensions, omit `--size`:

```bat
run_svg_forge.bat --input ".\output\barber-logo.svg" --to png jpg
```

To choose a background for both outputs, quote the colour in PowerShell or a
batch command when it begins with `#`:

```bat
run_svg_forge.bat --input ".\output\barber-logo.svg" --to png jpg --size 2048 --background "#F4F0E8"
```

For a white-fill logo, choose a dark JPG background such as `--background
"#111111"`. JPG backgrounds must be opaque because JPEG has no alpha channel.
If you want a transparent PNG plus a coloured JPG, run them separately so the
background is applied only to the JPG:

```bat
run_svg_forge.bat --input ".\output\barber-logo.svg" --output ".\logo-delivery" --to png --size 512 1024 2048
run_svg_forge.bat --input ".\output\barber-logo.svg" --output ".\logo-delivery" --to jpg --size 512 1024 2048 --background "#111111"
```

JPG defaults to quality 95 with full-colour 4:4:4 subsampling, which avoids the
extra colour-edge smearing common in logo JPEGs. You can govern it explicitly:

```bat
run_svg_forge.bat --input ".\output\barber-logo.svg" --to jpg --size 2048 --jpg-quality 98
```

Multiple SVGs and recursive folders work the same way as raster inputs:

```bat
run_svg_forge.bat --input ".\logo-masters" --output ".\logo-delivery" --to png jpg --size 512 2048 --recursive
```

Supported vector inputs are `.svg` and `.svgz`. Export sizes can range from 1
to 16384 pixels on the longest edge. The high-quality renderer uses system
fonts and resolves linked SVG resources relative to each source file.

## Raster Inputs

Supported input files:

- `.png`
- `.jpg`
- `.jpeg`
- `.webp`

You can pass one folder, multiple folders, one file, or a list of explicit files:

```bat
run_svg_forge.bat --input ".\samples"
run_svg_forge.bat --input ".\samples\a.png" ".\samples\b.webp"
run_svg_forge.bat --input ".\samples" --recursive
```

Filenames are preserved by default. For example, `quest-icon.png` becomes
`quest-icon.svg`.

## Presets

| Preset | Best for |
| --- | --- |
| `icon-clean` | Small icons with readable silhouettes |
| `logo-clean` | Logo marks and cleaner brand shapes |
| `logo-mono-hq` | High-quality black/white or single-colour logos |
| `glyph-bw` | Black/white symbols, masks, and simple UI glyphs |
| `flat-colour` | Reduced-palette colour icons |
| `detailed-colour` | More detailed colour illustrations |

List presets:

```bat
run_svg_forge.bat --list-presets
```

### High-Quality Monochrome Logos

Use `logo-mono-hq` for black/white or single-colour logos, especially when a
JPEG edge produces small stair-steps after ordinary tracing:

```bat
run_svg_forge.bat --input "F:\logos\source.jpg" --output "F:\logos\svg-review" --preset logo-mono-hq
```

This preset enlarges the raster contour internally before tracing and then
normalizes the SVG back to the source dimensions with a `viewBox`. The result
keeps the same displayed size while allowing the fitted curve to land between
the original pixel coordinates. Its white/background area becomes transparent.

The default uses 4x contour supersampling and a black/white threshold of 128.
For unusually soft or faint source artwork, either value can be overridden:

```bat
run_svg_forge.bat --input ".\logo.jpg" --preset logo-mono-hq --threshold 144
run_svg_forge.bat --input ".\logo.jpg" --preset logo-mono-hq --supersample 8
```

Supported supersampling factors are `1`, `2`, `3`, `4`, and `8`. Higher values
can produce larger SVG files and slower conversions. Threshold and supersample
overrides are intentionally limited to monochrome presets; use `logo-clean` for
logos whose separate colours must be preserved.

## Useful Flags

Dry-run without writing output or a log file:

```bat
run_svg_forge.bat --input ".\samples" --preset icon-clean --dry-run
```

Stable dry-run smoke check when generated sample rasters are absent:

```bat
run_svg_forge.bat --input ".\samples\dry-run-only" --output ".\output\dry-run-check" --preset icon-clean --dry-run
```

Expected result:

```text
planned: ...dry-run-placeholder.png -> ...dry-run-placeholder.svg
Dry run complete. No folders, output files, or logs were written.
  planned: 1
```

The `samples\dry-run-only` placeholder is intentionally not a real image. Use it
only with `--dry-run`; run `tools\make_samples.py` first when you need real
conversion samples.

Skip files that already have an SVG output:

```bat
run_svg_forge.bat --input ".\samples" --preset icon-clean --skip-existing
```

Write to a custom output folder:

```bat
run_svg_forge.bat --input "F:\icons\png" --output "F:\icons\svg" --preset flat-colour
```

Open converted SVGs in Inkscape when Inkscape is installed:

```bat
run_svg_forge.bat --input ".\samples" --preset logo-clean --open-inkscape
```

## Config

Defaults live in `svg_forge.config.json`:

```json
{
  "default_preset": "icon-clean",
  "default_output": "output",
  "skip_existing": false,
  "recursive": false
}
```

CLI flags override config values.

## Logs

Normal conversion and export runs append a text log at:

```text
output\svg-forge.log
```

If `--output` points somewhere else, the default log moves with that output
folder. Dry-run mode does not write a log because it is intended to be no-write.

## Make Sample Images

The repo includes a small helper for creating local sample rasters:

```powershell
.\.venv\Scripts\python.exe .\tools\make_samples.py
```

It writes PNG, JPG, and WebP sample files into `.\samples`. This is a real file
creation step. For no-write checks, use the `samples\dry-run-only` command in
Useful Flags instead.

## Troubleshooting

If `vtracer` is missing:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

If WebP conversion fails, reinstall Pillow:

```powershell
.\.venv\Scripts\python.exe -m pip install --force-reinstall Pillow
```

If SVG-to-PNG/JPG export reports that `resvg_py` is missing, install the pinned
project dependencies:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

If an older `.venv` points at a missing Python path, rebuild only this tool's
local `.venv` folder with the Install commands above.
