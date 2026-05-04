# Icon Changelog

## 2026-05-04

- Added workflow continuation rules so soft gates are parked as `#nath` tasks
  and approved docs-only or dry-run work can continue through another role
  rotation instead of stopping after one cycle.

## 2026-05-03

- Added `MAKE_ICON_DRY_RUN_TRANSCRIPT_CHECK.md` as the no-write `$make-icon`
  dry-run transcript acceptance check, with pass/fail criteria that forbid
  scripts, output folders, generated artifacts, APIs, images, asset operations,
  and folder icon application.
- Added the `#approved` task stamp rule for tasks Nath has explicitly cleared
  and kept approval stamps as separate task tags.
- Reviewed `MAKE_ICON_INTERFACE_PLAN.md` and accepted the no-write `$make-icon`
  command shape for planning only, while keeping script implementation parked.
- Added the `#nath` task-tag rule and tagged open tasks that require Nath
  approval, decision, unblock, or step-in before proceeding.
- Drafted `MAKE_ICON_INTERFACE_PLAN.md` as the no-write `$make-icon` interface
  plan, including planned command inputs, preview output, dry-run behavior, and
  output path assumptions without creating scripts or assets.
- Updated the icon-lane rotation scope rule so one normal rotation may complete
  the active task plus up to two small related docs-only tasks when no stop
  gates are triggered.
- Reviewed the two manual `$make-icon` briefs and decided the metadata/output
  shape is stable enough to plan a no-write tool interface while keeping
  `make_icon.py` parked.
- Added a second manual docs-only `$make-icon` brief for `build-notes`, proving
  the contract can cover a process-notes folder as well as a practical subtool
  folder without generation, scripts, API calls, asset moves, or folder-icon
  application.
- Added a manual docs-only `$make-icon` brief for `svg-forge`, proving the
  current contract can produce a useful planning artifact without generation,
  scripts, API calls, asset moves, or folder-icon application.
- Clarified the icon-lane cycle estimate rule: one cycle is a full ordered role
  rotation, and 7-cycle runs mean repeating that full rotation only when scope
  justifies it.
- Corrected the earlier SVG-Forge setup-doc workflow wording so it is recorded
  as a compact bounded pass, not a true seven-full-rotation run.
- Added `MAKE_ICON_CONTRACT.md` as the no-paid-call `$make-icon` contract and
  kept `make_icon.py` parked behind repeat-use, metadata, dry-run, output,
  ownership, and Nath-approval conditions.
- Added the icon-lane newest-first recording rule: new `SIGN_UP.md` dated
  entries and new `CHANGELOG.md` entries go above older entries.
- Reordered existing `SIGN_UP.md` dated entries and this changelog section so
  future entries have a clean newest-first pattern to follow.
- Clarified SVG-Forge setup and sample docs around the missing setup helper,
  required working directory, and the difference between generated sample files
  and no-write dry-run fixture checks.
- Ran the first bounded icon-lane workflow pass on SVG-Forge setup docs,
  keeping the change docs/dry-run only and recording that Inspiration Scout was
  useful for choosing the next docs-only contract task without expanding scope.
- Added a dry-run-only SVG-Forge sample fixture path and README guidance so
  future no-write dry-runs have a stable expected result.
- Assessed `build-notes` and adopted only lightweight manual workflow rules for
  briefs, review, recording, smoke-test evidence, and bounded inspiration while
  parking formal skills and icon tools behind repeat-use conditions.
- Ran the documented SVG-Forge dry-run command and confirmed it did not change
  the existing output snapshot, but it currently exits with `error: no
  supported input files found` because `samples` only contains `README.md`.
- Documented `svg-forge` as the first existing icon-lane subtool and queued a
  dry-run validation task instead of rewriting it.
- Promoted `vaultforge-icon` into a lightweight active VaultForge lane with
  `CODEX_START.md`, `SYSTEM.md`, `PLAN.md`, `TASKS.md`, `CHANGELOG.md`, and
  `SIGN_UP.md`.
