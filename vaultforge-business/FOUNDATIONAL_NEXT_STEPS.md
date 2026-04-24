# Foundational Next Steps

This note captures the shared-core cleanup state after the engine entrypoint rename
and business retarget work, so later dedicated `vaultforge-business` threads can
start from a clean baseline.

## Completed in this pass

- `vaultforge-engine\src\generate_art.py` was renamed to
  `vaultforge-engine\src\generate.py`.
- Current engine-facing wrappers were retargeted to the neutral entrypoint path.
- `vaultforge-business\run_business.ps1` was kept backward-compatible by
  retaining the `ArtRoot` alias while shifting runtime wording to `EngineRoot`
  and `shared engine`.
- `vaultforge-business\run-client-pack.ps1` was hardened by replacing
  `Invoke-Expression` with parsed command invocation so pack lines are executed
  with less quoting and injection risk.
- `vaultforge-business\pack-dryrun-safe.txt` was added as a reusable no-live-run
  pack fixture for future smoke checks.

## Verified already

- Engine unit tests passed after the neutral entrypoint rename.
- Direct engine dry-run passed using `py .\src\generate.py`.
- Business smoke dry-run passed after the retarget.
- Direct `run_business.ps1` dry-run passed after the retarget.
- Pack runner `-WhatIf` expansion passed and showed the expected business-side
  command expansion shape.
- Pack runner execution with `pack-dryrun-safe.txt` passed and returned exit code
  0, while routing outputs under
  `vaultforge-business\generated\dryrun-studio\logo\business-logo\modern-startup\...`.

## Pending verification

- None for the shared-core rename and business retarget baseline.

Reference command used for the completed pack-runner check:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\run-client-pack.ps1 -InputValue "Dryrun Studio" -Client "dryrun-studio" -Project "pack-dryrun-safe" -Tag "local, premium" -PromptFile ".\pack-dryrun-safe.txt" -Tweak "keep it simple" -StopOnError
```

The process-scoped execution-policy bypass was needed on this machine because
the local policy rejected unsigned scripts. The fixture remains safe because the
pack line includes `-DryRun`.

## Best next foundational items

1. Make dry-run consistently no-write.
   - Business dry-run currently still writes some metadata and directories.
   - Tighten the contract so dry-run means no generation and no persistent side
     effects unless explicitly requested.

2. Add wrapper-level parity checks.
   - Capture CLI/help and dry-run snapshots for engine, art bridge, and business
     so future renames do not rely only on manual comparison.

3. Add a small automated check for pack invocation.
   - Even a narrow smoke test around pack expansion and exit-code propagation
     would harden `run-client-pack.ps1` further.

4. Normalize remaining shared-core naming.
   - There are still likely stale labels such as `ArtRoot`, `art engine`, or
     art-specific notes in docs and generated metadata.
   - Treat that as wording cleanup unless it affects routing or correctness.

5. Decide on future business-specific shared-core boundaries.
   - Keep business prompt banks, presets, styles, and mods lane-owned.
   - Only move behavior into engine when it is genuinely shared and stable.

## Separate-thread business work that can run in parallel later

- Review and clean business prompt bank organization.
- Build safer config-driven pack definitions beyond line-by-line shell commands.
- Add gallery/contact-sheet or summary reporting for generated business packs.
- Tighten business metadata conventions and naming rules for client deliverables.

## Current blocker

- None. The prior thread-runner startup failure (`CreateProcessAsUserW failed:
  5`) has cleared, and the remaining pack-runner execution re-check now passes.
