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
