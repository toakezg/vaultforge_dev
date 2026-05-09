# Business Compatibility Pass

Date: 2026-04-12

## Goal

Evaluate whether `vaultforge-business` can retarget to `vaultforge-engine`, then land the smallest safe retarget if parity holds.

The tiny retarget landed on 2026-04-12.

## Current Business Flow

Primary wrapper:

```text
vaultforge-business\run_business.ps1
```

Current behavior:

- Builds a business-specific prompt from client, asset type, business preset, style, modifiers, tags, tweak/reference fields, and the user prompt.
- Creates a business run folder before generation.
- Writes `prompt.txt`, `run.json`, and `gallery-entry.json` even in dry-run mode.
- Maps business preset/style names to current generator preset/style names.
- Pushes into `E:\tools\vaultforge\vaultforge-engine`.
- Calls `py .\src\generate.py` directly.
- Passes an absolute `--output-dir` pointing back into `vaultforge-business\generated\...`.

Important finding:

Business does not call `vaultforge-art\run_art.bat`, so the art compatibility bridge is not part of the business path. Business now targets the shared engine directly.

## Business-Owned Behavior

These pieces should stay in `vaultforge-business` for now:

- client/job/tag folder routing
- business preset/style/mod mapping
- prompt injection of business fields
- `run.json` and `gallery-entry.json`
- variant filename naming
- pack runners such as `run-client-pack.ps1`

## Dry-Run Checks

### Business Smoke

Command:

```powershell
.\run_business_smoke.bat
```

Observed:

```text
Output dir: E:\tools\vaultforge\vaultforge-business\generated\smoke-test\logo\business-logo\clean-corporate\2026-04-12\job-smoke
Prompt included business fields, transparent-safe instruction, user prompt, vaultforge preset fragment, and geometric style fragment.
Output filename base: smoke-test__logo__business-logo__clean-corporate__local-trustworthy-clear__v01
```

Business metadata written:

```text
generated\smoke-test\logo\business-logo\clean-corporate\2026-04-12\job-smoke\prompt.txt
generated\smoke-test\logo\business-logo\clean-corporate\2026-04-12\job-smoke\run.json
generated\smoke-test\logo\business-logo\clean-corporate\2026-04-12\job-smoke\gallery-entry.json
```

### Direct Engine Equivalent

Command shape:

```powershell
$prompt = Get-Content -LiteralPath 'E:\tools\vaultforge\vaultforge-business\generated\smoke-test\logo\business-logo\clean-corporate\2026-04-12\job-smoke\prompt.txt' -Raw
py .\src\generate.py $prompt --preset vaultforge --style geometric --size 1024x1024 --quality medium --format png --background transparent --output-dir 'E:\tools\vaultforge\vaultforge-business\generated\smoke-test\logo\business-logo\clean-corporate\2026-04-12\job-smoke' --filename 'smoke-test__logo__business-logo__clean-corporate__local-trustworthy-clear__v01' --dry-run
```

Observed:

```text
Output dir matched the business run folder.
Prompt composition matched the business dry-run output.
Preset/style resolution matched: business-logo -> vaultforge, clean-corporate -> geometric.
Filename base matched; only timestamp differed as expected.
```

### Multi-Variant Business Dry-Run

Command:

```powershell
powershell -ExecutionPolicy Bypass -File '.\run_business.ps1' 'Premium logo for Test Plumbing Co' -Client 'test-plumbing' -AssetType 'logo' -Job 'parity' -Tag 'plumber, local' -Preset 'business-icon' -Style 'luxury-minimal' -Mod 'premium' -Variants 2 -DryRun
```

Observed:

```text
Variant 01 filename base: test-plumbing__logo__business-icon__luxury-minimal__plumber-local__v01
Variant 02 filename base: test-plumbing__logo__business-icon__luxury-minimal__plumber-local__v02
Preset/style resolution matched: business-icon -> icon, luxury-minimal -> fine-line.
Output dir remained under vaultforge-business\generated.
```

### Direct Engine Multi-Variant Equivalent

Command shape:

```powershell
$prompt = Get-Content -LiteralPath 'E:\tools\vaultforge\vaultforge-business\generated\test-plumbing\logo\business-icon\luxury-minimal\2026-04-12\job-parity\prompt.txt' -Raw
py .\src\generate.py $prompt --preset icon --style fine-line --size 1024x1024 --quality medium --format png --background auto --output-dir 'E:\tools\vaultforge\vaultforge-business\generated\test-plumbing\logo\business-icon\luxury-minimal\2026-04-12\job-parity' --filename 'test-plumbing__logo__business-icon__luxury-minimal__plumber-local__v01' --dry-run
```

Observed:

```text
Output dir matched.
Prompt composition matched.
Preset/style resolution matched.
Filename base matched; only timestamp differed as expected.
```

### Pack Runner Dry Check

Command:

```powershell
powershell -ExecutionPolicy Bypass -File '.\run-client-pack.ps1' -InputValue 'Parity Studio' -Client 'parity-studio' -Project 'pack-dry' -Tag 'local, premium' -PromptFile '.\logo-pack.txt' -Tweak 'keep it simple' -WhatIf
```

Observed:

```text
The pack runner expands five run_business.ps1 commands.
It does not directly call the generator.
Retargeting run_business.ps1 is enough to cover the current pack runner.
```

## Config Handling

`vaultforge-business\business_defaults.conf` and `vaultforge-business\business_smoke.conf` exist, but the current business wrappers do not consume them through `@file.conf`.

So config parity is not currently a business-runtime blocker. It should be handled later if business gets a direct engine config mode.

Safety note: do not run config files live just to test them unless they explicitly include `--dry-run`.

## `run_engine.bat` Check

A direct `run_engine.bat` equivalent was attempted with the multiline business prompt.

Command shape:

```powershell
$prompt = Get-Content -LiteralPath '...\prompt.txt' -Raw
.\run_engine.bat $prompt --preset icon --style fine-line ... --dry-run
```

Observed:

```text
The syntax of the command is incorrect.
```

This is a quoting/multiline prompt risk from adding a batch-wrapper layer.

## Recommendation

Business should call:

```text
E:\tools\vaultforge\vaultforge-engine\src\generate.py
```

directly with `py`, instead of calling `vaultforge-engine\run_engine.bat`.

Reason:

- least wrapper nesting
- fewer quoting issues
- business already constructs an argument array cleanly in PowerShell
- business already passes an absolute output dir, so it does not need the project-root override
- direct engine parity was proven for smoke and multi-variant dry-runs

## Parity Result

Business parity passed for comparable dry-run generator behavior, and the tiny retarget was applied:

- prompt composition matched
- preset/style mapping matched
- variant filename bases matched
- output root behavior matched because business passes absolute output dirs
- pack runner remains covered through `run_business.ps1`

Current caveats after retarget:

- business dry-run still writes metadata files before generation
- business config files are present but not wired into runtime
- `run_business.ps1` now uses `EngineRoot` as the primary parameter name and keeps `ArtRoot` as a backward-compatible alias

## Step 7 Engine-Native Flag Update

Date: 2026-04-13

The dedicated engine thread added the low-risk native handoff flags:

- `--client`
- `--job`
- `--tag`
- `--variants`

Engine behavior:

- `--client`, `--job`, and `--tag` are raw context metadata fields with matching slug fields.
- Context slugs join the default filename base when no explicit `--filename` is supplied.
- `--variants N` generates or previews N output paths with `__v01`, `__v02`, and later suffixes.
- When any context field is supplied or variants exceed 1, live runs write sidecar JSON metadata beside each generated image.
- Dry-runs preview the image and metadata paths without writing sidecar metadata.
- These flags do not inject client/job/tag text into the prompt. Business wrappers still own business prompt composition and business folder routing.

## Remaining Blockers

- Decide whether business wrappers should eventually pass native engine `--client`, `--job`, `--tag`, and `--variants` directly, or keep their current wrapper-owned metadata files.
- Decide whether business config files should become real runtime entrypoints or remain documentation-only.
- Business wrappers can now choose when to pass native engine `--input-image` and `--reference-image`; wrapper-level tweak wording still belongs in business prompt composition.
