# SVG-Forge Changelog

## 2026-05-04

- Ran the real sample smoke path after explicit approval: generated
  `samples\icon-star.png`, `samples\logo-blocks.jpg`, and
  `samples\glyph-bolt.webp`, then converted them with `icon-clean` into
  `output\real-sample-smoke\icon-star.svg`,
  `output\real-sample-smoke\logo-blocks.svg`,
  `output\real-sample-smoke\glyph-bolt.svg`, and
  `output\real-sample-smoke\svg-forge.log`.

## 2026-05-03

- Added a `samples\dry-run-only` fixture path and README guidance so dry-run
  smoke checks have a stable expected result even before generated raster
  samples exist.
- Clarified the setup docs so the manual virtual environment commands are the
  source of truth and removed the stale reference to a missing `setup_venv.bat`
  helper.

## 2026-05-01

- Added the first CLI-first SVG-Forge implementation.
- Added VTracer-backed batch conversion for PNG, JPG, JPEG, and WebP inputs.
- Added presets, dry-run, skip-existing, config defaults, conversion logging, and Windows batch launchers.
