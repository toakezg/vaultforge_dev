# SVG-Forge Real Samples Decision

Date: 2026-05-04

## Decision

Do not generate real SVG-Forge sample rasters in the current docs-only
rotation.

Real sample rasters are still useful for a future conversion smoke test, but
they are a write step and should be run only in a later live/write validation
task. The current safe path remains the existing `samples\dry-run-only`
placeholder command for no-write source discovery.

## Current Evidence

- `tools\make_samples.py` creates `samples\icon-star.png`,
  `samples\logo-blocks.jpg`, and `samples\glyph-bolt.webp`.
- `samples\README.md` already labels that helper as a write step.
- `samples\dry-run-only\README.md` says the placeholder is not a real image and
  should only be used with `--dry-run`.
- `svg-forge\output\` already contains prior local conversion outputs, but
  cleanup or deletion is not part of this decision.

## Cleanup Expectation

Do not move or delete existing SVG-Forge assets or prior output snapshots as
part of sample validation. If a future live smoke test writes files, use a
dedicated output folder and leave cleanup as a separate explicit task unless
Nath approves removal.

## Future Live Validation

When a later task explicitly allows file writes, run from
`vaultforge-icon\svg-forge`:

```powershell
.\.venv\Scripts\python.exe .\tools\make_samples.py
.\run_svg_forge.bat --input ".\samples" --output ".\output\real-sample-smoke" --preset icon-clean
```

Expected write scope:

- `samples\icon-star.png`
- `samples\logo-blocks.jpg`
- `samples\glyph-bolt.webp`
- `output\real-sample-smoke\*.svg`
- `output\real-sample-smoke\svg-forge.log`

The smoke test should record command, exit code, written paths, and whether the
generated SVG/log files are inspectable.
