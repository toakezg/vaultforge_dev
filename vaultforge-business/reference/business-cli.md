# VaultForge Business CLI Reference

This is the operator reference for the current VaultForge Business command-line surface. It is written in a `yt-dlp`-style shape: command synopsis first, then option details, examples, output behavior, and known future placeholders.

The current business CLI is mostly PowerShell scripts with small `.bat` launchers. The business scripts live in this folder and target the sibling shared engine at `..\vaultforge-engine` by default.

## Quick Command Map

| Command | Purpose | Primary script |
| --- | --- | --- |
| `run_business.bat` | Run one prompt through the business wrapper. | `run_business.ps1` |
| `run_business_smoke.bat` | Run the built-in smoke prompt in business dry-run mode. | `run_business.ps1` |
| `run-client-pack.bat` | Run a text or JSON command pack with placeholders. | `run-client-pack.ps1` |
| `run_business_bank.bat` | Shortcut for the starter logo pack. | `run-client-pack.bat` |
| `run_business_md_bank.bat` | Run markdown prompt-bank notes. | `run_business_md_bank.ps1` |
| `build-review-summary.bat` | Build a Markdown review summary from generated manifests. | `build-review-summary.ps1` |
| `build-contact-sheets.bat` | Build `contact-sheet.jpg` files beside generated runs. | `build-contact-sheets.ps1` |
| `build-gallery.bat` | Build the local HTML review gallery. | `build-gallery.ps1` |
| `update-prompt-note.bat` | Write review status fields back into prompt-bank frontmatter. | `update-prompt-note.ps1` |
| `run_loop_10.bat` | Run one selected markdown note ten times. | `run_business_md_bank.ps1` |
| `run_loop_forever.bat` | Repeatedly run one selected markdown note until stopped. | `run_business_md_bank.ps1` |
| `setup_venv.bat` | Create or reuse a local Python virtual environment. | Windows batch |
| `open_business_venv_terminal.bat` | Open a terminal at the business lane root. | Windows batch |

## Safety Modes

| Mode | Where | Behavior |
| --- | --- | --- |
| `-WhatIf` | Business wrapper, pack runner, markdown-bank runner, prompt-note updater | Preview command or edit intent. For generation commands, no engine call is made. |
| `-DryRun` | Business wrapper and markdown-bank runner | Calls the shared engine with `--dry-run`. By default, business metadata/workspace files are not kept. |
| `-WriteMetadata` | Business wrapper and markdown-bank runner | With `-DryRun`, keeps business fixture files such as `prompt.txt`, `run.json`, and `gallery-entry.json`. |
| `-LogWhatIf` | Pack runner only | Allows `-WhatIf` preview rows to be appended to `logs\run-log.csv`. |
| `-StopOnError` | Pack runner and markdown-bank runner | Stops the batch when a child command fails. |

Important distinction: `-WhatIf` is no-execution preview. `-DryRun` still exercises the wrapper and shared engine dry-run path.

## Single Prompt Runner

### Synopsis

```powershell
powershell -ExecutionPolicy Bypass -File .\run_business.ps1 PROMPT [OPTIONS]
```

```bat
run_business.bat "PROMPT" [CLIENT] [ASSET_TYPE] [JOB] [TAG]
```

### Description

`run_business.ps1` is the main business wrapper. It composes a business-aware prompt, maps business-facing preset/style/mod names to the shared engine where supported, writes business manifests, and calls `..\vaultforge-engine\src\generate.py`.

The `.bat` launcher exposes the common positional fields only. Use the PowerShell script directly for advanced options.

### Positional Argument

| Argument | Required | Default | Meaning |
| --- | --- | --- | --- |
| `Prompt` | Yes | none | The natural-language asset request. |

### Business Naming Options

| Option | Default | Meaning |
| --- | --- | --- |
| `-Client TEXT` | `unsorted` | Operator-facing client name. Also becomes `client_slug` for folders. |
| `-AssetType TEXT` | `brand` | Asset grouping, for example `logo`, `icon`, `cover`, `brand-board`, `profile-picture`. |
| `-Job TEXT` | `manual` | Job/run name. Used in output folder `job-{job_slug}`. |
| `-Tag TEXT` | empty | Short context string, commonly comma-separated, for example `local,premium,round1`. |
| `-OutputRoot PATH` | `.\generated` | Business output root. |
| `-SourcePromptFile PATH` | empty | Source markdown note to copy into the run folder as `prompt.source.md`. |

### Business Prompt Options

| Option | Default | Meaning |
| --- | --- | --- |
| `-Preset TEXT` | `business-logo` | Business preset name. |
| `-Style TEXT[,TEXT...]` | `clean-corporate` | Business style list. Can be passed more than once or comma-separated. |
| `-Mod TEXT[,TEXT...]` | empty | Business modifier list. Can be passed more than once or comma-separated. |
| `-TransparentSafe` | off | Adds transparent-background-friendly prompt text, forces `-Background transparent`, and passes `transparent-bg-ready` to the engine constraints. |
| `-Tweak TEXT` | empty | Business-owned refinement context appended to the prompt. This is not yet a native shared edit loop. |
| `-InputImage PATH` | empty | Local image path passed to the shared engine and recorded in metadata. |
| `-ReferenceImage PATH` | empty | Local reference image path passed to the shared engine and recorded in metadata. |

### Generation Options

| Option | Default | Allowed values | Meaning |
| --- | --- | --- | --- |
| `-Variants N` | `1` | integer `>= 1` | Number of images to ask the engine for. |
| `-Size TEXT` | `1024x1024` | engine-supported size | Image size forwarded to the shared engine. |
| `-Quality TEXT` | `medium` | `low`, `medium`, `high` | Image quality forwarded to the shared engine. |
| `-Format TEXT` | `png` | `jpeg`, `png`, `webp` | Output format forwarded to the shared engine. |
| `-Background TEXT` | `auto` | `auto`, `transparent`, `opaque` | Background handling forwarded to the shared engine. |
| `-EngineRoot PATH` | `..\vaultforge-engine` | path | Shared engine root. Alias: `-ArtRoot`. |
| `-DryRun` | off | switch | Calls the shared engine with `--dry-run`. |
| `-WriteMetadata` | off | switch | Keeps business metadata during dry runs. |
| `-WhatIf` | off | switch | Prints the engine command and writes no files. |

### Current Preset Mapping

| Business preset | Engine preset |
| --- | --- |
| `business-icon` | `business-icon` |
| `business-cover` | `business-cover` |
| `social-brand-tile` | `social-brand-tile` |
| `brand-board` | `brand-board` |
| anything else, including `business-logo` | `vaultforge` |

### Current Style Mapping

| Business style | Engine style |
| --- | --- |
| `clean-corporate` | `clean-corporate` |
| `luxury-minimal` | `fine-line` |
| `modern-startup` | `modern-startup` |
| `bold-retro-brand` | `pixel` |
| `friendly-flat` | `geometric` |
| `premium-3d` | `photoreal` |
| `mono-mark` | `fine-line` |
| `vector-crisp` | `vector-crisp` |
| `editorial-brand` | `editorial-brand` |
| `neon-signage` | `cinematic` |
| anything else | `geometric` |

### Current Native Constraint Pass-Through

Only these business mods are passed to the shared engine as native `--constraint` values:

- `high-contrast`
- `print-safe`
- `small-size-readable`
- `transparent-bg-ready`

Other mods remain business prompt context only.

### Examples

Preview without running the engine:

```powershell
powershell -ExecutionPolicy Bypass -File .\run_business.ps1 "Premium logo for Empower You Plan Management" -Client "empower-you" -AssetType "logo" -Job "pack-01" -Tag "ndis,premium,local" -WhatIf
```

Dry-run the shared engine without keeping business files:

```powershell
powershell -ExecutionPolicy Bypass -File .\run_business.ps1 "Clean app icon for Gallable" -Client "gallable" -AssetType "icon" -Job "app-icon-01" -Preset "business-icon" -Style "friendly-flat" -Mod "small-size-readable" -DryRun
```

Dry-run and keep metadata fixtures:

```powershell
powershell -ExecutionPolicy Bypass -File .\run_business.ps1 "Clean app icon for Gallable" -Client "gallable" -AssetType "icon" -Job "app-icon-01" -Preset "business-icon" -Style "friendly-flat" -DryRun -WriteMetadata
```

Run with image/reference context:

```powershell
powershell -ExecutionPolicy Bypass -File .\run_business.ps1 "Refine this profile icon direction for a warmer local brand feel" -Client "toakezg" -AssetType "profile-picture" -Job "profile-img-refine" -Preset "business-icon" -Style "friendly-flat" -InputImage ".\path\input.png" -ReferenceImage ".\path\reference.png" -Tweak "keep the mark simple and readable"
```

### Output

Runs are routed to:

```text
generated\{client_slug}\{asset_slug}\{business_preset_slug}\{primary_style_slug}\{date}\job-{job_slug}\
```

Expected files per live run:

- `prompt.txt`
- `run.json`
- `gallery-entry.json`
- generated image files
- engine image sidecar `.json` files when the shared engine writes them
- `prompt.source.md` when `-SourcePromptFile` is supplied and exists

## Smoke Runner

### Synopsis

```bat
run_business_smoke.bat
```

### Description

Runs a fixed smoke prompt through `run_business.ps1` with `-DryRun`. It uses:

- client: `smoke-test`
- asset type: `logo`
- job: `smoke`
- tag: `local, trustworthy, clear`
- preset: `business-logo`
- style: `clean-corporate`
- mod: `small-size-readable`
- `-TransparentSafe`

Use this to check wrapper-to-engine wiring without making business output files.

## Text And JSON Pack Runner

### Synopsis

```powershell
powershell -ExecutionPolicy Bypass -File .\run-client-pack.ps1 -InputValue TEXT -Client TEXT -Project TEXT -Tag TEXT [OPTIONS]
```

```bat
run-client-pack.bat "INPUT" "CLIENT" "PROJECT" "TAG" ["PROMPTFILE"] ["TWEAK"]
```

### Description

`run-client-pack.ps1` executes command packs. Packs can be plain text command lines or structured JSON. It expands placeholders, runs each command, and logs results to `logs\run-log.csv`.

The pack runner is a command dispatcher. It does not generate images directly unless the pack commands call `run_business.ps1` or another generation command.

### Required Options

| Option | Meaning |
| --- | --- |
| `-InputValue TEXT` | Value used for `{INPUT}` placeholder expansion. |
| `-Client TEXT` | Value used for `{CLIENT}` and run logging. |
| `-Project TEXT` | Value used for `{PROJECT}` and run logging. Often maps to business wrapper `-Job`. |
| `-Tag TEXT` | Value used for `{TAG}` and run logging. |

### Optional Options

| Option | Default | Meaning |
| --- | --- | --- |
| `-PromptFile PATH` | `.\logo-pack.txt` | Pack file to execute. Supports `.txt` and `.json`. |
| `-Tweak TEXT` | empty | Value used for `{TWEAK}` placeholder expansion. |
| `-StopOnError` | off | Exit when a command fails. |
| `-PauseBetween` | off | Wait for Enter between commands. |
| `-DelaySeconds N` | `0` | Sleep between commands. |
| `-WhatIf` | off | Print planned commands and do not execute them. |
| `-LogWhatIf` | off | Log preview rows while in `-WhatIf` mode. |

### Placeholder Tokens

| Token | Source |
| --- | --- |
| `{INPUT}` | `-InputValue` |
| `{CLIENT}` | `-Client` |
| `{PROJECT}` | `-Project` |
| `{TAG}` | `-Tag` |
| `{TWEAK}` | `-Tweak` |

### Pack Formats

Plain text packs:

- One command per non-empty line.
- Lines starting with `#` are ignored.
- Placeholders are expanded before parsing/execution.

Structured JSON packs:

```json
{
  "commands": [
    {
      "command": ".\\run_business.ps1",
      "args": [
        "{INPUT}",
        "-Client",
        "{CLIENT}",
        "-Job",
        "{PROJECT}"
      ]
    }
  ]
}
```

`args` and `arguments` are both accepted. Structured packs are safer for quoting-heavy command lines.

### Examples

Preview the logo pack without touching the run log:

```powershell
powershell -ExecutionPolicy Bypass -File .\run-client-pack.ps1 -InputValue "Empower You Plan Management" -Client "empower-you" -Project "logo-pack-01" -Tag "round1" -PromptFile ".\logo-pack.txt" -WhatIf
```

Preview and log preview rows:

```powershell
powershell -ExecutionPolicy Bypass -File .\run-client-pack.ps1 -InputValue "Empower You Plan Management" -Client "empower-you" -Project "logo-pack-01" -Tag "round1" -PromptFile ".\logo-pack.txt" -WhatIf -LogWhatIf
```

Run a JSON pack and stop on first failure:

```powershell
powershell -ExecutionPolicy Bypass -File .\run-client-pack.ps1 -InputValue "Client Name" -Client "client-name" -Project "starter-pack-01" -Tag "round1" -PromptFile ".\pack-dryrun-safe.json" -StopOnError
```

## Starter Pack Shortcut

### Synopsis

```bat
run_business_bank.bat "INPUT" "CLIENT" "PROJECT" "TAG" ["TWEAK"]
```

### Description

Shortcut wrapper around `run-client-pack.bat` that always uses `logo-pack.txt` as the prompt file.

## Markdown Prompt-Bank Runner

### Synopsis

```powershell
powershell -ExecutionPolicy Bypass -File .\run_business_md_bank.ps1 [OPTIONS]
```

```bat
run_business_md_bank.bat [OPTIONS]
```

### Description

Runs markdown prompt-bank notes from `my-prompts-bank`. It parses simple YAML frontmatter, skips non-prompt notes, removes the opening H1 from the prompt body, and calls `run_business.ps1`.

### Options

| Option | Default | Meaning |
| --- | --- | --- |
| `-Path PATH` | `.\my-prompts-bank` | Folder or file to scan. |
| `-OutputRoot PATH` | `.\generated` | Business output root passed to `run_business.ps1`. |
| `-EngineRoot PATH` | `..\vaultforge-engine` | Shared engine root passed to `run_business.ps1`. |
| `-Status TEXT` | `draft` | Only run notes with matching `status`, unless `-All` is set. |
| `-Limit N` | `0` | Limit number of files considered after sorting. `0` means no limit. |
| `-VariantsOverride N` | `0` | Override note frontmatter `variants` when greater than zero. |
| `-All` | off | Ignore status filtering. |
| `-IncludeTemplates` | off | Include `_template` folders. By default templates are skipped. |
| `-DryRun` | off | Pass `-DryRun` to `run_business.ps1`. |
| `-WriteMetadata` | off | Pass `-WriteMetadata` to `run_business.ps1`. |
| `-WhatIf` | off | Print planned `run_business.ps1` commands without running them. |
| `-StopOnError` | off | Stop after the first failed prompt. |

### Recognized Frontmatter

| Frontmatter key | Maps to |
| --- | --- |
| `client` | `run_business.ps1 -Client` |
| `asset_type` or `asset` | `-AssetType` |
| `job` or `project` | `-Job` |
| `preset` or `business_preset` | `-Preset` |
| `styles` | `-Style` |
| `mods` | `-Mod` |
| `tags` or `tag` | `-Tag` |
| `size` | `-Size` |
| `quality` | `-Quality` |
| `format` | `-Format` |
| `background` | `-Background` |
| `variants` | `-Variants` |
| `tweak` | `-Tweak` |
| `input_image` | `-InputImage` |
| `reference_image` | `-ReferenceImage` |
| `transparent_safe` | `-TransparentSafe` when truthy |
| `status` | status filter |

Truthy values for `transparent_safe` are `1`, `true`, `yes`, `y`, and `on`.

### Examples

Preview one note, including templates:

```bat
run_business_md_bank.bat -Path ".\my-prompts-bank" -IncludeTemplates -WhatIf -Limit 1
```

Preview all runnable notes with three variants:

```bat
run_business_md_bank.bat -Path ".\my-prompts-bank" -All -WhatIf -VariantsOverride 3
```

Dry-run draft notes:

```bat
run_business_md_bank.bat -Path ".\my-prompts-bank" -DryRun
```

Dry-run and keep metadata fixtures:

```bat
run_business_md_bank.bat -Path ".\my-prompts-bank" -DryRun -WriteMetadata
```

Run one specific note:

```bat
run_business_md_bank.bat -Path ".\my-prompts-bank\Gallable\gallable-app-icon.md"
```

## Review Summary Builder

### Synopsis

```powershell
powershell -ExecutionPolicy Bypass -File .\build-review-summary.ps1 [OPTIONS]
```

```bat
build-review-summary.bat [OPTIONS]
```

### Description

Scans generated output for `gallery-entry.json` files and writes a Markdown table for review. It does not generate images.

### Options

| Option | Default | Meaning |
| --- | --- | --- |
| `-GeneratedRoot PATH` | `.\generated` | Root to scan. |
| `-OutFile PATH` | empty | Output Markdown path. If empty, the script prints the summary to the console. |
| `-Limit N` | `0` | Limit rows. `0` means no limit. |

### Example

```bat
build-review-summary.bat -OutFile ".\generated\_review\business-summary.md"
```

## Contact Sheet Builder

### Synopsis

```powershell
powershell -ExecutionPolicy Bypass -File .\build-contact-sheets.ps1 [OPTIONS]
```

```bat
build-contact-sheets.bat [OPTIONS]
```

### Description

Scans generated runs and writes `contact-sheet.jpg` beside generated images. It uses `gallery-entry.json` as the run manifest.

### Options

| Option | Default | Meaning |
| --- | --- | --- |
| `-GeneratedRoot PATH` | `.\generated` | Root to scan. |
| `-OutName TEXT` | `contact-sheet.jpg` | Filename written in each run folder. |
| `-Columns N` | `0` | Requested sheet columns. `0` auto-sizes. |
| `-ThumbnailSize N` | `220` | Thumbnail size in pixels. |
| `-Padding N` | `18` | Sheet padding in pixels. |
| `-LabelHeight N` | `34` | Label area height in pixels. |
| `-Limit N` | `0` | Limit processed runs. |
| `-Force` | off | Overwrite existing contact sheets. |

### Example

```bat
build-contact-sheets.bat -GeneratedRoot ".\generated" -Force
```

## HTML Gallery Builder

### Synopsis

```powershell
powershell -ExecutionPolicy Bypass -File .\build-gallery.ps1 [OPTIONS]
```

```bat
build-gallery.bat [OPTIONS]
```

### Description

Builds an HTML gallery from `gallery-entry.json` files and generated images. Contact sheets are preferred as preview images when present.

### Options

| Option | Default | Meaning |
| --- | --- | --- |
| `-GeneratedRoot PATH` | `.\generated` | Root to scan. |
| `-OutFile PATH` | `generated\_gallery\index.html` | HTML output path. |
| `-Limit N` | `0` | Limit rows. |

### Example

```bat
build-gallery.bat -GeneratedRoot ".\generated"
```

## Prompt Note Updater

### Synopsis

```powershell
powershell -ExecutionPolicy Bypass -File .\update-prompt-note.ps1 [OPTIONS]
```

```bat
update-prompt-note.bat [OPTIONS]
```

### Description

Updates YAML frontmatter fields in a markdown prompt note after review. It can find the prompt note from a generated run folder if `run.json` includes `source_prompt_file`.

### Options

| Option | Default | Meaning |
| --- | --- | --- |
| `-PromptPath PATH` | empty | Prompt note to update. |
| `-RunDir PATH` | empty | Generated run folder. Used to discover `source_prompt_file` and first image. |
| `-Status TEXT` | `generated` | Value written to `status`. |
| `-Image PATH` | empty | Value written to `image`. If omitted with `-RunDir`, the first generated image is used. |
| `-Rating TEXT` | empty | Value written to `rating`. |
| `-Notes TEXT` | empty | Value written to `notes`. |
| `-WhatIf` | off | Preview the intended update without writing the note. |

### Examples

Update a known prompt note:

```bat
update-prompt-note.bat -PromptPath ".\my-prompts-bank\example-client\logo-01.md" -Status review -Rating 8 -Notes "strong option"
```

Update from a run folder:

```bat
update-prompt-note.bat -RunDir ".\generated\client\asset\preset\style\date\job-name" -Status generated
```

Preview a note update:

```bat
update-prompt-note.bat -PromptPath ".\my-prompts-bank\example-client\logo-01.md" -Status selected -Rating 9 -WhatIf
```

## Loop Helpers

### `run_loop_10.bat`

Runs:

```powershell
powershell -ExecutionPolicy Bypass -File .\run_business_md_bank.ps1 -Path ".\my-prompts-bank\Gallable\gallable-app-icon.md"
```

ten times, then pauses.

### `run_loop_forever.bat`

Runs:

```powershell
powershell -ExecutionPolicy Bypass -File "%~dp0run_business_md_bank.ps1" -Path "%~dp0my-prompts-bank\vaultforge\cover-01.md"
```

in a two-second loop until the terminal is stopped.

These helpers are narrow local automation shortcuts, not general-purpose client commands.

## Environment Helpers

### `setup_venv.bat`

Creates or reuses `.venv`, upgrades `pip`, then installs from `requirements.txt` when present or `pyproject.toml` editable mode otherwise.

### `open_business_venv_terminal.bat`

Opens a `cmd` terminal in the business lane root and prints the expected shared engine location.

## Current Shared Engine Boundary

The business wrapper currently forwards these engine-native fields:

- prompt text
- `--preset`
- `--style`
- `--size`
- `--quality`
- `--format`
- `--background`
- `--output-dir`
- `--filename`
- `--client`
- `--job`
- `--tag`
- `--variants`
- `--constraint`
- `--input-image`
- `--reference-image`
- `--dry-run`

The business wrapper owns these higher-level behaviors:

- business output folder shape
- business prompt composition
- business preset/style alias mapping
- business modifier filtering
- `prompt.txt`
- `run.json`
- `gallery-entry.json`
- `prompt.source.md`
- markdown prompt-bank parsing
- review summary/contact sheet/gallery helpers
- prompt-note review closure fields

## Current Output And Log Files

| File or folder | Written by | Purpose |
| --- | --- | --- |
| `generated\...` | `run_business.ps1` and shared engine | Business run folders and generated assets. |
| `prompt.txt` | `run_business.ps1` | Composed business prompt sent to the engine. |
| `run.json` | `run_business.ps1` | Detailed business run manifest. |
| `gallery-entry.json` | `run_business.ps1` | Lightweight browse/review manifest. |
| `prompt.source.md` | `run_business.ps1` | Source markdown note copy when provided. |
| `logs\run-log.csv` | `run-client-pack.ps1` | Pack execution log. |
| `contact-sheet.jpg` | `build-contact-sheets.ps1` | Per-run visual review sheet. |
| `generated\_gallery\index.html` | `build-gallery.ps1` | Local HTML gallery. |
| `generated\_review\business-summary.md` | common `build-review-summary.ps1` output | Markdown review table. |

## Future Directions

Everything in this section is a placeholder or future direction, not current CLI behavior.

### Placeholder: Native Business Help Command

Potential command:

```bat
business-cli help
```

Would print this reference in a compact terminal form and point to `reference\business-cli.md`.

### Placeholder: Unified Business Command

Potential command:

```bat
business-cli run --prompt "..." --client "..." --asset logo
```

Would wrap `run_business.ps1`, markdown-bank execution, review summary building, and packaging helpers under one command namespace.

### Placeholder: Review Closure Command

Potential command:

```bat
business-cli review close --run-dir "..." --status selected --rating 9
```

Would combine generated-run inspection with `update-prompt-note.ps1` and possibly refresh summary/gallery outputs.

### Placeholder: Delivery Package Command

Potential command:

```bat
business-cli package --run-dir "..." --client "..." --job "..."
```

Would copy selected outputs into a delivery package skeleton after the review checklist is satisfied.

### Placeholder: Client Intake To Prompt Notes

Potential command:

```bat
business-cli intake --brief ".\my-prompts-bank\_intake\client-intake-template.md"
```

Would convert a completed intake note into one or more runnable prompt-bank notes.

### Placeholder: Native Refinement/Edit Loop

Potential command:

```bat
business-cli refine --run-dir "..." --tweak "make the icon warmer"
```

The current wrapper records `-Tweak`, `-InputImage`, and `-ReferenceImage`, and passes image paths through to the shared engine. A full refinement/edit loop still needs a shared engine contract before the business CLI should claim it as a complete workflow.

## Notes For Operators

- Prefer `-WhatIf` before running broad packs.
- For markdown-bank tests, start with a single note path or `-Limit 1`.
- Use `-DryRun` when you want to exercise the engine dry-run path.
- Add `-WriteMetadata` only when you intentionally want dry-run fixtures kept.
- Keep generated review decisions flowing back to prompt notes with `update-prompt-note.bat`; otherwise review surfaces can drift from the prompt bank.
