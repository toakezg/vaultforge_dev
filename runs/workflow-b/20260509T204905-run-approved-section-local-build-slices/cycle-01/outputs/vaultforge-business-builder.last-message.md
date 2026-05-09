Implemented the business builder slice in `F:\vaultforge\vaultforge-business`.

Changes landed:
- [run_business.ps1](F:/vaultforge/vaultforge-business/run_business.ps1:21) now defaults to sibling `..\vaultforge-engine`, preserves `-EngineRoot` / `-ArtRoot`, and passes engine-native `--client`, `--job`, `--tag`, and `--variants`.
- [run_business.ps1](F:/vaultforge/vaultforge-business/run_business.ps1:242) now calls the engine once per business run and lets engine-native variants fan out.
- [run_business_md_bank.ps1](F:/vaultforge/vaultforge-business/run_business_md_bank.ps1:4) now uses the same sibling engine default.
- Updated business docs/tasks/changelog/handoff in [README.md](F:/vaultforge/vaultforge-business/README.md:146), [PLAN.md](F:/vaultforge/vaultforge-business/PLAN.md:30), [TASKS.md](F:/vaultforge/vaultforge-business/TASKS.md:42), [CHANGELOG.md](F:/vaultforge/vaultforge-business/CHANGELOG.md:3), and [SIGN_UP.md](F:/vaultforge/vaultforge-business/SIGN_UP.md:53).

Verification run:
- PowerShell parser checks passed for both wrappers.
- Direct `run_business.ps1 -WhatIf` showed `--client`, `--job`, `--tag`, and `--variants 2`.
- Direct `run_business.ps1 -DryRun` reached the engine, showed context metadata and two variant output paths, and did not create the unique checked business output folder.
- `run_business_smoke.bat` passed.
- Markdown-bank `-WhatIf` passed.
- Pack-runner `-WhatIf` exposed a pre-existing log side effect; I removed the verification log row and added follow-up task `business-pack-whatif-log-side-effect`.

No live generation was run. The next recorded slice is `business-manifest-contract-review`.

