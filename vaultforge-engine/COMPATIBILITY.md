# Compatibility Pass

Date: 2026-04-12

## Goal

Make the existing `vaultforge-art` launcher delegate to `vaultforge-engine` while preserving the old art command shape and art-root defaults.

`vaultforge-business` was not retargeted in this pass.

## Pre-Change Comparison

Single prompt dry-runs used the same prompt composition:

```powershell
.\run_art.bat "A clean geometric VaultForge test icon" --preset icon --style geometric --mod hopeful --dry-run
py .\src\generate.py "A clean geometric VaultForge test icon" --preset icon --style geometric --mod hopeful --dry-run
```

Both composed:

```text
A clean geometric VaultForge test icon. single centered icon subject, clean emblem silhouette, minimal background distraction, readable small-format design. geometric construction, crisp vector-like edges, balanced shapes, strong symbolic clarity. hopeful emotional tone, uplifting light, quiet optimism, forward-looking warmth
```

Observed mismatch:

- `vaultforge-art` default output root was `E:\tools\image_generation\vaultforge-art\assets\generated`.
- `vaultforge-engine` default output root was `E:\tools\vaultforge\vaultforge-engine\assets\generated`.

Batch dry-runs also matched prompt cleanup, preset/style/mod resolution, and batch state naming when pointed at the same prompt folder. The same root mismatch existed for default output paths.

`@file.conf` handling remained compatible, but note that the art smoke config does not include `--dry-run`; explicit `--dry-run` must be added when testing it safely.

## Compatibility Change

The engine now supports a project-root override through:

```text
VAULTFORGE_ENGINE_PROJECT_ROOT
```

The art launcher sets that variable to its own root before calling:

```text
E:\tools\vaultforge\vaultforge-engine\src\generate.py
```

This lets `vaultforge-art` keep its existing command shape while the shared engine owns the generator behavior.

## Post-Change Checks

Engine unit tests:

```powershell
$env:PYTHONPATH=(Resolve-Path 'src').Path; py -m unittest discover -s tests
```

Result:

```text
Ran 7 tests
OK
```

Art launcher single prompt dry-run:

```powershell
.\run_art.bat "A clean geometric VaultForge test icon" --preset icon --style geometric --mod hopeful --dry-run
```

Result:

```text
Output dir: E:\tools\image_generation\vaultforge-art\assets\generated
```

Art launcher batch smoke dry-run:

```powershell
.\run_art.bat --batch-smoke --preset vaultforge --style painterly --mod hopeful --dry-run
```

Result:

```text
Batch dry run complete: 2 prompt file(s) would run, 0 would skip.
```

Art launcher config dry-run:

```powershell
.\run_art.bat '@.\assets\batch-input-smoke\smoke.conf' --dry-run
```

Result:

```text
Batch dry run complete: 0 prompt file(s) would run, 2 would skip.
```

Root XP4Life wrapper dry-run:

```powershell
.\run-icons-part-a.bat --dry-run
```

Result:

```text
quests: 3 prompt file(s) would run
achievements: 3 prompt file(s) would run
titles: 2 prompt file(s) would run
rewards: 2 prompt file(s) would run
```

Direct engine batch smoke dry-run:

```powershell
py .\src\generate.py --batch-smoke --preset icon --style geometric --dry-run
```

Result:

```text
Batch dry run complete: 1 prompt file(s) would run, 0 would skip.
```

## Cleanup Note

One accidental non-dry-run `@smoke.conf` check created two smoke images and an untracked `.batch-state.json` in the art smoke folder. The two generated images and the state file were removed.

## Follow-Up After Business Retarget

Business retargeting was completed in a later pass and is documented in
`COMPATIBILITY_BUSINESS.md`.

Remaining follow-ups:

- Decide how much dry-run metadata writing should remain lane-owned.
- Decide whether business config files should become runtime entrypoints.
- Keep business prompt banks, presets, styles, and mods lane-owned unless they
  become clearly reusable.
