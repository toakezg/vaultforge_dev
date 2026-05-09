# Workflow B Cancel Handoff

- Cancelled: `2026-05-09T22:49:44+10:00`
- Run id: `direct-escape-hatch-test`
- Cycle: `1` of `1`
- Active agent: root-coordinator (lane `root`, role `coordinator`, workdir `F:\vaultforge`)
- Reason: operator requested cancellation with Ctrl+C or batch termination.
- Escape hatch workflow: `F:\toakezg\workflows\esape-hatch.md`

## Escape Hatch Summary

Stop reason:
: operator cancellation / manual interrupt

Active workflow:
: VaultForge Workflow B running Workflow A-style lane agents

Current stage:
: cycle 1 of 1, active agent root-coordinator

Completed:
: Review `checkpoints.jsonl` and `status.jsonl` for all `agent_finished`,
  `cycle_finished`, and verification records before the cancellation point.

Partial or uncertain:
: The active agent and any outputs without a matching final signal block should
  be treated as partial or uncertain.

Changed files/artifacts:

```text
M CHANGELOG.md
 M MULTI_AGENT_WORKFLOW_B.md
 M TASKS.md
 M WORKFLOW_REVIEW.md
 M vaultforge-business/SIGN_UP.md
 M vaultforge-engine/SIGN_UP.md
 M workflow_b.md
 M workflow_b_controller.py
```

Run artifacts:

[no run artifacts found]

Commands/checks already run:
: The controller command is represented by `workflow-b-plan.md`; agent-level
  checks are recorded in each `cycle-XX/outputs/*.last-message.md` file when
  the agent completed cleanly.

Known errors or risks:
: Cancellation may leave the active lane with partial edits or no final
  `WORKFLOW_B_*` signal block. Do not assume the active agent completed.

Do not repeat without checking:
: Do not rerun the same lane slice blindly until the run packet, dirty git
  status, and active agent output are reviewed.

Recommended resume workflow:
: Esape Hatch verification cycle, then Workflow B with a narrower task if the
  interrupted lane is clean enough to continue.

First next action:
: Inspect this handoff, `workflow-b-live-status.md`, `checkpoints.jsonl`, and
  `status.jsonl`; then check the active lane's git diff before continuing.

Verification before continuing:
: Confirm whether the active agent produced a final message and whether any
  changed files are complete, incomplete, uncertain, or unsafe to repeat.

## What To Review

- `workflow-b-live-status.md`
- `checkpoints.jsonl`
- `status.jsonl`
- latest `cycle-XX/outputs/*.last-message.md` files
- any changed files from the active lane before resuming

## Budget Snapshot

```json
{
  "elapsed_seconds": 0.1,
  "elapsed_minutes": 0.002,
  "timebox_minutes": 20,
  "remaining_minutes": 19.998,
  "timebox_used_percent": 0.01,
  "usage_budget_usd": 1,
  "estimated_agent_usd": 0.08,
  "agent_runs_started": 0,
  "estimated_usage_usd": 0.0,
  "reported_usage_usd": 0.0,
  "remaining_estimated_usage_usd": 1.0,
  "estimated_usage_used_percent": 0.0
}
```

## Resume Shape

Start a fresh run after reviewing the partial outputs:

```bat
run_workflow_b_watch.bat --cycles 1 --lane root --timebox-minutes 20 --usage-budget-usd 1 --estimated-agent-usd 0.08 --hard-gate-mode switch-safe --commit-mode review --task "Verify escape hatch handoff template"
```

Do not use `--force-unlock` unless `.workflow-b.lock` remains and no Workflow B
Python process is active.
