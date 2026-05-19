# VaultForge Icon CLI Reference

Status checked from `F:\vaultforge\vaultforge-icon` on 2026-05-13.

This is a practical CLI reference for the icon lane, written in a `yt-dlp`-style
shape: command first, then options, examples, output behavior, and safety notes.

The repo currently has three real command surfaces:

- `svg-forge\run_svg_forge.bat` / `svg_forge.py` - raster images to SVG.
- `2ico\run_2ico.bat` / `image_to_ico.py` - raster images to Windows `.ico`.
- `run_icon_proposal.ps1` - proposal image generation through the VaultForge
  engine.

Future command ideas such as `$make-icon` and `$apply-icon` are documented near
the end and marked `NOT IN YET`.

## Current Verification Snapshot

| Command surface | Current state | Verification notes |
| --- | --- | --- |
| `svg-forge` | CLI help and preset listing work with global `py`; local `.venv` is not present in this checkout. | `py .\svg_forge.py --help` and `py .\svg_forge.py --list-presets` returned usable output. Real conversion still needs `vtracer` and `Pillow` installed in the interpreter used. |
| `2ico` | Script and wrappers exist, but not runnable in this checkout until setup is run. | `2ico\.venv` is missing and global `py .\image_to_ico.py --help` exits with `Pillow is required`. Run `setup_venv.bat` from `2ico`. |
| `run_icon_proposal.ps1` | Script exists and engine path exists, but current `.env` is missing. | `..\vaultforge-engine\src\generate.py` exists; `vaultforge-icon\.env` was not present during this check. The script requires `ICON_KEY`. |
| `$make-icon` | `NOT IN YET`. | Contract/interface docs only. No `make_icon.py` or `run_make_icon.bat`. |
| `$apply-icon` | `NOT IN YET`. | Contract docs only. No `apply_icon.py` or `run_apply_icon.bat`. |

## Global Conventions

Run commands from the tool folder unless the example says otherwise.

Paths should be quoted when they contain spaces:

```powershell
".\run_svg_forge.bat" --input "F:\media\icons\source png" --output "F:\media\icons\svg"
```

Use `--dry-run` when available before a batch write. Dry-run behavior differs by
tool:

- `svg-forge --dry-run` does not write folders, SVGs, or logs.
- `2ico --dry-run` does not write ICO files.
- `run_icon_proposal.ps1 -DryRun` still resolves input/output paths and creates
  the output directory before passing `--dry-run` to the engine.

## `svg-forge`

Raster-to-SVG converter for icons, logos, glyphs, and small visual assets.

### Command

From `F:\vaultforge\vaultforge-icon\svg-forge`:

```bat
run_svg_forge.bat [OPTIONS]
```

Direct Python form:

```powershell
py .\svg_forge.py [OPTIONS]
```

If `svg-forge\.venv\Scripts\python.exe` exists, `run_svg_forge.bat` uses it.
Otherwise it falls back to `py`.

### Basic Examples

Convert a folder using defaults:

```bat
run_svg_forge.bat --input ".\samples"
```

Convert a folder to a specific output folder:

```bat
run_svg_forge.bat --input ".\samples" --output ".\output" --preset icon-clean
```

Convert specific files:

```bat
run_svg_forge.bat --input ".\samples\a.png" ".\samples\b.webp" --output ".\output"
```

Scan folders recursively:

```bat
run_svg_forge.bat --input ".\samples" --recursive --output ".\output"
```

List presets:

```bat
run_svg_forge.bat --list-presets
```

No-write preview:

```bat
run_svg_forge.bat --input ".\samples" --preset icon-clean --dry-run
```

### Options

#### `--input INPUT [INPUT ...]`

Input file(s) or folder(s). Folders are scanned for supported raster files.

Supported input extensions:

- `.png`
- `.jpg`
- `.jpeg`
- `.webp`

Multiple inputs are accepted after one `--input` flag.

#### `--output OUTPUT`

Output folder. Defaults to the `default_output` value in
`svg_forge.config.json`, currently:

```json
"output"
```

Output filenames preserve source stems:

```text
quest-icon.png -> quest-icon.svg
```

When `--recursive` is used, relative subfolders are preserved under the output
folder.

#### `--preset PRESET`

Tracing preset. Defaults to the `default_preset` value in
`svg_forge.config.json`, currently `icon-clean`.

Available presets:

| Preset | Use |
| --- | --- |
| `icon-clean` | Balanced cleanup for small colour icons. |
| `logo-clean` | Clean logo marks and brand shapes. |
| `glyph-bw` | Black/white symbols, masks, and simple glyphs. |
| `flat-colour` | Reduced-palette flat colour icons. |
| `detailed-colour` | Richer, more detailed colour images. |

#### `--config CONFIG`

Path to the JSON config file. Default:

```text
svg-forge\svg_forge.config.json
```

Current config:

```json
{
  "default_preset": "icon-clean",
  "default_output": "output",
  "skip_existing": false,
  "recursive": false
}
```

CLI flags override config values.

#### `--dry-run`

Prints planned conversions without writing SVG files, output folders, or logs.

Expected dry-run summary shape:

```text
planned: <source> -> <destination>
Dry run complete. No folders, SVG files, or logs were written.
  planned: <count>
```

#### `--skip-existing`

Skips any output SVG that already exists. Without this flag, `svg-forge`
converts and writes to the target path.

#### `--recursive`

Scans input folders recursively and preserves relative subfolders under the
output directory.

#### `--log LOG`

Custom log path. Defaults to:

```text
<output>\svg-forge.log
```

Normal conversion runs append to the log. Dry-run mode does not write a log.

#### `--open-inkscape`

Alias:

```text
--open-after-convert
```

After conversion, opens converted SVG files in Inkscape when Inkscape is found.
The script checks `PATH` and common Windows install locations.

#### `--list-presets`

Lists the preset names and descriptions, then exits.

#### `-h`, `--help`

Prints help text and exits.

### Exit Behavior

- Returns `0` when all planned or actual conversions complete without failures.
- Returns `1` when no supported inputs are found or at least one conversion
  fails.
- Returns `2` for argument/config errors such as an unknown preset.

### Dependencies

Install from `svg-forge`:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

There is no `setup_venv.bat` in `svg-forge` yet.

## `2ico`

Raster-to-ICO converter for Windows icon files.

### Current Local Status

The command files exist, but this checkout currently needs setup before it is
actually runnable:

- `2ico\.venv\Scripts\python.exe` is missing.
- Global `py .\image_to_ico.py --help` fails because `Pillow` is missing.

Run setup from `F:\vaultforge\vaultforge-icon\2ico`:

```bat
setup_venv.bat
```

After setup, use:

```bat
run_2ico.bat [OPTIONS]
```

Direct Python form after setup:

```powershell
.\.venv\Scripts\python.exe .\image_to_ico.py [OPTIONS]
```

### Basic Examples

Single file to an output folder:

```bat
run_2ico.bat --input ".\samples\icon.png" --output ".\output"
```

Single file to a specific `.ico` path:

```bat
run_2ico.bat --input ".\samples\icon.png" --output ".\output\icon.ico"
```

Batch folder:

```bat
run_2ico.bat --batch --input ".\samples" --output ".\output"
```

Recursive batch:

```bat
run_2ico.bat --batch --input ".\samples" --output ".\output" --recursive
```

Custom icon sizes:

```bat
run_2ico.bat --input ".\icon.png" --output ".\output" --sizes 16,32,48,256
```

No-write preview:

```bat
run_2ico.bat --batch --input ".\samples" --output ".\output" --dry-run
```

List supported formats:

```bat
run_2ico.bat --list-formats
```

### Launchers

#### `setup_venv.bat`

Creates `2ico\.venv`, upgrades `pip`, and installs `requirements.txt`.

#### `run_2ico.bat`

Passes all terminal arguments through to `image_to_ico.py`.

#### `run_2ico_batch.bat`

Interactive wrapper. Prompts for:

- input image file or folder
- output ICO file or folder

Then runs:

```bat
image_to_ico.py --batch --input "<input>" --output "<output>"
```

#### `run_2ico_input.bat`

Interactive wrapper. Prompts for:

- input image file or folder
- output ICO file or folder
- optional ICO sizes

If sizes are blank, it uses:

```text
16,24,32,48,64,128,256
```

### Options

#### `--input INPUT`, `-i INPUT`

Image file or directory containing images.

Required unless `--list-formats` is used.

Supported input extensions:

- `.png`
- `.jpg`
- `.jpeg`
- `.webp`
- `.bmp`
- `.gif`
- `.tif`
- `.tiff`

#### `--output OUTPUT`, `-o OUTPUT`

Output `.ico` file or output directory.

Behavior:

- If input is a single file and output ends with `.ico`, that exact path is
  used.
- If input is a single file and output is a folder, the output filename is
  `<input-stem>.ico`.
- If input is a directory, outputs are written under the output directory.
- If omitted, outputs are written beside the input images with `.ico`
  extensions.

#### `--batch`

Treats input as batch-capable. Directories batch automatically even without this
flag, but the flag makes intent clear.

#### `--recursive`

When input is a directory, includes supported images in subdirectories and
mirrors relative folders under the output directory.

#### `--sizes SIZES`

Comma-separated icon sizes. Default:

```text
16,24,32,48,64,128,256
```

Accepted forms:

```text
16
32,48,256
32x32,48x48
```

Rules:

- Sizes must be square.
- Sizes must be between `1` and `256`.
- Duplicate sizes are removed while preserving order.

#### `--overwrite`

Overwrites existing `.ico` files.

#### `--skip-existing`

Skips outputs that already exist.

#### Default Existing-File Behavior

If a target exists and neither `--overwrite` nor `--skip-existing` is used,
`2ico` writes a numbered safe filename:

```text
icon.ico
icon-1.ico
icon-2.ico
```

#### `--dry-run`

Prints planned conversions without writing ICO files.

Expected dry-run summary shape:

```text
planned: <source> -> <destination>
Dry run complete. No ICO files were written.
summary: converted=<count> skipped=<count> failed=<count>
```

#### `--list-formats`

Prints supported input extensions and exits.

#### `-h`, `--help`

Prints help text and exits.

### Exit Behavior

- Returns `0` when conversions complete without failures.
- Returns `1` when no supported inputs are found or any conversion fails.
- Returns `2` for setup, dependency, argument, or runtime errors caught by the
  top-level command.

## `run_icon_proposal.ps1`

PowerShell runner for generated proposal images. It loads `ICON_KEY` from the
icon lane `.env`, maps it to the child engine environment variable, and calls
the VaultForge engine generator.

### Current Local Status

The script exists and the engine script exists at:

```text
..\vaultforge-engine\src\generate.py
```

This checkout currently does not have:

```text
vaultforge-icon\.env
```

So the runner will stop with a missing `.env` error until `ICON_KEY` is restored
locally.

### Command

From `F:\vaultforge\vaultforge-icon`:

```powershell
.\run_icon_proposal.ps1 [OPTIONS]
```

### Default Invocation

```powershell
.\run_icon_proposal.ps1
```

Default values:

| Parameter | Default |
| --- | --- |
| `-Batch` | `generated\proposals\first-inspired-run\prompts` |
| `-Output` | `generated\proposals\first-inspired-run\images` |
| `-Client` | `VaultForge Icon` |
| `-Job` | `first-inspired-run` |
| `-Tag` | `proposal,inspired-agent` |
| `-Quality` | `low` |

The child engine call uses these fixed values:

| Engine arg | Value |
| --- | --- |
| `--preset` | `icon` |
| `--style` | `geometric` |
| `--size` | `1024x1024` |
| `--format` | `png` |
| `--background` | `transparent` |

### Examples

Dry-run a custom prompt batch:

```powershell
.\run_icon_proposal.ps1 `
  -Batch "generated\proposals\my-run\prompts" `
  -Output "generated\proposals\my-run\images" `
  -Client "VaultForge Icon" `
  -Job "my-run" `
  -Tag "proposal,my-run" `
  -Quality "low" `
  -DryRun
```

Run a live proposal batch:

```powershell
.\run_icon_proposal.ps1 `
  -Batch "generated\proposals\my-run\prompts" `
  -Output "generated\proposals\my-run\images" `
  -Client "VaultForge Icon" `
  -Job "my-run" `
  -Tag "proposal,my-run" `
  -Quality "low"
```

### Parameters

#### `-Batch <path>`

Prompt batch folder, resolved relative to `vaultforge-icon`.

The path must already exist. The script calls `Resolve-Path` on it before
running the engine.

#### `-Output <path>`

Output image folder, relative to `vaultforge-icon` unless an absolute path is
provided.

The script creates this directory before invoking the engine.

#### `-Client <name>`

Client label passed to the engine as `--client`.

#### `-Job <name>`

Job label passed to the engine as `--job`.

Use a stable run id, usually matching the proposal folder name.

#### `-Tag <tag-list>`

Comma-separated tag string passed to the engine as `--tag`.

#### `-Quality <quality>`

Image quality passed through to the engine as `--quality`.

Current script default is:

```text
low
```

#### `-DryRun`

Adds `--dry-run` to the child engine command.

Important: the wrapper still checks `.env`, resolves the batch path, and creates
the output directory before the engine receives `--dry-run`.

### Secret Handling

The script reads:

```text
ICON_KEY=<secret>
```

from:

```text
vaultforge-icon\.env
```

It sets this child-process environment variable:

```text
IMAGE_GENERATION_KEY_B_OPENAI_API_KEY 
```

Do not print the key in logs or docs.

### Failure Cases

The script stops when:

- `.env` is missing.
- `ICON_KEY` is missing or blank.
- `-Batch` cannot be resolved.
- the engine script or Python launcher fails.

The script exits with the child `py` process exit code.

## Setup Commands

### `svg-forge` Environment Setup

```powershell
cd F:\vaultforge\vaultforge-icon\svg-forge
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

### `2ico` Environment Setup

```powershell
cd F:\vaultforge\vaultforge-icon\2ico
.\setup_venv.bat
```

### Proposal Runner Secret Setup

Create a local-only `.env` at:

```text
F:\vaultforge\vaultforge-icon\.env
```

Required key:

```text
ICON_KEY=<your key>
```

Do not commit or paste the key.

## Future Commands - NOT IN YET

Everything in this section is planned or contract-only. These are not currently
runnable commands in this repo.

## `$make-icon` - NOT IN YET

Planned workflow/tool label for turning a folder, lane, client, project, or task
purpose into reviewable icon concepts.

No current files exist for:

- `make_icon.py`
- `run_make_icon.bat`

### Proposed Shape

```text
$make-icon --target <path-or-name> --purpose <short-purpose> --use <intended-use> --no-write
```

### Proposed Future Options

#### `--target <path-or-name>` - NOT IN YET

Existing folder path or stable target name.

#### `--purpose <short-purpose>` - NOT IN YET

Short description of what the icon should represent.

#### `--use <intended-use>` - NOT IN YET

Intended use, such as:

- `folder-icon`
- `lane-identity`
- `subtool-identity`
- `client-concept`

#### `--no-write` - NOT IN YET

Required safety flag in the planned first version. The proposed first real
interface should refuse to continue without it.

#### `--style <style-note>` - NOT IN YET

Optional style constraints.

#### `--brief <existing-brief.md>` - NOT IN YET

Optional existing Markdown brief to review or reuse.

#### `--concept-count <1-3>` - NOT IN YET

Optional count for concept directions.

#### `--output-root <planned-output-folder>` - NOT IN YET

Optional planned output location for future preview paths.

#### `--format markdown` - NOT IN YET

Optional preview format. Current plan only discusses Markdown.

### Planned No-Write Output Shape - NOT IN YET

```text
MAKE ICON PREVIEW
target: vaultforge-icon/svg-forge
purpose: raster-to-SVG conversion subtool identity
intended_use: folder icon concept
mode: no-write

planned_outputs:
  markdown_brief: <output-root>/briefs/<safe-target-name>.md
  metadata: <output-root>/metadata/<safe-target-name>.json

blocked_actions:
  - no image generation
  - no API call
  - no asset move/delete
  - no folder icon application
```

### Explicitly Not Approved Yet

- image generation
- API calls
- paid calls
- secrets or cloud auth
- asset moves/deletion
- folder icon application
- creating `make_icon.py`
- creating `run_make_icon.bat`

## `$apply-icon` - NOT IN YET

Planned workflow/tool label for placing already-selected icons onto approved
target folders.

No current files exist for:

- `apply_icon.py`
- `run_apply_icon.bat`

### Proposed Future Shape

```text
$apply-icon --plan <apply-plan.md-or-json> --dry-run
```

This exact invocation is a proposed practical wrapper shape. The existing
contract defines the plan and transcript requirements, not a final runnable CLI.

### Proposed Future Options

#### `--plan <path>` - NOT IN YET

Path to a reviewed apply-plan.

#### `--dry-run` - NOT IN YET

Required first-mode safety flag. Planned dry-run output must show what would be
inspected or changed without applying folder icons.

#### `--target <path>` - NOT IN YET

Possible future shortcut for a single target. Not approved by the current
contract as a replacement for a plan.

#### `--icon-source <path>` - NOT IN YET

Possible future shortcut for the selected icon source. Not approved by the
current contract as a replacement for a plan.

#### `--approve-apply` - NOT IN YET

Possible future explicit live-apply gate. Not approved for implementation.

### Required Future Dry-Run Transcript Fields - NOT IN YET

Future dry-run output should show:

- source plan path
- plan status
- target count
- target paths
- icon source paths
- planned actions
- current no-write mode
- created files count
- moved/deleted assets count
- applied folder icons count
- blocked entries and blocker reasons

For the current contract, every dry-run preview must report:

```text
created_files: 0
moved_or_deleted_assets: 0
applied_folder_icons: 0
```

### Explicitly Not Approved Yet

- applying folder icons
- moving, deleting, renaming, or overwriting assets
- creating `apply_icon.py`
- creating `run_apply_icon.bat`
- creating generated apply-plan folders
- image generation
- API calls
- taste decisions between visual directions

## Possible Future Enhancements - NOT IN YET

These are useful candidates, but no command currently implements them.

### Common Flags

```text
--yes
--quiet
--verbose
--json
--log-file <path>
--report <path>
```

Potential use:

- `--yes` for explicit noninteractive confirmation after a dry-run contract
  exists.
- `--quiet` for script-friendly output.
- `--verbose` for full source/destination tracing.
- `--json` for machine-readable summaries.
- `--log-file` for deterministic logs.
- `--report` for Markdown run reports.

### Icon Set Runner

```text
$make-icon-set --targets <targets.md> --style <style-guide.txt> --output <run-folder> --dry-run
```

Potential use:

- read a scoped target list
- create one prompt per target
- run `run_icon_proposal.ps1` or a later approved engine wrapper
- write proposal images and metadata under `generated/proposals/<run-id>/`

Status: `NOT IN YET`. Current docs describe the workflow contract only.

### Scout-To-Proposal Runner

```text
$icon-scout --root <folder> --output generated/proposals/inbox/<name>.md --dry-run
```

Potential use:

- inspect a scoped folder
- summarize icon candidates
- write proposal-ready target descriptions

Status: `NOT IN YET`. Current docs describe checklist/contract behavior only.

## Quick Command Index

Currently real files:

```text
svg-forge\run_svg_forge.bat
svg-forge\svg_forge.py
2ico\setup_venv.bat
2ico\run_2ico.bat
2ico\run_2ico_batch.bat
2ico\run_2ico_input.bat
2ico\image_to_ico.py
run_icon_proposal.ps1
```

Currently parked / not present:

```text
make_icon.py
run_make_icon.bat
apply_icon.py
run_apply_icon.bat
```

