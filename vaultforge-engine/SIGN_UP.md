# Engine Sign Up

New engine threads should add a short entry here before or after their first meaningful change.

Use this shape:

```text
## YYYY-MM-DD - thread label

- Role:
- Scope:
- Read:
- Changed:
- Handoff:
```

## 2026-05-10 - workflow b 055419 engine reviewer

- Role: Reviewer for Workflow B cycle 1, engine lane
- Scope: review the evidence-only engine builder pass for run `20260510T055419-run-approved-build-slices-while-analyzing-workfl`
- Read: cycle 1 coordinator routing note, builder last message, current workflow review guidance, dirty baseline, engine `TASKS.md`, `SIGN_UP.md`, `VERIFICATION.md`, `src\generate.py`, `tests\test_generate.py`, and current `assets\generated`
- Changed: recorded this reviewer handoff and run-packet review note only
- Handoff: no blocking findings. Reviewer reran 24 unit tests, the committed smoke config dry-run, normal empty gallery-index smoke to a temp file, `--gallery-index --dry-run` rejection, and `git diff --check` for the scoped engine files. The contact-sheet renderer remains correctly parked as `#live-required`; no live generation, generated art, fixture-policy decision, cross-lane ownership change, root Workflow B controller edit, or renderer implementation was approved.

## 2026-05-10 - workflow b 055419 engine builder

- Role: Builder for Workflow B cycle 1, engine lane
- Scope: section-local verification and handoff evidence for run `20260510T055419-run-approved-build-slices-while-analyzing-workfl`
- Read: cycle 1 root coordinator routing note, active run packet plan/status/live status, dirty baseline, Workflow A/B review guidance, engine `README.md`, `TASKS.md`, `SIGN_UP.md`, `VERIFICATION.md`, `RUN_MANIFEST.md`, and current `assets\generated`
- Changed: recorded verification evidence only; no renderer implementation because the coordinator routed this slot as evidence-only and `engine-contact-sheet-renderer` remains `#live-required`
- Handoff: no hard gate was triggered in engine. Unit tests passed, the committed smoke config dry-run stayed no-live/no-write, normal gallery-index over empty `assets\generated` wrote a temp zero-entry index, and `--gallery-index --dry-run` rejected without creating output. No safe engine implementation slice remains until real sidecar examples or a root-approved contact-sheet fixture strategy exists; reviewer should check this evidence and then Workflow B should continue through reviewer/recorder or another approved safe slice outside engine.

## 2026-05-10 - workflow b 012133 engine builder

- Role: Builder for Workflow B cycle 1, engine lane
- Scope: section-local verification and handoff evidence for run `20260510T012133-run-approved-section-local-build-slices-while-an`
- Read: cycle 1 root coordinator routing note, active run packet live status/status stream, dirty baseline, Workflow A/B review guidance, engine `TASKS.md`, `SIGN_UP.md`, `VERIFICATION.md`, `RUN_MANIFEST.md`, and current `assets\generated`
- Changed: recorded verification evidence only; no renderer implementation because the coordinator routed this slot as evidence-only and `engine-contact-sheet-renderer` remains `#live-required`
- Handoff: no hard gate was triggered in engine. Unit tests passed, the committed smoke config dry-run stayed no-live/no-write, normal gallery-index over empty `assets\generated` wrote a temp zero-entry index, and `--gallery-index --dry-run` rejected without creating output. No safe engine implementation slice remains until real sidecar examples or a root-approved contact-sheet fixture strategy exists; reviewer should check this evidence and then Workflow B should continue through reviewer/recorder or another approved safe slice outside engine.

## 2026-05-10 - workflow b 005900 engine builder

- Role: Builder for Workflow B cycle 1, engine lane
- Scope: section-local verification and handoff evidence for run `20260510T005900-run-approved-section-local-build-slices-while-an`
- Read: current run packet plan/status, cycle 1 root coordinator routing note, dirty baseline, engine `TASKS.md`, `SIGN_UP.md`, `VERIFICATION.md`, `RUN_MANIFEST.md`, current `assets\generated`, and gallery/index test coverage
- Changed: recorded verification evidence only; no renderer implementation because the coordinator parked `engine-contact-sheet-renderer` as `#live-required` and `assets\generated` still has no real sidecar examples to consume
- Handoff: no hard gate was triggered in engine. Unit tests passed, the committed smoke config dry-run stayed no-live/no-write, normal gallery-index over empty `assets\generated` wrote a temp zero-entry index, and `--gallery-index --dry-run` rejected without creating output. No safe engine implementation slice remains until real sidecar examples or a root-approved contact-sheet fixture strategy exists; route the next safe Workflow B slice away from engine or fix the root resume `--execute` flag.

## 2026-05-10 - workflow b 005900 engine reviewer

- Role: Reviewer for Workflow B cycle 1, engine lane
- Scope: review the builder's evidence-only pass for run `20260510T005900-run-approved-section-local-build-slices-while-an`
- Read: run packet plan/status, root coordinator routing, builder output, dirty baseline, builder diff, `TASKS.md`, `SIGN_UP.md`, `VERIFICATION.md`, `src\generate.py`, `tests\test_generate.py`, and current `assets\generated`
- Changed: recorded this reviewer handoff and run-packet review note only
- Handoff: no blocking findings. Reviewer reran 24 unit tests, the committed smoke config dry-run, normal empty gallery-index smoke to a temp file, and `--gallery-index --dry-run` rejection. The contact-sheet renderer remains correctly parked as `#live-required`; no live generation, generated art, fixture-policy decision, or renderer implementation was approved.

## 2026-05-10 - workflow b root recorder 005900 engine closure

- Role: Root recorder closing the Workflow B cycle 1 engine slice
- Scope: affected section handoff note only
- Read: active run packet status/checkpoints, coordinator output, engine builder output, engine reviewer output, current engine `SIGN_UP.md`, root `CHANGELOG.md`, and reviewed engine commit metadata
- Changed: recorded that the reviewed engine verification/evidence pass is closed for this cycle and committed as `d400135`
- Handoff: no new engine hard gate was created. `engine-contact-sheet-renderer` remains `#live-required` until real sidecar examples or a root-approved contact-sheet fixture strategy exists. Verification passed with 24 unit tests OK, smoke config dry-run no-live/no-write behavior, normal empty gallery-index output to a temp zero-entry JSON, and `--gallery-index --dry-run` rejection without output. Next safe Workflow B work should route away from engine or fix the root resume `--execute` flag unless new approved engine inputs appear.

## 2026-05-10 - workflow b 005900 cycle 2 engine builder

- Role: Builder for Workflow B cycle 2, engine lane
- Scope: section-local verification and handoff evidence for run `20260510T005900-run-approved-section-local-build-slices-while-an`
- Read: cycle 2 root coordinator routing note, refreshed workflow review guidance, current run packet plan/status/checkpoints, dirty baseline, engine `TASKS.md`, `SIGN_UP.md`, `VERIFICATION.md`, and current `assets\generated`
- Changed: recorded verification evidence only; no renderer implementation because the coordinator kept `engine-contact-sheet-renderer` parked as `#live-required` and routed this engine-only slot as evidence-only
- Handoff: no hard gate was triggered in engine. Unit tests passed, the committed smoke config dry-run stayed no-live/no-write, normal gallery-index over empty `assets\generated` wrote a temp zero-entry index, and `--gallery-index --dry-run` rejected without creating output. No safe engine implementation slice remains until real sidecar examples or a root-approved contact-sheet fixture strategy exists; the next productive approved slice is root-capable Workflow B resume-command work, outside this engine builder scope.

## 2026-05-10 - workflow b 005900 cycle 2 engine reviewer

- Role: Reviewer for Workflow B cycle 2, engine lane
- Scope: review the evidence-only engine builder pass for run `20260510T005900-run-approved-section-local-build-slices-while-an`
- Read: cycle 2 coordinator routing note, builder last message, current workflow review guidance, dirty baseline, engine `TASKS.md`, `SIGN_UP.md`, `VERIFICATION.md`, `src\generate.py`, `tests\test_generate.py`, and current `assets\generated`
- Changed: recorded this reviewer handoff and run-packet review note only
- Handoff: no blocking findings. Reviewer reran 24 unit tests, the committed smoke config dry-run, normal empty gallery-index smoke to a temp file, and `--gallery-index --dry-run` rejection. The contact-sheet renderer remains correctly parked as `#live-required`; no live generation, generated art, fixture-policy decision, cross-lane ownership change, or renderer implementation was approved.

## 2026-05-10 - workflow b root recorder 005900 cycle 2 engine closure

- Role: Root recorder closing the Workflow B cycle 2 engine evidence slice
- Scope: affected section handoff note only
- Read: cycle 2 run packet status/checkpoints, coordinator output, engine builder output, engine reviewer output, current engine `SIGN_UP.md`, and root `CHANGELOG.md`
- Changed: recorded that the cycle 2 evidence-only engine pass is closed without a commit because engine docs were already dirty with mixed pre-existing Workflow B entries
- Handoff: no new engine hard gate was created. `engine-contact-sheet-renderer` remains `#live-required` until real sidecar examples or a root-approved contact-sheet fixture strategy exists. Verification passed with 24 unit tests OK, smoke config dry-run no-live/no-write behavior, normal empty gallery-index output to a temp zero-entry JSON, and `--gallery-index --dry-run` rejection without output. Next productive Workflow B work should route to the root resume-command fix or another approved safe slice unless new approved engine inputs appear.

## 2026-05-10 - workflow b 005900 cycle 3 engine builder

- Role: Builder for Workflow B cycle 3, engine lane
- Scope: section-local verification and handoff evidence for run `20260510T005900-run-approved-section-local-build-slices-while-an`
- Read: cycle 3 coordinator routing note, refreshed workflow review guidance, current run packet status/checkpoints/live status, dirty baseline, engine `TASKS.md`, `SIGN_UP.md`, `VERIFICATION.md`, and current `assets\generated`
- Changed: recorded verification evidence only; no renderer implementation because the coordinator kept `engine-contact-sheet-renderer` parked as `#live-required` and routed this generated engine slot as evidence-only
- Handoff: no hard gate was triggered in engine. Unit tests passed, the committed smoke config dry-run stayed no-live/no-write, normal gallery-index over empty `assets\generated` wrote a temp zero-entry index, and `--gallery-index --dry-run` rejected without creating output. No safe engine implementation slice remains until real sidecar examples or a root-approved contact-sheet fixture strategy exists; the next productive approved slice is root-capable Workflow B resume-command flag work, outside this engine builder scope.

## 2026-05-10 - workflow b 005900 cycle 3 engine reviewer

- Role: Reviewer for Workflow B cycle 3, engine lane
- Scope: review the evidence-only engine builder pass for run `20260510T005900-run-approved-section-local-build-slices-while-an`
- Read: cycle 3 coordinator routing note, builder last message, current workflow review guidance, dirty baseline, engine `TASKS.md`, `SIGN_UP.md`, `VERIFICATION.md`, `src\generate.py`, `tests\test_generate.py`, and current `assets\generated`
- Changed: recorded this reviewer handoff and run-packet review note only
- Handoff: no blocking findings. Reviewer reran 24 unit tests, the committed smoke config dry-run, normal empty gallery-index smoke to a temp file, and `--gallery-index --dry-run` rejection. The contact-sheet renderer remains correctly parked as `#live-required`; no live generation, generated art, fixture-policy decision, cross-lane ownership change, or renderer implementation was approved. No commit was made because the engine docs already had mixed pre-existing Workflow B entries in the dirty baseline.

## 2026-05-10 - workflow b 004631 cycle 2 engine builder

- Role: Builder for Workflow B cycle 2, engine lane
- Scope: section-local verification and handoff evidence for run `20260510T004631-run-approved-section-local-build-slices-while-an`
- Read: current run packet plan/status, cycle 2 root coordinator routing note, dirty baseline, engine `TASKS.md`, `SIGN_UP.md`, `VERIFICATION.md`, and current `assets\generated`
- Changed: recorded verification evidence only; no renderer implementation because `engine-contact-sheet-renderer` remains `#live-required` and `assets\generated` still has no real sidecar examples to consume
- Handoff: no hard gate was triggered in engine. Unit tests passed, the committed smoke config dry-run stayed no-live/no-write, normal gallery-index over empty `assets\generated` wrote a temp zero-entry index, and `--gallery-index --dry-run` rejected without creating output. No safe engine implementation slice remains until real sidecar examples or a root-approved contact-sheet fixture strategy exists; route the next safe Workflow B slice away from engine unless new approved inputs appear.

## 2026-05-10 - workflow b 004631 engine live-required evidence

- Role: Builder for Workflow B cycle 1, engine lane
- Scope: section-local verification and handoff evidence for run `20260510T004631-run-approved-section-local-build-slices-while-an`
- Read: active run packet plan/status, root coordinator routing note, dirty baseline, engine `TASKS.md`, `SIGN_UP.md`, `VERIFICATION.md`, `RUN_MANIFEST.md`, and current `assets\generated`
- Changed: recorded verification evidence only; no renderer implementation because `engine-contact-sheet-renderer` remains `#live-required` and `assets\generated` has no real sidecar examples to consume
- Handoff: no hard gate was triggered in engine. Unit tests passed, the committed smoke config dry-run stayed no-live/no-write, normal gallery-index over empty `assets\generated` wrote a temp zero-entry index, and `--gallery-index --dry-run` rejected without creating output. No safe engine implementation slice remains until real sidecar examples or a root-approved contact-sheet fixture strategy exists.

## 2026-05-10 - workflow b 004631 engine reviewer

- Role: Reviewer for Workflow B cycle 1, engine lane
- Scope: review builder evidence for the contact-sheet live-required gate in run `20260510T004631-run-approved-section-local-build-slices-while-an`
- Read: active run packet routing and builder output, dirty baseline, builder diff, `TASKS.md`, `SIGN_UP.md`, `VERIFICATION.md`, `RUN_MANIFEST.md`, `src\generate.py`, `tests\test_generate.py`, and current `assets\generated`
- Changed: recorded this reviewer handoff only
- Handoff: no blocking findings. Reviewer reran the unit suite, smoke config dry-run, normal empty gallery-index smoke, and `--gallery-index --dry-run` rejection. The contact-sheet renderer remains correctly parked as `#live-required`; no live generation, generated art, fixture-policy decision, or renderer implementation was approved.

## 2026-05-10 - workflow b root recorder 004631 engine closure

- Role: Root recorder closing the Workflow B cycle 1 engine slice
- Scope: affected section handoff note only
- Read: active run packet status/checkpoints, coordinator output, engine builder output, engine reviewer output, current engine `SIGN_UP.md`, current engine `TASKS.md`, and recent commit log
- Changed: recorded that the reviewed engine live-required gate evidence is closed for this cycle and committed as `a7e92e3`
- Handoff: no new engine hard gate was created. `engine-contact-sheet-renderer` remains `#live-required` until real sidecar examples or a root-approved contact-sheet fixture strategy exists. Verification passed with 24 unit tests OK, smoke config dry-run no-live/no-write behavior, normal empty gallery-index output to a temp zero-entry index, and `--gallery-index --dry-run` rejection without output.

## 2026-05-09 - workflow b 235211 engine live-required gate

- Role: Builder for Workflow B cycle 1, engine lane
- Scope: section-local verification and handoff evidence for the contact-sheet renderer gate in run `20260509T235211-run-approved-section-local-build-slices-while-an`
- Read: active run packet plan/status, root coordinator output, dirty baseline, engine `TASKS.md`, `SIGN_UP.md`, `VERIFICATION.md`, and current `assets\generated`
- Changed: recorded verification evidence only; no code change because `engine-contact-sheet-renderer` remains `#live-required` and `assets\generated` has no real sidecar examples to consume
- Handoff: no new engine hard gate. Reviewer should confirm the evidence: unit tests pass, the committed smoke config dry-run remains no-live/no-write, normal gallery-index over empty `assets\generated` writes a temp zero-entry index, and `--gallery-index --dry-run` rejects without creating output. Safe engine implementation work does not remain until real sidecar examples or a root-approved contact-sheet fixture strategy exists.

## 2026-05-09 - workflow b 235211 engine reviewer

- Role: Reviewer for Workflow B cycle 1, engine lane
- Scope: review the builder's live-required contact-sheet gate evidence and dry-run/gallery guard checks for run `20260509T235211-run-approved-section-local-build-slices-while-an`
- Read: active run packet outputs, builder diff, `TASKS.md`, `SIGN_UP.md`, `VERIFICATION.md`, `src\generate.py`, `tests\test_generate.py`, and current `assets\generated`
- Changed: recorded this reviewer handoff only
- Handoff: no blocking findings. The contact-sheet renderer remains correctly parked as `#live-required`; unit tests pass, smoke config dry-run remains no-live/no-write with empty generated output and no batch state, normal gallery-index writes a temp zero-entry index, and `--gallery-index --dry-run` rejects without creating output. Safe engine implementation work does not remain until real sidecar examples or a root-approved contact-sheet fixture strategy exists.

## 2026-05-09 - workflow b 233547 engine live-required gate

- Role: Builder for Workflow B cycle 1, engine lane
- Scope: section-local verification and handoff evidence for the contact-sheet renderer gate
- Read: active run packet status and root coordinator output, dirty baseline, engine `TASKS.md`, `SIGN_UP.md`, `VERIFICATION.md`, `README.md`, and current `assets\generated`
- Changed: recorded verification evidence only; no code change because `engine-contact-sheet-renderer` is already `#live-required` and `assets\generated` has no real sidecar examples to consume
- Handoff: no new engine hard gate. Reviewer should confirm the evidence: unit tests pass, the committed smoke config dry-run remains no-live/no-write, normal gallery-index over empty `assets\generated` writes a temp zero-entry index, and `--gallery-index --dry-run` rejects without creating output. Safe engine implementation work does not remain until real sidecar examples or a root-approved contact-sheet fixture strategy exists.

## 2026-05-09 - workflow b 233547 engine reviewer

- Role: Reviewer for Workflow B cycle 1, engine lane
- Scope: review the builder's live-required contact-sheet gate evidence and dry-run/gallery guard checks
- Read: active run packet outputs, builder diff, `TASKS.md`, `SIGN_UP.md`, `VERIFICATION.md`, `README.md`, `src\generate.py`, `tests\test_generate.py`, and current `assets\generated`
- Changed: recorded this reviewer handoff only
- Handoff: no blocking findings. The contact-sheet renderer remains correctly parked as `#live-required`; unit tests pass, smoke config dry-run remains no-write, normal gallery-index writes a temp zero-entry index, and `--gallery-index --dry-run` rejects without creating output. Safe engine implementation work does not remain until real sidecar examples or a root-approved fixture strategy exists.

## 2026-05-09 - workflow b root recorder 233547 engine closure

- Role: Root recorder closing the Workflow B cycle 1 engine slice
- Scope: affected section handoff note only
- Read: active run packet output notes for root coordinator, engine builder, and engine reviewer; current engine `SIGN_UP.md`; recent commit log
- Changed: recorded that the reviewed engine live-required gate evidence is closed for this cycle and committed as `a50bc48`
- Handoff: no new engine hard gate was created. `engine-contact-sheet-renderer` remains `#live-required` until real sidecar examples or a root-approved contact-sheet fixture strategy exists. The dry-run guard remains intact: `--gallery-index --dry-run` rejects without creating output, while normal explicit gallery-index output is still allowed.

## 2026-05-09 - workflow b engine build slices

- Role: Builder for Workflow B cycle 1, engine lane
- Scope: section-local documentation/task updates only because terminal inspection and verification were blocked by a Windows sandbox `CryptUnprotectData failed: 2148073483` error before PowerShell started
- Read: root and engine snapshots embedded in run packet, including `MULTI_AGENT_WORKFLOW.md`, `THREAD_MAP.md`, engine `PLAN.md`, engine `TASKS.md`, engine `CHANGELOG.md`, and this sign-up pattern
- Changed: marked the config dry-run smoke decision and manifest contract review as complete, added follow-up tasks for a committed dry-run smoke config and a minimal run-manifest field list, and kept gallery hooks blocked behind that manifest field-list task
- Handoff: next engine builder should inspect the live files, then implement `engine-dry-run-smoke-config` and `engine-run-manifest-field-list`; run tests and a dry-run config command before moving gallery hooks forward

## 2026-05-09 - workflow b engine reviewer

- Role: Reviewer for Workflow B cycle 1, engine lane
- Scope: review the builder result for committed dry-run smoke config, run-manifest field list, and section-local docs/task updates
- Read: builder diff, `assets\batch-input-smoke\smoke.conf`, `RUN_MANIFEST.md`, `tests\fixtures\smoke-reference.svg`, `src\generate.py` metadata writer, and the workflow handoff
- Changed: updated this handoff only
- Handoff: no blocking findings. Recorder can record the reviewer pass and keep `engine-gallery-hooks` gated behind `RUN_MANIFEST.md`.

## 2026-05-09 - workflow b engine recorder closure

- Role: Root recorder closing the Workflow B cycle 1 engine slice
- Scope: affected section handoff note only
- Read: run packet outputs for coordinator, engine builder, engine reviewer, and the live engine handoff
- Changed: recorded that the reviewed engine dry-run smoke and run-manifest slice is closed for cycle 1
- Handoff: no hard gate remains for this engine slice. `engine-gallery-hooks` stays a later task gated behind `engine-run-manifest-field-list` / `RUN_MANIFEST.md` review, and should not start inside this recorder pass.

## 2026-05-09 - workflow b engine no-write preview

- Role: Builder for Workflow B cycle 1, engine lane
- Scope: section-local docs and verification evidence for `engine-no-write-preview`
- Read: root coordinator brief, active run packet status/checkpoints, engine `TASKS.md`, `RUN_MANIFEST.md`, `VERIFICATION.md`, and current generator metadata/dry-run paths
- Changed: verified the committed smoke config as the current no-write preview path, marked `engine-no-write-preview` complete, and recorded the decision that no separate preview flag is needed yet
- Handoff: reviewer should check the doc/task updates and the verification evidence. Gallery/contact-sheet work remains a later safe slice and should keep lane-owned gallery files separate unless root expands the sidecar contract.

## 2026-05-09 - workflow b engine no-write preview reviewer

- Role: Reviewer for Workflow B cycle 1, engine lane
- Scope: review the no-write preview decision, task closure, and verification evidence
- Read: builder diff, active run packet outputs, `assets\batch-input-smoke\smoke.conf`, `RUN_MANIFEST.md`, `VERIFICATION.md`, `TASKS.md`, and `src\generate.py` dry-run/metadata paths
- Changed: updated this reviewer handoff only
- Handoff: no blocking findings. The committed smoke config verifies `--dry-run` as the current no-write preview path without creating generated images, sidecar JSON, or batch state. Recorder can capture this pass and continue to the next approved safe slice.

## 2026-05-09 - workflow b engine gallery index hook

- Role: Builder for Workflow B cycle 1, engine lane
- Scope: section-local gallery/contact-sheet hook slice after `RUN_MANIFEST.md` settled the minimum sidecar field list
- Read: active run packet status and plan, `RUN_MANIFEST.md`, `TASKS.md`, `VERIFICATION.md`, `README.md`, `src\generate.py`, and `tests\test_generate.py`
- Changed: added `--gallery-index`, `--gallery-source`, and `--gallery-output`; added sidecar index helpers and tests; documented the hook; marked `engine-gallery-hooks` complete and added a later contact-sheet renderer follow-up
- Handoff: reviewer should check that the hook is index-only, API-free, and lane-neutral. Contact-sheet rendering remains a later task gated behind real gallery-index examples.

## 2026-05-09 - workflow b engine gallery index reviewer

- Role: Reviewer for Workflow B cycle 1, engine lane
- Scope: review the gallery index hook, tests, docs, and dry-run contract behavior
- Read: builder diff, `src\generate.py`, `tests\test_generate.py`, `RUN_MANIFEST.md`, `VERIFICATION.md`, and active run packet outputs
- Changed: recorded a blocking review finding and reopened the gallery hook task pending a dry-run guard
- Handoff: blocking finding: `py .\src\generate.py --gallery-index --dry-run --gallery-source assets\generated --gallery-output $env:TEMP\vaultforge-engine-gallery-index-dry-run-conflict.json` writes the output JSON even though engine `--dry-run` is documented as the no-write preview path. Next safe fix should reject the flag combination or implement a true gallery-index preview before review commits the slice.

## Multi-Agent Handoff

- Task: Run approved section-local build slices
- Current role: Reviewer blocked engine gallery index hook slice
- Last verified state: `--gallery-index` appears in help, unit tests pass, a normal gallery-index smoke writes a temp index, and the committed batch smoke dry-run still avoids live API calls. Review found `--gallery-index --dry-run` writes an index file, which violates the current engine no-write dry-run contract.
- Files touched: `src\generate.py`, `tests\test_generate.py`, `README.md`, `RUN_MANIFEST.md`, `PLAN.md`, `TASKS.md`, `CHANGELOG.md`, `VERIFICATION.md`, `SIGN_UP.md`
- Verification run: `py .\src\generate.py --help`; `$env:PYTHONPATH=(Resolve-Path 'src').Path; py -B -m unittest discover -s tests`; `py .\src\generate.py --gallery-index --gallery-source assets\generated --gallery-output $env:TEMP\vaultforge-engine-gallery-index-review.json`; `py .\src\generate.py '@assets\batch-input-smoke\smoke.conf'`; `py .\src\generate.py --gallery-index --dry-run --gallery-source assets\generated --gallery-output $env:TEMP\vaultforge-engine-gallery-index-dry-run-conflict.json`
- Blocker or decision: No hard gate found. Blocking review finding remains inside the safe engine lane: guard the dry-run conflict before committing this slice.
- Resume prompt: Fix `--gallery-index --dry-run` by rejecting the flag combination or making it preview-only, add a regression test, rerun the unit tests plus gallery-index smoke, then reviewer can re-check and commit the scoped engine changes.

## 2026-05-09 - workflow b root recorder cycle 1 gallery guard handoff

- Role: Root recorder for Workflow B cycle 1
- Scope: affected section handoff note only
- Read: active run packet status/checkpoints, coordinator output, engine builder output, engine reviewer output, current engine `SIGN_UP.md`, current engine `TASKS.md`, and current git status/diff state
- Changed: recorded that the gallery-index hook is not closed because reviewer found `--gallery-index --dry-run` writes JSON despite the no-write dry-run contract
- Handoff: no hard gate is needed for this engine issue. The next safe engine slice is `engine-gallery-index-dry-run-guard`: reject the flag combination or make it preview-only, add a regression test, rerun unit tests and gallery-index smoke checks, then reviewer can commit scoped engine changes.

## 2026-05-09 - workflow b engine gallery dry-run guard

- Role: Builder for Workflow B cycle 1, engine lane
- Scope: section-local fix for `engine-gallery-index-dry-run-guard`
- Read: active run packet prompt, dirty baseline, `TASKS.md`, `SIGN_UP.md`, `VERIFICATION.md`, `RUN_MANIFEST.md`, `README.md`, `src\generate.py`, and `tests\test_generate.py`
- Changed: rejected `--gallery-index --dry-run` during argument validation, added a regression test, documented the no-write guard, and marked the gallery hook plus guard tasks complete after verification
- Handoff: reviewer should re-check the scoped diff, the unit suite, the rejected dry-run conflict, and the normal gallery-index smoke. No hard gate was found; contact-sheet rendering remains the next later engine gallery task.

## 2026-05-09 - workflow b engine gallery dry-run guard reviewer

- Role: Reviewer for Workflow B cycle 1, engine lane
- Scope: review the `engine-gallery-index-dry-run-guard` fix, regression test, docs, and verification evidence
- Read: builder output, scoped engine diff, `src\generate.py`, `tests\test_generate.py`, `README.md`, `RUN_MANIFEST.md`, `TASKS.md`, `CHANGELOG.md`, `VERIFICATION.md`, and active run packet status
- Changed: updated this reviewer handoff only
- Handoff: no blocking findings. Unit tests pass, `--gallery-index --dry-run` rejects without creating the requested JSON file, normal `--gallery-index` still writes an explicit index, and the committed batch smoke dry-run remains no-live/no-write. Recorder can capture the commit and continue only with another approved safe slice.

## 2026-05-09 - workflow b root recorder cycle 1 gallery guard closure

- Role: Root recorder for Workflow B cycle 1
- Scope: affected section handoff note only
- Read: active run packet output notes for root coordinator, engine builder, engine reviewer, business builder, and business reviewer; current engine `SIGN_UP.md`; current git status and recent commit log
- Changed: recorded that the engine gallery dry-run guard has passed reviewer checks and is already committed as `cd9a86d`
- Handoff: no engine hard gate remains for `engine-gallery-index-dry-run-guard`. The engine dry-run contract is now protected by rejecting `--gallery-index --dry-run`; normal explicit gallery-index output remains allowed. No live generation was run or approved in this recorder pass.

## 2026-05-09 - workflow b engine cycle 2 builder routing

- Role: Builder for Workflow B cycle 2, engine lane
- Scope: section-local docs/evidence only; no code change because the remaining contact-sheet renderer task requires real sidecar examples and `assets\generated` is currently empty
- Read: refreshed root workflow review guidance, cycle 2 root coordinator routing note, engine task board, `RUN_MANIFEST.md`, `VERIFICATION.md`, current dirty baseline, and current generator/gallery tests
- Changed: tagged `engine-contact-sheet-renderer` as `#live-required` to make the missing real sidecar examples explicit, and left the implementation slice for a later approved pass
- Handoff: no engine hard gate was triggered, but there is no approved engine implementation slice ready in this cycle. Reviewer can check the docs-only task tag plus verification: unit tests passed, smoke config dry-run stayed no-live/no-write, empty gallery-index smoke produced a zero-entry temp index, and `--gallery-index --dry-run` still rejects without creating output.

## 2026-05-09 - workflow b engine cycle 2 reviewer

- Role: Reviewer for Workflow B cycle 2, engine lane
- Scope: review the builder's docs-only routing decision for `engine-contact-sheet-renderer`
- Read: cycle 2 coordinator routing note, engine builder output, current engine diff, `TASKS.md`, `SIGN_UP.md`, `src\generate.py`, `VERIFICATION.md`, and current `assets\generated`
- Changed: recorded this reviewer handoff only
- Handoff: no blocking findings. The `#live-required` tag is appropriate because `assets\generated` has no real sidecar examples, the remaining contact-sheet renderer would otherwise depend on missing live/generated evidence, and the existing gallery dry-run guard still verifies. Unit tests passed, smoke config dry-run stayed no-write, normal empty gallery-index wrote only a temp zero-entry index, and `--gallery-index --dry-run` rejected without creating output.

## 2026-04-16 - engine task review

- Role: Task Master review for the engine section
- Scope: validate engine task priority, dependency order, and missing prerequisites against the current engine docs and compatibility notes
- Read: root startup docs, engine system/plan/tasks/changelog/sign-up docs, verification and compatibility notes, business follow-up tasks, and the current generator/wrapper state
- Changed: raised config-safe `@file.conf` review, added ongoing engine doc hygiene, added explicit manifest-contract and edit/reference-contract planning tasks, and re-linked gallery plus image-input work behind the right prerequisites
- Handoff: next engine work should settle config-safe testing and the shared metadata/edit contract before landing gallery hooks or native image-input/reference support

## 2026-04-15 - execution mode decision

- Role: engine runtime/planning follow-through
- Scope: decide whether engine threads should require an editable `.venv` or stay launcher-based for now
- Read: root startup docs, engine docs, current launcher/packaging files, business retarget notes
- Changed: kept launcher/direct-script execution as the current engine contract; updated `run_engine.bat` to use a local `.venv` only when one already exists
- Handoff: next engine task can stay focused on dry-run safety and future image-input/edit API work without assuming a dedicated engine install step

## 2026-04-13 - section setup

- Role: documentation setup for dedicated engine threads
- Scope: section docs, root handoff, and startup requirements
- Read: root `CODEX_START.md`, root `THREAD_MAP.md`, engine docs, Nath notes
- Changed: engine docs now point new threads through root overhead first
- Handoff: next engine thread should handle the engine-specific step 7 task from the business notes

## 2026-04-13 - engine step 7

- Role: first dedicated engine worker thread
- Scope: engine-native business handoff flags and shared generator verification
- Read: root startup docs, root thread map, engine docs, Nath notes, business step 7 note
- Changed: added and verified `--client`, `--job`, `--tag`, and `--variants` in `src\generate.py`
- Handoff: root/business notes can mark business step 7 complete; edit/reference image APIs remain a later engine task
