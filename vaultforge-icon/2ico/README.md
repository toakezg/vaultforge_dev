# 2ico

2ico is a small Windows-friendly image-to-ICO converter for single files and
batch folders.

## Install

From this folder:

```bat
setup_venv.bat
```

## Quick Start

Single file:

```bat
run_2ico.bat --input ".\samples\icon.png" --output ".\output"
```

Batch folder:

```bat
run_2ico.bat --batch --input ".\samples" --output ".\output"
```

Direct Python form:

```powershell
.\.venv\Scripts\python.exe .\image_to_ico.py --batch --input ".\samples" --output ".\output"
```

## Launchers

- `setup_venv.bat` creates the local Python environment and installs Pillow.
- `run_2ico.bat` passes terminal arguments straight to the CLI.
- `run_2ico_batch.bat` prompts for input and output paths, then runs batch mode.
- `run_2ico_input.bat` prompts for one input path, one output path, and optional sizes.

## Inputs

Supported input files:

- `.png`
- `.jpg`
- `.jpeg`
- `.webp`
- `.bmp`
- `.gif`
- `.tif`
- `.tiff`

Input can be a single image file or a directory. Directories are scanned only at
the top level unless `--recursive` is used.

## Useful Flags

Dry run:

```bat
run_2ico.bat --batch --input ".\samples" --output ".\output" --dry-run
```

Recursive batch:

```bat
run_2ico.bat --batch --input ".\samples" --output ".\output" --recursive
```

Custom ICO sizes:

```bat
run_2ico.bat --input ".\icon.png" --output ".\output" --sizes 16,32,48,256
```

Overwrite existing outputs:

```bat
run_2ico.bat --batch --input ".\samples" --output ".\output" --overwrite
```

Skip existing outputs:

```bat
run_2ico.bat --batch --input ".\samples" --output ".\output" --skip-existing
```

By default, existing target names are kept safe by writing a numbered name such
as `icon-1.ico`.
