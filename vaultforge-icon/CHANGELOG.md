# Icon Changelog

## 2026-05-04

- Added `generated/proposals/inbox/` for user or agent idea drops, including a
  media color style guide note sourced from `f:\media\icons\my_icons\style-guide.txt`.
- Added `documents/contracts/ICON_SET_GENERATION_WORKFLOW_CONTRACT.md` to define
  the future directory/style-guide-to-icon-set workflow with Directory Scout,
  Inspiration Scout, generation, review, and later apply-plan handoff.
- Added `run_icon_proposal.ps1` so the icon lane can use `ICON_KEY` from
  `vaultforge-icon/.env` while still calling the shared engine. The runner maps
  the key to the engine's expected variable only for the generation process and
  does not print secrets.
- Finished the first inspired-agent proposal run after switching to the
  lane-local `.env` key: `generated/proposals/first-inspired-run/` now contains
  proposal Markdown, three prompt files, three PNG proposal images, three JSON
  metadata files, and batch state.
- Created the first inspired-agent proposal run folder at
  `generated/proposals/first-inspired-run/` with proposal Markdown, three prompt
  files, an `images/` output folder, and a run log. The clean dry-run exited 0
  with 3 prompt files planned and 0 skipped. The live engine attempt exited 1
  because the existing API key lacks `api.responses.write` scope, so no proposal
  images, JSON metadata, selected/applied outputs, asset operations, or folder
  icon application were produced.
- Organized icon-lane contracts, reviews, and decisions into
  `documents/contracts/`, `documents/reviews/`, and `documents/decisions/`,
  with `documents/README.md` as the local index.
- Added reference-only warnings to the XP4Life Part A notes so they can guide
  future routes without acting as current build requirements or `$make-icon`
  planning contracts.
- Recorded Nath's approval for inspired-agent proposal docs to guide future icon
  proposal runs, and approved `generated/proposals/` for proposal Markdown,
  supporting metadata, generated proposal images, and run metadata, including
  scoped API/paid generation.
- Revised `$review-handoff-writer` conditions so root-doc cooperation counts as
  approved cross-lane need, while real skill/spec creation remains a scoped
  follow-up task.
- Added `documents/decisions/ICON_SKILL_CONDITIONS_DECISION.md` and decided not to create
  `$review-handoff-writer` or `$smoke-test-recorder` as real skills now. Both
  remain parked with revised activation gates based on cross-lane reuse,
  missed-field pain, Nath request, and repeated smoke evidence across different
  check types.
- Ran the explicitly approved SVG-Forge real-sample smoke validation from
  `vaultforge-icon\svg-forge`. `tools\make_samples.py` wrote three local sample
  rasters, and `run_svg_forge.bat --input ".\samples" --output
  ".\output\real-sample-smoke" --preset icon-clean` converted them into three
  inspectable SVGs plus `svg-forge.log` with both commands exiting 0.
- Updated the icon-lane no-write policy: local file/folder writes are approved
  when a task explicitly scopes them and the paths stay inside the lane/write
  scope. Hard gates remain for secrets/cloud auth, paid/API work, generated
  artifacts without path approval, asset move/delete, folder-icon application,
  ownership changes, and taste decisions.
- Added `documents/decisions/SVG_FORGE_REAL_SAMPLES_DECISION.md`, deciding not to generate real
  SVG-Forge sample rasters during the docs-only rotation and parking the exact
  future write validation as `#live-required`.
- Added `documents/contracts/APPLY_ICON_APPLY_PLAN_CONTRACT.md` as the docs-only approved
  `$apply-icon` apply-plan format, with required plan fields, target-entry
  fields, Markdown/JSON previews, dry-run transcript requirements, and
  activation gates that keep `apply_icon.py`, generated outputs, asset
  operations, and folder-icon application parked.
- Added `documents/reviews/MAKE_ICON_OUTPUT_PATH_REVIEW.md` and accepted
  `vaultforge-icon/generated/briefs/` plus
  `vaultforge-icon/generated/metadata/` as planned no-write preview defaults,
  while keeping the folders parked and uncreated until a later approved write
  task.
- Retuned workflow approval gates so build and dry-run work can continue toward
  the icon-generator goal, `#nath` is reserved for hard gates, and future
  non-dry-run validation is recorded as `#live-required` when it does not block
  safe progress.
- Added workflow continuation rules so soft gates are parked as `#nath` tasks
  and approved docs-only or dry-run work can continue through another role
  rotation instead of stopping after one cycle.

## 2026-05-03

- Added `documents/contracts/MAKE_ICON_DRY_RUN_TRANSCRIPT_CHECK.md` as the no-write `$make-icon`
  dry-run transcript acceptance check, with pass/fail criteria that forbid
  scripts, output folders, generated artifacts, APIs, images, asset operations,
  and folder icon application.
- Added the `#approved` task stamp rule for tasks Nath has explicitly cleared
  and kept approval stamps as separate task tags.
- Reviewed `documents/contracts/MAKE_ICON_INTERFACE_PLAN.md` and accepted the no-write `$make-icon`
  command shape for planning only, while keeping script implementation parked.
- Added the `#nath` task-tag rule and tagged open tasks that require Nath
  approval, decision, unblock, or step-in before proceeding.
- Drafted `documents/contracts/MAKE_ICON_INTERFACE_PLAN.md` as the no-write `$make-icon` interface
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
- Added `documents/contracts/MAKE_ICON_CONTRACT.md` as the no-paid-call `$make-icon` contract and
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
