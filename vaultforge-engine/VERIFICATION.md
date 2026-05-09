# Verification

Date: 2026-04-12

## First Copy-Based Prototype

The first engine prototype was copied from:

```text
E:\tools\image_generation\vaultforge-art
```

The sibling source worktree was not modified.

## Checks Run

Unit tests:

```powershell
$env:PYTHONPATH=(Resolve-Path 'src').Path; py -m unittest discover -s tests
```

Result:

```text
Ran 7 tests
OK
```

Direct dry-run:

```powershell
py .\src\generate.py "A clean geometric VaultForge test icon" --preset icon --style geometric --dry-run
```

Result:

```text
Output dir: E:\tools\vaultforge\vaultforge-engine\assets\generated
```

Batch smoke dry-run:

```powershell
py .\src\generate.py --batch-smoke --preset icon --style geometric --dry-run
```

Result:

```text
Batch dry run complete: 1 prompt file(s) would run, 0 would skip.
```

Launcher dry-run:

```powershell
.\run_engine.bat "A launcher smoke test icon" --preset icon --style geometric --dry-run
```

Result:

```text
Output dir: E:\tools\vaultforge\vaultforge-engine\assets\generated
```

## Notes

- Dry-run checks do not require a live API key.
- The copied engine currently preserves the shared CLI behavior under `src\generate.py`.
- `PROJECT_ROOT` was adjusted so default engine paths resolve from `vaultforge-engine`, not `vaultforge-engine\src`.
- Business now targets the shared engine directly through `run_business.ps1`.

## Engine Step 7 Handoff

Date: 2026-04-13

Unit tests:

```powershell
$env:PYTHONPATH=(Resolve-Path 'src').Path; py -m unittest discover -s tests
```

Result:

```text
Ran 11 tests
OK
```

Native context and variants dry-run:

```powershell
py .\src\generate.py "A premium local service logo mark" --preset icon --style geometric --client "Empower You" --job "logo-pack-01" --tag "local, premium" --variants 2 --dry-run
```

Result:

```text
Context metadata: client=Empower You (empower-you), job=logo-pack-01 (logo-pack-01), tag=local, premium (local-premium)
Variants: 2
Output path v01: ...empower-you__job-logo-pack-01__local-premium__a-premium-local-service-logo-mark__v01.png
Output path v02: ...empower-you__job-logo-pack-01__local-premium__a-premium-local-service-logo-mark__v02.png
```

Batch smoke with native context and variants:

```powershell
py .\src\generate.py --batch-smoke --preset icon --style geometric --client "Smoke Client" --job "batch-smoke" --tag "engine" --variants 2 --dry-run
```

Result:

```text
Batch dry run complete: 1 prompt file(s) would run, 2 image request(s) would be made, 0 would skip.
```

## Workflow B Engine Build Slice

Date: 2026-05-09

Unit tests:

```powershell
$env:PYTHONPATH=(Resolve-Path 'src').Path; py -B -m unittest discover -s tests
```

Result:

```text
Ran 20 tests
OK
```

Committed config dry-run:

```powershell
py .\src\generate.py '@assets\batch-input-smoke\smoke.conf'
```

Expected coverage:

- `@file.conf` parsing
- `--batch-smoke` prompt routing
- explicit `--output-dir`
- native client/job/tag metadata preview
- two output variants
- local `--reference-image`
- metadata path preview without live API writes

Observed result:

```text
Batch dry run complete: 1 prompt file(s) would run, 2 image request(s) would be made, 0 would skip.
```

## Workflow B No-Write Preview Decision

Date: 2026-05-09

Help check:

```powershell
py .\src\generate.py --help
```

Unit tests:

```powershell
$env:PYTHONPATH=(Resolve-Path 'src').Path; py -B -m unittest discover -s tests
```

Result:

```text
Ran 20 tests
OK
```

Dry-run no-write check:

```powershell
py .\src\generate.py '@assets\batch-input-smoke\smoke.conf'
```

Observed result:

```text
Batch dry run complete: 1 prompt file(s) would run, 2 image request(s) would be made, 0 would skip.
```

No-write evidence:

- `assets\generated` was empty before and after the dry-run command.
- `assets\batch-input-smoke\.batch-state.json` did not exist before or after the dry-run command.
- The dry-run printed intended image and metadata paths but did not create PNG or JSON outputs.

Decision:

- Keep `--dry-run` as the current no-write preview path.
- Do not add a separate preview flag until a lane wrapper proves it needs behavior that differs from the engine dry-run contract.

## Workflow B Gallery Index Hook

Date: 2026-05-09

Help check:

```powershell
py .\src\generate.py --help
```

Unit tests:

```powershell
$env:PYTHONPATH=(Resolve-Path 'src').Path; py -B -m unittest discover -s tests
```

Result:

```text
Ran 23 tests
OK
```

Gallery index smoke:

```powershell
py .\src\generate.py --gallery-index --gallery-source assets\generated --gallery-output $env:TEMP\vaultforge-engine-gallery-index-smoke.json
```

Observed result:

```text
Gallery index written: C:\Users\natha\AppData\Local\Temp\vaultforge-engine-gallery-index-smoke.json
```

Existing no-write smoke still passes:

```powershell
py .\src\generate.py '@assets\batch-input-smoke\smoke.conf'
```

Observed result:

```text
Batch dry run complete: 1 prompt file(s) would run, 2 image request(s) would be made, 0 would skip.
```

Decision:

- `--gallery-index` is the first shared gallery/contact-sheet hook.
- It indexes existing sidecar JSON only; it does not call the API, render a contact sheet, or write lane-owned gallery pages.

## Workflow B Gallery Index Hook Reviewer Finding

Date: 2026-05-09

Reviewer verification:

```powershell
py .\src\generate.py --help
$env:PYTHONPATH=(Resolve-Path 'src').Path; py -B -m unittest discover -s tests
py .\src\generate.py --gallery-index --gallery-source assets\generated --gallery-output $env:TEMP\vaultforge-engine-gallery-index-review.json
py .\src\generate.py '@assets\batch-input-smoke\smoke.conf'
py .\src\generate.py --gallery-index --dry-run --gallery-source assets\generated --gallery-output $env:TEMP\vaultforge-engine-gallery-index-dry-run-conflict.json
```

Passing checks:

- Help includes the gallery index flags.
- Unit tests passed: `Ran 23 tests`, `OK`.
- A normal gallery-index smoke wrote a temp JSON index.
- The committed smoke config dry-run still completed without a live API call.

Blocking finding:

- `--gallery-index --dry-run` still writes the gallery index JSON. That conflicts with the current engine decision that `--dry-run` is the no-write preview path.

Next safe fix:

- Reject `--gallery-index --dry-run`, or make that combination preview-only, and add a regression test before marking `engine-gallery-hooks` complete.

## Workflow B Gallery Index Dry-Run Guard

Date: 2026-05-09

Unit tests:

```powershell
$env:PYTHONPATH=(Resolve-Path 'src').Path; py -B -m unittest discover -s tests
```

Result:

```text
Ran 24 tests
OK
```

Rejected dry-run conflict:

```powershell
$out = Join-Path $env:TEMP 'vaultforge-engine-gallery-index-dry-run-guard.json'
if (Test-Path $out) { Remove-Item -LiteralPath $out -Force }
py .\src\generate.py --gallery-index --dry-run --gallery-source assets\generated --gallery-output $out
Test-Path $out
```

Observed result:

```text
generate.py: error: --gallery-index cannot be combined with --dry-run because it writes an index file.
Exit code: 2
Output exists: false
```

Normal gallery-index smoke:

```powershell
$out = Join-Path $env:TEMP 'vaultforge-engine-gallery-index-guard-normal.json'
if (Test-Path $out) { Remove-Item -LiteralPath $out -Force }
py .\src\generate.py --gallery-index --gallery-source assets\generated --gallery-output $out
Test-Path $out
```

Observed result:

```text
Gallery index written: C:\Users\natha\AppData\Local\Temp\vaultforge-engine-gallery-index-guard-normal.json
Exit code: 0
Output exists: true
```

Decision:

- Reject `--gallery-index --dry-run` instead of adding a second preview behavior.
- Keep `--dry-run` as the engine no-write preview contract.
- Keep normal `--gallery-index` as an explicit index-writing operation.
