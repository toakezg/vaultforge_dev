# Samples

Run this from `vaultforge-icon\svg-forge` after installing dependencies:

```powershell
.\.venv\Scripts\python.exe .\tools\make_samples.py
```

The helper writes a few simple PNG, JPG, and WebP files here for smoke tests.

This is a write step. For no-write dry-run smoke checks, use:

```bat
run_svg_forge.bat --input ".\samples\dry-run-only" --output ".\output\dry-run-check" --preset icon-clean --dry-run
```
