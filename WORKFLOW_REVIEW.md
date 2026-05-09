# VaultForge Workflow Review

This note is the root review surface for Workflow A and Workflow B.

It exists so long-running Workflow B runs have one short place to check whether
the workflow itself is still behaving well.

## Imported Lessons From Workflow Types

- Router-Triage should be the front door for vague or mixed work. Classify
  tasks by lane, risk, workflow type, and next action before sending agents out.
- Memory-Context Refresh should happen at the start of each cycle. Agents should
  reread current root/section docs, current dirty state, and handoff notes
  instead of relying only on cycle 1 context.
- Planner-Executor-Verifier is the default lane pattern for actual build work:
  inspect, plan, execute, verify, then narrow-fix if needed.
- Parallel Specialist Review fits review-heavy steps where multiple risk lenses
  matter, such as tests, contracts, scope drift, and operator workflow.
- Sequential Builder-Critic Loop fits docs, specs, prompt packs, and quality
  improvement over a small number of passes.
- Test-Driven Agent Loop fits code, CLIs, parsers, and repeatable behavior
  where checks can control the loop.
- Human-In-The-Loop Approval remains the hard gate for destructive, external,
  paid, secret, live, asset-moving, or taste-heavy decisions.

## Workflow B Review Cadence

- The controller updates the snapshot block every `--workflow-review-every`
  cycles. Default: every 2 cycles.
- The controller also updates this note when watched workflow docs change.
- Agents should treat this note as guidance, not permission to bypass
  `THREAD_MAP.md`, lane ownership, or decision gates.

## Watched Workflow Inputs

- `MULTI_AGENT_WORKFLOW.md`
- `MULTI_AGENT_WORKFLOW_B.md`
- `WORKFLOW_REVIEW.md`
- `THREAD_MAP.md`
- `TASKS.md`
- `F:\toakezg\workflows\workflow-types.md` when it exists

## Review Questions

- Did the last cycle start from current root and section docs?
- Was the task routed to the right lane?
- Did each agent stay inside its write scope?
- Did reviewers verify real behavior or only restate intent?
- Did commit policy avoid pre-existing dirty files?
- Did any workflow change appear mid-run, and was it included in the next
  prompt?

<!-- workflow-b-controller-snapshot:start -->
## Controller Review Snapshot

- Updated: `2026-05-09T21:07:50+10:00`
- Reason: cycle review cadence
- Run id: `20260509T210750-verify-workflow-review-watcher-self-update-suppr`
- Cycle: `2` of `2`
- Run packet: `F:\vaultforge\runs\workflow-b-verify\20260509T210750-verify-workflow-review-watcher-self-update-suppr`
- Commit mode: `review`
- Watched workflow changes this cycle:
- none detected

## Current Workflow Lessons

- Use Router-Triage at the front of mixed or vague long-run tasks.
- Use Memory-Context Refresh at the start of each cycle so agents respect current docs and dirty state.
- Use Planner-Executor-Verifier as the default build lane pattern.
- Use Parallel Specialist Review when review needs multiple risk lenses.
- Use Test-Driven Agent Loop for code or CLI behavior with concrete checks.
- Use Human-In-The-Loop gates for destructive, external, paid, secret, or taste-heavy decisions.
- Keep Workflow B adaptive by refreshing workflow docs between cycles rather than freezing the first prompt forever.
<!-- workflow-b-controller-snapshot:end -->




