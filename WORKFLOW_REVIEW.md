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
- Time and estimated usage budgets should be set on long runs when Nath wants a
  bounded session, such as a 2-hour work block.
- Hard gate mode should be explicit for unattended-ish runs. Default is
  `switch-safe`.
- Agents should treat this note as guidance, not permission to bypass
  `THREAD_MAP.md`, lane ownership, or decision gates.

## Watched Workflow Inputs

- `MULTI_AGENT_WORKFLOW.md`
- `MULTI_AGENT_WORKFLOW_B.md`
- `WORKFLOW_REVIEW.md`
- `THREAD_MAP.md`
- `TASKS.md`
- `business-if-done.txt` as business-lane direction when present
- `F:\toakezg\workflows\workflow-types.md` when it exists

## Review Questions

- Did the last cycle start from current root and section docs?
- Was the task routed to the right lane?
- Did each agent stay inside its write scope?
- Did reviewers verify real behavior or only restate intent?
- Did commit policy avoid pre-existing dirty files?
- Did any workflow change appear mid-run, and was it included in the next
  prompt?
- For business-lane work, did the agent check `business-if-done.txt` without
  treating it as a blank approval for broad changes?
- Did the run stay inside its time and estimated usage budgets?
- If a hard gate appeared, did the selected hard-gate mode handle it correctly?

<!-- workflow-b-controller-snapshot:start -->
## Controller Review Snapshot

- Updated: `2026-05-09T23:52:11+10:00`
- Reason: cycle review cadence
- Run id: `20260509T235211-run-approved-section-local-build-slices-while-an`
- Cycle: `1` of `8`
- Run packet: `F:\vaultforge\runs\workflow-b\20260509T235211-run-approved-section-local-build-slices-while-an`
- Commit mode: `review`
- Timebox minutes: `20.0`
- Usage budget USD: `1.0`
- Hard gate mode: `switch-safe`
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









## Multi-Agent Handoff

- Task: Workflow B cycle 1 recorder closure for run `20260509T233547-run-approved-section-local-build-slices-while-an`
- Current role: root recorder
- Last verified state: controller created the run packet, refreshed the workflow review snapshot, produced six cycle prompts, and reached the root recorder slot. Status and checkpoint streams are readable. No watched workflow document changes were detected before the cycle. Root coordinator reported a hard gate and `switch-safe` continued to scoped safe work. Engine reviewer committed live-required contact-sheet gate evidence as `a50bc48`. Business reviewer committed the delivery package skeleton as `d574b8c`.
- Files touched: root `CHANGELOG.md`, root `WORKFLOW_REVIEW.md`, `vaultforge-engine/SIGN_UP.md`, and `vaultforge-business/SIGN_UP.md` by this recorder pass. Cycle commits also touched `vaultforge-engine/VERIFICATION.md` and business delivery package docs/template files.
- Verification run: inspected `workflow-b-plan.md`, `workflow-b-live-status.md`, `status.jsonl`, `checkpoints.jsonl`, all cycle output notes, `git status --short`, `git diff --stat`, `git show --stat a50bc48`, `git show --stat d574b8c`, and `git log --oneline -8`.
- Blocker or decision: hard gate remains recorded for moving business fragments into shared engine registries because that changes engine/business ownership and registry shape. Engine contact-sheet rendering remains `#live-required` until real sidecar examples or a root-approved fixture strategy exists. No live generation was run or approved.
- Resume prompt: continue Workflow B with a safe business-local builder slice such as `business-service-catalog` or `business-client-output-review-checklist`; keep `business-fragment-library-ownership-gate`, pricing/licensing/publication, live generation, and engine contact-sheet rendering gated until their approvals or evidence exist, and include `--execute` manually if resuming from the generated command before `root-workflow-b-resume-execute-flag` is fixed.










