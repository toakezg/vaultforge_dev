# Icon Tasks

## Icon Open Tasks

```tasks
not done
tag includes icon
```

## Active Pool

- [ ] 🔽 Review the planned `$make-icon` output path assumptions and decide whether `vaultforge-icon/generated/briefs/` and `vaultforge-icon/generated/metadata/` should stay, change, or remain parked #icon #planning #approved 🆔 icon-make-output-path-review ⛔ icon-make-dry-run-transcript-check 2026-05-03

## Next

- [ ] 🔽 Decide whether `$review-handoff-writer` should become a real skill after two more icon-lane handoff updates reuse the same shape #icon #skills 🆔 icon-skill-review-handoff-condition ⛔ icon-seven-cycle-test 2026-05-03
- [ ] 🔽 Decide whether `$smoke-test-recorder` should become a real skill after repeated SVG-Forge or wrapper checks use the same command/exit/no-write evidence shape #icon #skills 🆔 icon-skill-smoke-recorder-condition ⛔ icon-seven-cycle-test 2026-05-03
- [ ] 🔽 Draft an approved apply-plan format before any `$apply-icon` or `apply_icon.py` implementation #icon #tools #nath #approved 🆔 icon-apply-tool-contract 2026-05-03
- [ ] 🔽 Decide whether real SVG-Forge sample rasters should be generated for conversion smoke tests after reviewing write scope and cleanup expectations #icon #validation #nath #approved 🆔 icon-svg-forge-real-samples-decision 2026-05-03

## Landed Work

- [x] Add workflow continuation rules so soft gates are parked as `#nath` tasks and approved docs-only/dry-run work can continue through another rotation instead of stopping after one cycle #icon #workflow 🆔 icon-workflow-soft-gate-continuation 2026-05-04 ✅ 2026-05-04
- [x] Define the exact no-write `$make-icon` dry-run transcript acceptance check after the interface plan is reviewed, without creating `make_icon.py`, output folders, or generated artifacts #icon #validation 🆔 icon-make-dry-run-transcript-check ⛔ icon-make-interface-review 2026-05-03 ✅ 2026-05-03
- [x] Add the `#approved` stamp rule for tasks Nath has explicitly cleared and keep approval stamps as separate task tags #icon #workflow 🆔 icon-approved-task-stamp-rule 2026-05-03 ✅ 2026-05-03
- [x] Review `MAKE_ICON_INTERFACE_PLAN.md` and accept the no-write `$make-icon` command shape for planning only, while keeping implementation parked #icon #tools 🆔 icon-make-interface-review ⛔ icon-make-no-write-interface-plan 2026-05-03 ✅ 2026-05-03
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
- Use build-note roles as manual process first; do not create real Codex skills
  until repeated runs prove the stable shape.
- Estimate workflow size by full role rotations: one cycle is Coordinator ->
  Builder -> Reviewer -> Recorder; seven cycles means seven full rotations, not
  seven individual role handoffs.
- Park `make_icon.py` and `apply_icon.py` until their contracts and approval
  gates are written.
- Tag every task with at least one section tag and one task-type tag.
- Tag tasks with `#nath` when Nath must approve, decide, unblock, or step in.
- Use `#approved` as the approval stamp for tasks Nath has explicitly cleared.
- Give active and next tasks a short stable `🆔` id.
