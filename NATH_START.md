# NATH START - VaultForge Last 12 Hours

Reviewed at: 2026-05-10 02:10 +10:00

Window reviewed: roughly the last 12 hours from the local machine clock.

## Quick Read

The last 12 hours were mostly about making Workflow B real enough to use for
bounded multi-agent VaultForge work. The repo now has a long-run controller,
cycle packets, checkpoint logs, timebox and usage-budget controls, hard-gate
handling, cancellation handoffs, workflow-review refreshes, and reviewed
section work across engine, business, icon, and XP4L.

The strongest new thing to try is Workflow B in a small bounded run, but keep
the current resume-command caveat in mind: generated resume commands have been
recorded as missing `--execute`, `--commit-mode review`, and
`--hard-gate-mode switch-safe`, so add those manually for executable runs until
task `root-workflow-b-resume-execute-flag` is fixed.

## Watch-outs First

- Root currently has uncommitted recorder/doc edits in `CHANGELOG.md`,
  `WORKFLOW_REVIEW.md`, and `vaultforge-business/SIGN_UP.md`.
- `vaultforge-xp4l` is dirty inside its own repo: `CHANGELOG.md`, `README.md`,
  `SIGN_UP.md`, `TASKS.md`, and untracked `VAULT_OUTPUT_SHAPE.md`.
- `.workflow-b.lock` showed as deleted in root status during review. Treat lock
  state carefully before starting another run.
- A few ignored or local Obsidian files changed by timestamp, especially
  `.obsidian/workspace.json`; those did not show as the main tracked source
  changes in root status.
- Some `.tmp_tests` and icon wrapper temp folders return permission-denied
  warnings during recursive scans. This looks like existing local Windows
  permission state, not a fresh source-code failure.
- No live generation, paid/API generation, publication, pricing, licensing,
  asset move/delete, or shared engine registry migration was approved by the
  reviewed Workflow B notes.

## What Changed

### Workflow B Became A Working Long-run Controller

New and updated surfaces:

- `MULTI_AGENT_WORKFLOW_B.md`
- `workflow_b_controller.py`
- `workflow_b.md`
- `run_workflow_b.bat`
- `run_workflow_b_watch.bat`
- `WORKFLOW_REVIEW.md`
- `runs/workflow-b/...`
- `runs/workflow-b-verify/...`

Important behavior now exists:

- cycle packets with per-agent prompts
- optional `codex exec` execution
- review-mode commits
- lock file handling through `.workflow-b.lock`
- watched workflow docs
- `WORKFLOW_REVIEW.md` controller snapshots
- `status.jsonl`
- `checkpoints.jsonl`
- `workflow-b-live-status.md`
- budget and timebox stop handoffs
- Ctrl+C cancellation handoff files
- hard-gate modes: `stop`, `switch-safe`, and `record-continue`
- final signal parsing from spawned agents

Safe thing to try:

```powershell
.\run_workflow_b.bat --cycles 1 --lane vaultforge-business --task "Prepare the next safe business-local docs-only slice"
```

That prepares a plan packet only. It should not launch agents unless
`--execute` is added.

Small executable example:

```powershell
.\run_workflow_b_watch.bat --cycles 1 --timebox-minutes 20 --usage-budget-usd 1.00 --estimated-agent-usd 0.08 --hard-gate-mode switch-safe --lane vaultforge-business --execute --bypass-sandbox --commit-mode review --task "Prepare the Nath-facing paid launch decision note as docs only; do not approve pricing, licensing, publication, live generation, paid/API work, asset moves, fragment migration, or engine registry changes"
```

Use the watch launcher when you want the terminal to stay open and show a more
operator-facing exit summary.

### Business Lane Got Much More Client-ready

Recent reviewed business work added or tightened:

- client-ready criteria
- non-runnable client intake template
- delivery package skeleton
- internal service catalog
- output review checklist
- operator-facing `vaultforge-business/NATH_START.md`
- corrected pack-preview examples using PowerShell execution-policy bypass
- safer `-WhatIf` and dry-run verification notes

Best files to look at:

- `vaultforge-business/NATH_START.md`
- `vaultforge-business/BUSINESS_CLIENT_READY_CRITERIA.md`
- `vaultforge-business/BUSINESS_SERVICE_CATALOG.md`
- `vaultforge-business/BUSINESS_OUTPUT_REVIEW_CHECKLIST.md`
- `vaultforge-business/delivery-package-template/`
- `vaultforge-business/my-prompts-bank/_intake/client-intake-template.md`

Safe examples:

```powershell
cd .\vaultforge-business
.\run_business.ps1 -Prompt "Clean local service logo with simple symbol" -Client "demo-client" -AssetType "logo" -Job "first-pass" -Tag "local,premium" -WhatIf
```

```powershell
cd .\vaultforge-business
.\run_business_md_bank.ps1 -Path ".\my-prompts-bank" -IncludeTemplates -WhatIf -Limit 1
```

```powershell
cd .\vaultforge-business
powershell -ExecutionPolicy Bypass -File .\run-client-pack.ps1 -InputValue "Demo Client" -Client "demo-client" -Project "logo-pack-01" -Tag "round1" -PromptFile ".\logo-pack.txt" -WhatIf
```

Next useful thing to look at:

- write the Nath-facing paid launch decision note, but keep actual pricing,
  licensing, publication, live generation, paid/API use, asset moves, fragment
  migration, and engine registry changes gated until explicitly approved.

### Engine Lane Is Safer Around Dry-runs

Recent engine work and verification focused on no-write safety and evidence:

- `.env` API-key loading and lane override flags landed earlier in the window
- direct `--input-image` and `--reference-image` support is documented as added
- gallery-index dry-run guard was fixed so `--gallery-index --dry-run` rejects
- normal explicit gallery-index output remains allowed
- smoke config dry-runs stayed no-live/no-write
- contact-sheet renderer remains parked as `#live-required`

Best files to look at:

- `vaultforge-engine/VERIFICATION.md`
- `vaultforge-engine/SIGN_UP.md`
- `vaultforge-engine/RUN_MANIFEST.md`
- `vaultforge-engine/TASKS.md`

Safe examples:

```powershell
cd .\vaultforge-engine
py -B -m unittest discover -s tests
```

```powershell
cd .\vaultforge-engine
py .\src\generate.py '@assets\batch-input-smoke\smoke.conf'
```

```powershell
cd .\vaultforge-engine
py .\src\generate.py "A clean geometric VaultForge test icon" --preset icon --style geometric --client "Demo Client" --job "dry-run-test" --tag "safe" --variants 2 --dry-run
```

Do not treat the contact-sheet renderer as ready. It is intentionally blocked
until there are real sidecar examples or a root-approved fixture strategy.

### XP4L Got Clearer Boundaries

XP4L received several docs-only alignment passes:

- `ENGINE_BOUNDARIES.md`
- `OUTPUT_CONTRACT.md`
- `XP_RULES_SURFACE.md`
- `HEURISTIC_BOUNDARIES.md`
- `VERIFICATION_CRITERIA.md`
- `VAULT_OUTPUT_SHAPE.md` currently appears untracked/dirty in the nested repo

The work clarifies:

- XP4L owns interpretation after the neutral event contract
- XP4L does not own upstream execution claims
- rules, heuristics, rarity, output shape, and vault materialization are
  separate surfaces
- live vault writes to XP4Life remain gated
- scoring values, parser behavior, event-contract changes, and persistent
  progression design changes remain gated

Best files to look at:

- `vaultforge-xp4l/VAULT_OUTPUT_SHAPE.md`
- `vaultforge-xp4l/XP_RULES_SURFACE.md`
- `vaultforge-xp4l/HEURISTIC_BOUNDARIES.md`
- `vaultforge-xp4l/VERIFICATION_CRITERIA.md`

Safe examples:

```powershell
cd .\vaultforge-xp4l
python -m unittest discover -s tests -v
```

Safe review path before any live XP4Life write:

```text
1. Put adapter-formatted JSON in the selected .4/inbox path.
2. Run XP4L with --dot4-inbox, --vault-root, --state-path, and --dry-run.
3. Inspect dot4_intake, progression, obsidian_output, and result.
4. Only rerun without --dry-run after accepting the preview.
```

### Icon Lane Stayed Gated

Icon work mostly resolved a proposal decision without generation:

- `vaultforge-icon/documents/decisions/MEDIA_STYLE_PROPOSAL_STATUS_GATE.md`
  records that the media style guide remains inactive/reference-only
- `run_icon_proposal.ps1` was not run
- no paid/API proposal generation was approved
- no generated media proposal output folder was created
- no selected/applied output, asset operation, folder icon application, or
  cross-lane ownership change was approved

Best file to look at:

- `vaultforge-icon/documents/decisions/MEDIA_STYLE_PROPOSAL_STATUS_GATE.md`

Safe next action:

```text
Review whether the media style guide should stay inactive or become active in a
future approved task. Do not run proposal generation until that decision is
explicit.
```

## Commit Timeline

Recent root commits in the reviewed window:

- `edac1b9` - added Workflow B controller files and workflow docs
- `cf95750` - engine no-write preview work
- `2279fcb` - business pack `-WhatIf` logging
- `cd9a86d` - engine gallery dry-run guard
- `e89fe60` - business client-ready docs
- `ecb36c2` - engine contact sheet live gate
- `ac4ec51` - business client intake template
- `d574b8c` - business delivery package skeleton
- `4145e8e` - engine live-required gate
- `1e4c87e` - budget, gates, timebox, checkpoint docs
- `a7e92e3` and `d400135` - engine verification/evidence cycles
- `afabeb0` - icon media style inactive decision
- `47a6806` - lane batch: engine, business, icon, XP4L
- `da7301f` - business `NATH_START.md` reviewed and committed
- `397506b` - root recorder note for engine verification and XP4L output shape

Nested `vaultforge-xp4l` commits in the same window include:

- `e0b76bf` - engine boundaries
- `ef5c6a6` - verification criteria
- `ba8b31d` - event contract task cleanup
- `9c0dfa2` - output contract
- `cdb65e6` - XP rules surface
- `4cb82fc` - heuristic boundaries

## New Things Worth Trying

### 1. Try a one-cycle Workflow B dry plan

Use this when you want to inspect the generated packet before letting agents
run.

```powershell
.\run_workflow_b.bat --cycles 1 --lane vaultforge-business --task "Plan the next safe business-local docs-only improvement"
```

Then inspect:

```powershell
Get-ChildItem .\runs\workflow-b | Sort-Object LastWriteTime -Descending | Select-Object -First 1
```

Look inside the newest packet for:

- `workflow-b-plan.md`
- `workflow-b-plan.json`
- `cycle-01/*.prompt.md`

### 2. Try a tiny executable business docs run

Use this only if the lock state is clear and you are comfortable launching
Codex CLI agents.

```powershell
.\run_workflow_b_watch.bat --cycles 1 --timebox-minutes 20 --usage-budget-usd 1.00 --estimated-agent-usd 0.08 --hard-gate-mode switch-safe --lane vaultforge-business --execute --bypass-sandbox --commit-mode review --task "Create a docs-only Nath paid-launch decision note. Do not approve or change pricing, licensing, publication, live generation, paid/API use, assets, fragment migration, or engine registry ownership."
```

### 3. Inspect the latest run status without reconstructing chat

```powershell
Get-Content .\runs\workflow-b\20260510T015750-use-multiagents-to-perform-a-clean-up-of-documen\workflow-b-live-status.md
```

```powershell
Get-Content .\runs\workflow-b\20260510T015750-use-multiagents-to-perform-a-clean-up-of-documen\checkpoints.jsonl -Tail 20
```

### 4. Re-check root and nested repo dirt before another run

```powershell
git status --short
git -C .\vaultforge-xp4l status --short
```

### 5. Review business as an actual client lane

```powershell
cd .\vaultforge-business
Get-Content .\NATH_START.md
Get-Content .\BUSINESS_CLIENT_READY_CRITERIA.md
Get-Content .\BUSINESS_OUTPUT_REVIEW_CHECKLIST.md
```

The key question to answer next is not "can this generate cool output?" It is:

```text
Can this reliably turn a client request into a reviewed delivery package?
```

### 6. Review XP4L output before live vault writes

```powershell
cd .\vaultforge-xp4l
Get-Content .\VAULT_OUTPUT_SHAPE.md
python -m unittest discover -s tests -v
```

Focus on whether the dry-run preview shape is good enough before anything
touches `E:\XP4Life`.

## Best Next Moves

1. Fix `root-workflow-b-resume-execute-flag` so generated resume commands are
   not missing the flags needed for real executable review-mode continuation.
2. Decide whether to commit or cleanly record the current root recorder edits
   and the nested XP4L dirty files before starting another long run.
3. Continue business with the Nath-facing paid launch decision note as a
   decision surface only, not an approval to sell or publish.
4. Keep engine contact-sheet rendering parked until real sidecar examples or a
   fixture strategy are approved.
5. Keep icon media-style proposal generation inactive until Nath explicitly
   activates that source note for generation.
