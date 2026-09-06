# SVG-Forge Changelog

## 2026-08-18

- Added same-script SVG-to-PNG/JPG export through `--to png`, `--to jpg`, or
  `--to png jpg`, powered by the Windows-friendly resvg renderer.
- Added proportional multi-size export through `--size`, using the requested
  value as the longest edge so logos are never stretched.
- Added transparent PNG output, white-by-default JPG output, configurable
  `--background`, and high-quality 4:4:4 JPEG output with `--jpg-quality`.
- Added stable size-labelled filenames, SVG/SVGZ batch and recursive input,
  render caching across PNG/JPG pairs, dry-run planning, and export logging.
- Added SVG raster-export regression and integration coverage.
- Added the `logo-mono-hq` preset for black/white and single-colour logos. It
  traces a 4x Lanczos-supersampled binary contour and preserves the source
  display dimensions through the generated SVG `viewBox`.
- Added monochrome `--threshold` and `--supersample` overrides, with validation
  that prevents them from silently changing colour presets.
- Added regression tests for supersampled preparation, SVG normalization, and
  an end-to-end VTracer conversion.

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
