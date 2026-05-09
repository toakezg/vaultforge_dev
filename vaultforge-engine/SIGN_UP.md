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

## Multi-Agent Handoff

- Task: Run approved section-local build slices
- Current role: Reviewer passed engine no-write preview slice
- Last verified state: reviewer reran `py .\src\generate.py --help`, unit tests, and the committed smoke config dry-run. The smoke config printed two output paths and two metadata paths, made no API call, left `assets\generated` empty, and did not create `assets\batch-input-smoke\.batch-state.json`.
- Files touched: `PLAN.md`, `TASKS.md`, `CHANGELOG.md`, `VERIFICATION.md`, `SIGN_UP.md`
- Verification run: `py .\src\generate.py --help`; `$env:PYTHONPATH=(Resolve-Path 'src').Path; py -B -m unittest discover -s tests`; `py .\src\generate.py '@assets\batch-input-smoke\smoke.conf'`; checked `assets\generated` and `assets\batch-input-smoke\.batch-state.json` before and after the dry-run command
- Blocker or decision: No hard gate found. `--dry-run` remains the engine's no-write preview path; no separate preview flag is needed until a lane wrapper proves a different behavior is required.
- Resume prompt: Continue Workflow B with the next approved safe slice. For engine, `engine-gallery-hooks` remains the next later task and should start only after reading `RUN_MANIFEST.md`, current `TASKS.md`, and this reviewer handoff.

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
