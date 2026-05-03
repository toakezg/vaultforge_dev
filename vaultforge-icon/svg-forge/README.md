# SVG-Forge

SVG-Forge is a small Windows-friendly raster-to-SVG batch converter for icon,
logo, and glyph workflows. It uses VTracer as the vector tracing engine and
keeps the wrapper simple: folder in, SVG files out, with presets and a log.

## Install

From this folder:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Or run the helper:

```bat
setup_venv.bat
```

## Quick Start

```bat
run_svg_forge.bat --input ".\samples" --output ".\output" --preset icon-clean
```

The direct Python form is:

```powershell
.\.venv\Scripts\python.exe .\svg_forge.py --input ".\samples" --output ".\output" --preset icon-clean
```

## Inputs

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
| `glyph-bw` | Black/white symbols, masks, and simple UI glyphs |
| `flat-colour` | Reduced-palette colour icons |
| `detailed-colour` | More detailed colour illustrations |

List presets:

```bat
run_svg_forge.bat --list-presets
```

## Useful Flags

Dry-run without writing output or a log file:

```bat
run_svg_forge.bat --input ".\samples" --preset icon-clean --dry-run
```

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

Normal conversion runs append a text log at:

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

It writes PNG, JPG, and WebP sample files into `.\samples`.

## Troubleshooting

If `vtracer` is missing:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

If WebP conversion fails, reinstall Pillow:

```powershell
.\.venv\Scripts\python.exe -m pip install --force-reinstall Pillow
```

If an older `.venv` points at a missing Python path, delete only this tool's
local `.venv` folder and rerun `setup_venv.bat`.
