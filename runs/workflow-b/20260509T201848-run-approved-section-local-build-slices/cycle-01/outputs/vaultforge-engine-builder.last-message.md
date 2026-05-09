Completed the `vaultforge-engine` builder slice.

I added the committed dry-run smoke config path and manifest contract draft:
- [smoke.conf](F:/vaultforge/vaultforge-engine/assets/batch-input-smoke/smoke.conf:1) now exercises `@file.conf`, batch smoke, explicit output dir, client/job/tag metadata, two variants, and `--reference-image`.
- [smoke-reference.svg](F:/vaultforge/vaultforge-engine/tests/fixtures/smoke-reference.svg:1) is tracked under tests fixtures so the config is portable.
- [RUN_MANIFEST.md](F:/vaultforge/vaultforge-engine/RUN_MANIFEST.md:1) defines the first stable sidecar field list for future gallery/contact-sheet work.
- Updated [README.md](F:/vaultforge/vaultforge-engine/README.md:1), [VERIFICATION.md](F:/vaultforge/vaultforge-engine/VERIFICATION.md:1), [PLAN.md](F:/vaultforge/vaultforge-engine/PLAN.md:1), [TASKS.md](F:/vaultforge/vaultforge-engine/TASKS.md:1), [CHANGELOG.md](F:/vaultforge/vaultforge-engine/CHANGELOG.md:1), and [SIGN_UP.md](F:/vaultforge/vaultforge-engine/SIGN_UP.md:1).

Verification passed:
- `py .\src\generate.py --help`
- `$env:PYTHONPATH=(Resolve-Path 'src').Path; py -B -m unittest discover -s tests` -> `Ran 20 tests`, `OK`
- `py .\src\generate.py '@assets\batch-input-smoke\smoke.conf'` -> dry-run only, 1 prompt, 2 image requests previewed, metadata paths previewed, no generated output or batch state written
- `git diff --check -- vaultforge-engine` -> no whitespace errors, only existing CRLF normalization warnings

No hard gate found. The slice is ready for the engine reviewer pass.

