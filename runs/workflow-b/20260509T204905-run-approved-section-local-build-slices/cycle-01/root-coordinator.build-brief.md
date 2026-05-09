# Root Coordinator Build Brief

- Run: `20260509T204905-run-approved-section-local-build-slices`
- Cycle: 1 of 7
- Role: root coordinator
- Target sections: `vaultforge-engine`, then `vaultforge-business`
- Write scope used by coordinator: active Workflow B run packet only

## Understanding

Workflow B is running with sequential agents. Root coordinates and records the
route; section builders and reviewers own section-local implementation and
verification. The controller already generated all cycle prompts at cycle start,
so later agents should inspect live section docs and diffs instead of trusting
only the embedded snapshots.

## Approved Slice Route

1. `vaultforge-engine` reviewer should run first.
   - Live handoff in `vaultforge-engine/SIGN_UP.md` says the engine builder
     slice is complete and ready for review.
   - Review focus: `assets/batch-input-smoke/smoke.conf`,
     `tests/fixtures/smoke-reference.svg`, `RUN_MANIFEST.md`, `README.md`,
     `VERIFICATION.md`, `PLAN.md`, `TASKS.md`, `CHANGELOG.md`, and
     `SIGN_UP.md`.
   - Verification requested by the handoff: `py .\src\generate.py --help`,
     `$env:PYTHONPATH=(Resolve-Path 'src').Path; py -B -m unittest discover -s tests`,
     and `py .\src\generate.py '@assets\batch-input-smoke\smoke.conf'`.

2. `vaultforge-business` builder may retry after the engine reviewer only if
   live shell reads work in that section.
   - Existing `vaultforge-business/SIGN_UP.md` entry records a prior hard gate
     from `windows sandbox: CryptUnprotectData failed: 2148073483`.
   - This coordinator turn could read via PowerShell from root, so the next
     business builder should verify from its own workdir with `git status --short`,
     `Get-Content .\run_business.ps1`, and
     `Get-Content ..\vaultforge-engine\src\generate.py`.
   - Approved first business task remains
     `business-engine-native-metadata-adoption`; if reads fail again, record the
     hard gate and do not edit wrapper behavior from snapshots.

3. Root recorder should capture factual results only.
   - Include files touched, commands run, blockers, and the next resume prompt.
   - Do not infer section success where a builder or reviewer did not verify it.

## Gates

- No new root hard gate found by this coordinator pass.
- Soft risk: cycle prompts were generated before later live section handoffs, so
  every downstream role should start from live files.
- Root should not move, delete, or rewrite unrelated files in this cycle.

## Evidence

- Read run plan: `workflow-b-plan.md`, `workflow-b-plan.json`, `status.jsonl`.
- Read active handoffs: `vaultforge-engine/SIGN_UP.md`,
  `vaultforge-business/SIGN_UP.md`.
- Read active task boards: `vaultforge-engine/TASKS.md`,
  `vaultforge-business/TASKS.md`.
- Checked controller behavior and active lock: `.workflow-b.lock`.
- Checked dirty tree with `git status --short`; unrelated deletes and Obsidian
  state changes already exist and were left untouched.

## Next Prompt

Continue Workflow B cycle 1 as `vaultforge-engine-reviewer`. Read the live
`vaultforge-engine/SIGN_UP.md` handoff and inspect the current engine diff before
reviewing. Rerun the requested verification commands, lead with findings and
file/line references where possible, then hand off to the business builder or
root recorder according to the result.
