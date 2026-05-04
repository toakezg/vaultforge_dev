# Icon Tasks

## Icon Open Tasks

```tasks
not done
tag includes icon
```

## Active Pool

No active icon task is selected. Use the next approved task unless Nath picks a
different slice.

## Next

- [ ] 🔼 Run a small media-folder icon-set proposal batch from `generated/proposals/inbox/media-style-guide-note.md`, using the icon-set workflow contract and stopping before selection or folder-icon application #icon #proposals #approved 🆔 icon-media-style-set-proposal 2026-05-04
- [ ] 🔽 Draft a directory-scout proposal intake checklist that can inspect a scoped target folder, summarize folders/subfolders, and write proposal-ready descriptions into `generated/proposals/inbox/` #icon #proposals #approved 🆔 icon-directory-scout-intake-checklist 2026-05-04
- [ ] 🔽 Draft the root-cooperative `$review-handoff-writer` spec/checklist for icon-to-root recording, without creating a real skill file until the spec is reviewed #icon #skills #approved 🆔 icon-review-handoff-root-coop-spec 2026-05-04

## Landed Work

- [x] Set up `generated/proposals/inbox/` for user/agent idea drops and add the media color style guide as reference input for future proposal runs #icon #proposals #approved 🆔 icon-proposal-inbox-setup 2026-05-04 ✅ 2026-05-04
- [x] Add `documents/contracts/ICON_SET_GENERATION_WORKFLOW_CONTRACT.md` to define directory/style-guide input, Directory Scout, set generation, review, and later apply-plan flow without applying folder icons #icon #proposals #docs #approved 🆔 icon-set-generation-workflow-contract 2026-05-04 ✅ 2026-05-04
- [x] Add `run_icon_proposal.ps1` so the icon lane can load `ICON_KEY` from `vaultforge-icon/.env`, map it to the engine's expected image-generation key variable for the child process only, and manage proposal generation without printing secrets #icon #tools #approved 🆔 icon-proposal-env-runner 2026-05-04 ✅ 2026-05-04
- [x] Finish the first approved inspired-agent icon proposal pass into `vaultforge-icon/generated/proposals/first-inspired-run/`; proposal Markdown, three prompt files, three PNG proposal images, three JSON metadata files, and batch state were written using the lane `.env` key through `run_icon_proposal.ps1` #icon #proposals #approved 🆔 icon-inspired-agent-first-proposal-run 2026-05-04 ✅ 2026-05-04
- [x] Record Nath's approval that inspired-agent proposal docs may guide future icon proposal runs and that `vaultforge-icon/generated/proposals/` is approved for proposal Markdown, supporting metadata, generated proposal images, and run metadata, including scoped API/paid generation #icon #proposals #approved 🆔 icon-inspired-agent-proposal-approval 2026-05-04 ✅ 2026-05-04
- [x] Organize icon-lane contracts, reviews, and decisions into `documents/contracts/`, `documents/reviews/`, and `documents/decisions/`, leaving root for operational docs #icon #docs #approved 🆔 icon-documents-cleanup 2026-05-04 ✅ 2026-05-04
- [x] Mark XP4Life Part A notes as reference/inspiration only, not direct build requirements or the current `$make-icon` planning contract #icon #docs #xp4life #approved 🆔 icon-part-a-reference-warning 2026-05-04 ✅ 2026-05-04
- [x] Revise `$review-handoff-writer` conditions so root-doc cooperation counts as approved cross-lane need while real skill/spec creation remains a scoped follow-up #icon #skills #approved 🆔 icon-review-handoff-root-coop-approved 2026-05-04 ✅ 2026-05-04
- [x] Decide not to create `$smoke-test-recorder` as a real skill now; keep it parked and revise activation to require at least two more repeated smoke records across different cases, including at least one wrapper or no-write check #icon #skills 🆔 icon-skill-smoke-recorder-condition ⛔ icon-seven-cycle-test 2026-05-03 ✅ 2026-05-04
- [x] Decide not to create `$review-handoff-writer` as a real skill now; keep it parked and revise activation to require cross-lane reuse, missed-field pain, or Nath asking for a reusable recorder outside the icon lane #icon #skills 🆔 icon-skill-review-handoff-condition ⛔ icon-seven-cycle-test 2026-05-03 ✅ 2026-05-04
- [x] Run the explicitly approved SVG-Forge real-sample smoke validation from `vaultforge-icon\svg-forge`: `.\.venv\Scripts\python.exe .\tools\make_samples.py` exited 0, `.\run_svg_forge.bat --input ".\samples" --output ".\output\real-sample-smoke" --preset icon-clean` exited 0, wrote three sample rasters plus three inspectable SVGs and `svg-forge.log`, and did not delete or move prior outputs #icon #validation #live-required #approved 🆔 icon-svg-forge-real-sample-live-smoke 2026-05-04 ✅ 2026-05-04
- [x] Update the icon-lane no-write policy so local file/folder writes are approved only when explicitly scoped and lane-local, while preserving hard gates for secrets/cloud auth, paid/API work, generated artifacts, asset move/delete, folder-icon application, ownership changes, and taste decisions #icon #workflow #approved 🆔 icon-local-write-scope-policy 2026-05-04 ✅ 2026-05-04
- [x] Decide not to generate real SVG-Forge sample rasters during the docs-only rotation, document the write scope and cleanup expectations, and park the exact future live run as `#live-required` #icon #validation #approved 🆔 icon-svg-forge-real-samples-decision 2026-05-03 ✅ 2026-05-04
- [x] Draft an approved apply-plan format before any `$apply-icon` or `apply_icon.py` implementation, while keeping scripts, generated outputs, assets, and folder-icon application parked #icon #tools #approved 🆔 icon-apply-tool-contract 2026-05-03 ✅ 2026-05-04
- [x] Review the planned `$make-icon` output path assumptions and keep `vaultforge-icon/generated/briefs/` plus `vaultforge-icon/generated/metadata/` as no-write preview defaults while leaving the folders parked and uncreated #icon #planning #approved 🆔 icon-make-output-path-review ⛔ icon-make-dry-run-transcript-check 2026-05-03 ✅ 2026-05-04
- [x] Retune approval gates so build/dry-run work can continue toward the icon-generator goal, reserve `#nath` for hard gates, and use `#live-required` for missing live runs that do not block dry-run progress #icon #workflow 🆔 icon-live-required-soft-gate-rule 2026-05-04 ✅ 2026-05-04
- [x] Add workflow continuation rules so soft gates are parked as `#nath` tasks and approved docs-only/dry-run work can continue through another rotation instead of stopping after one cycle #icon #workflow 🆔 icon-workflow-soft-gate-continuation 2026-05-04 ✅ 2026-05-04
- [x] Define the exact no-write `$make-icon` dry-run transcript acceptance check after the interface plan is reviewed, without creating `make_icon.py`, output folders, or generated artifacts #icon #validation 🆔 icon-make-dry-run-transcript-check ⛔ icon-make-interface-review 2026-05-03 ✅ 2026-05-03
- [x] Add the `#approved` stamp rule for tasks Nath has explicitly cleared and keep approval stamps as separate task tags #icon #workflow 🆔 icon-approved-task-stamp-rule 2026-05-03 ✅ 2026-05-03
- [x] Review `documents/contracts/MAKE_ICON_INTERFACE_PLAN.md` and accept the no-write `$make-icon` command shape for planning only, while keeping implementation parked #icon #tools 🆔 icon-make-interface-review ⛔ icon-make-no-write-interface-plan 2026-05-03 ✅ 2026-05-03
- [x] Add the `#nath` task-tag rule and tag open tasks that require Nath approval, decision, unblock, or step-in before proceeding #icon #workflow 🆔 icon-nath-task-tag-rule 2026-05-03 ✅ 2026-05-03
- [x] Draft a no-write `$make-icon` interface plan that describes command inputs, preview output, dry-run behavior, and output path assumptions without creating `make_icon.py` or generating/applying assets #icon #tools 🆔 icon-make-no-write-interface-plan ⛔ icon-make-brief-review 2026-05-03 ✅ 2026-05-03
- [x] Update the icon-lane rotation scope limit so one normal rotation may land the active task plus up to two small related docs-only tasks when no stop gates are triggered #icon #workflow 🆔 icon-rotation-two-task-limit 2026-05-03 ✅ 2026-05-03
- [x] Review the two manual `$make-icon` briefs and decide the metadata/output shape is stable enough to plan a no-write tool interface, while keeping `make_icon.py` parked unless Nath approves implementation #icon #tools 🆔 icon-make-brief-review ⛔ icon-make-second-manual-brief 2026-05-03 ✅ 2026-05-03
- [x] Run a second manual docs-only `$make-icon` brief for `build-notes` and confirm the contract can handle a process-notes folder as well as a practical subtool folder #icon #tools 🆔 icon-make-second-manual-brief 2026-05-03 ✅ 2026-05-03
- [x] Run one manual docs-only `$make-icon` brief for `svg-forge` and confirm the contract remains useful while `make_icon.py` stays parked #icon #tools 🆔 icon-make-manual-brief-test 2026-05-03 ✅ 2026-05-03
- [x] Clarify the icon-lane cycle estimate rule: one cycle is a full ordered role rotation, and 7-cycle runs repeat that rotation only when scope justifies it #icon #workflow 🆔 icon-cycle-estimate-rule 2026-05-03 ✅ 2026-05-03
- [x] Draft the no-paid-call `$make-icon` contract and keep `make_icon.py` parked behind repeat-use, metadata, dry-run, output, ownership, and Nath-approval conditions #icon #tools 🆔 icon-make-tool-contract 2026-05-03 ✅ 2026-05-03
- [x] Add the icon-lane newest-first recording rule and reorder `SIGN_UP.md` plus `CHANGELOG.md` so future entries follow it cleanly #icon #docs 🆔 icon-newest-first-recording-rule 2026-05-03 ✅ 2026-05-03
- [x] Promote `vaultforge-icon` as a lightweight active icon lane with a section doc spine and SVG-Forge as its first existing subtool #icon #docs 2026-05-03
- [x] Verify the documented SVG-Forge dry-run path stayed no-write but is currently blocked by missing sample raster inputs #icon #validation 🆔 icon-svg-forge-dry-run 2026-05-03 ✅ 2026-05-03
- [x] Assess `build-notes` and adopt only lightweight workflow rules while parking formal skills and icon tools behind clear conditions #icon #planning 🆔 icon-build-notes-assessment 2026-05-03 ✅ 2026-05-03
- [x] Add a dry-run-only SVG-Forge sample fixture path and verify the dry-run expected result without output writes #icon #validation 🆔 icon-svg-forge-dry-run-fixture 2026-05-03 ✅ 2026-05-03
- [x] Run a bounded icon workflow pass on SVG-Forge setup docs and record Inspiration Scout outcomes without expanding scope; later clarified this was not a true seven-full-rotation run #icon #workflow 🆔 icon-seven-cycle-test 2026-05-03 ✅ 2026-05-03
- [x] Clarify SVG-Forge setup docs around the missing setup helper, working directory, and write-vs-dry-run sample paths #icon #docs 🆔 icon-svg-forge-setup-docs 2026-05-03 ✅ 2026-05-03

## Working Rules

- Keep icon work lane-owned and lightweight.
- Keep shared generation contracts in engine.
- Keep general art experimentation in art.
- Keep client/business packaging in business unless an icon proof needs a local
  note first.
- Use dry-run checks before live generation or conversion changes.
- Local file/folder writes are approved when the task explicitly scopes the
  write and the path stays inside the lane/write scope.
- Generated artifacts and generated output folders still need explicit
  path-level approval.
- Use build-note roles as manual process first; do not create real Codex skills
  until repeated runs prove the stable shape.
- Estimate workflow size by full role rotations: one cycle is Coordinator ->
  Builder -> Reviewer -> Recorder; seven cycles means seven full rotations, not
  seven individual role handoffs.
- Park `make_icon.py` and `apply_icon.py` until their contracts and approval
  gates are written.
- Tag every task with at least one section tag and one task-type tag.
- Tag tasks with `#nath` only when Nath must approve, decide, unblock, or step
  in at a hard gate.
- Tag tasks with `#live-required` when a future non-dry-run validation is
  needed but dry-run/build work can continue.
- Use `#approved` as the approval stamp for tasks Nath has explicitly cleared.
- Give active and next tasks a short stable `🆔` id.
