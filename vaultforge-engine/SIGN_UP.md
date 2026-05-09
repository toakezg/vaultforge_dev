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
