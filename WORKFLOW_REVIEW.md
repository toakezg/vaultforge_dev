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

- Updated: `2026-05-10T01:57:50+10:00`
- Reason: cycle review cadence
- Run id: `20260510T015750-use-multiagents-to-perform-a-clean-up-of-documen`
- Cycle: `1` of `8`
- Run packet: `F:\vaultforge\runs\workflow-b\20260510T015750-use-multiagents-to-perform-a-clean-up-of-documen`
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

- Task: Workflow B cycle 2 recorder closure for run `20260510T005905-run-approved-section-local-build-slices-while-an`
- Current role: root recorder
- Last verified state: controller reached the cycle 2 root-recorder slot after detecting changed `WORKFLOW_REVIEW.md`, refreshing prompts, and producing four cycle 2 prompts. Status and checkpoint streams are readable. Root coordinator recorded no hard gate and routed the safe slice to `vaultforge-xp4l` for docs-only heuristic-boundary documentation. XP4L builder added the section-local heuristic-boundaries note. XP4L reviewer found no blocking issues, reran the XP4L checks, and committed the reviewed XP4L section change as `4cb82fc`.
- Files touched: root `CHANGELOG.md`, root `WORKFLOW_REVIEW.md`, and `vaultforge-xp4l/SIGN_UP.md` by this recorder pass. Cycle work also touched `vaultforge-xp4l/HEURISTIC_BOUNDARIES.md`, `README.md`, `ENGINE_BOUNDARIES.md`, `XP_RULES_SURFACE.md`, `VERIFICATION_CRITERIA.md`, `TASKS.md`, `CHANGELOG.md`, and `SIGN_UP.md` in XP4L commit `4cb82fc`, plus the run-packet outputs `root-coordinator-routing.md` and `vaultforge-xp4l-reviewer-review.md`.
- Verification run: inspected `workflow-b-live-status.md`, `status.jsonl`, `checkpoints.jsonl`, cycle 2 output notes, `root-coordinator-routing.md`, `vaultforge-xp4l-builder.last-message.md`, `vaultforge-xp4l-reviewer-review.md`, root `git status --short`, XP4L `git status --short`, XP4L `git log -1 --oneline`, XP4L `git show --stat --name-only -1`, XP4L `SIGN_UP.md`, and root `CHANGELOG.md`. Reviewer verification passed `python -m unittest discover -s tests -v` with 21 tests OK.
- Blocker or decision: no hard gate was recorded for this cycle. No runtime behavior change, live `E:\XP4Life` write, scoring value/config change, event-contract/source change, parser behavior change, fixture/test change, persistent progression design change, paid/API work, or cross-lane ownership change was run or approved. No `.workflow-b.lock` existed at recorder verification time. The generated resume command still omits `--execute`, `--commit-mode review`, and `--hard-gate-mode switch-safe`, so executable resumes should add them manually until `root-workflow-b-resume-execute-flag` is fixed.
- Resume prompt: continue Workflow B with vault-output-shape alignment or a narrow XP4L coverage gap, after checking remaining timebox and estimated usage. Keep live vault writes, XP scoring semantics and values, event-contract/source changes, parser behavior changes, fixture/test changes, persistent progression design changes, paid/API work, and cross-lane ownership changes gated unless Nath explicitly approves them. Executable resumes should add `--execute --commit-mode review --hard-gate-mode switch-safe` manually.

## Multi-Agent Handoff

- Task: Workflow B cycle 2 recorder closure for run `20260510T005900-run-approved-section-local-build-slices-while-an`
- Current role: root recorder
- Last verified state: controller reached the cycle 2 root-recorder slot after detecting changed `WORKFLOW_REVIEW.md`, refreshing prompts, and producing four cycle 2 prompts. Status and checkpoint streams are readable. Root coordinator recorded no hard gate and safe-switched the generated engine slot to evidence-only because no approved engine implementation slice remained. Engine builder and reviewer kept `engine-contact-sheet-renderer` parked as `#live-required`; reviewer found no blocking issues and made no commit because engine docs were already dirty with mixed pre-existing Workflow B entries.
- Files touched: root `CHANGELOG.md`, root `WORKFLOW_REVIEW.md`, and `vaultforge-engine/SIGN_UP.md` by this recorder pass. Cycle work also touched `vaultforge-engine/SIGN_UP.md`, `vaultforge-engine/VERIFICATION.md`, and the run-packet outputs `root-coordinator-routing.md` and `vaultforge-engine-reviewer-review.md`.
- Verification run: inspected `workflow-b-plan.md`, `workflow-b-live-status.md`, `status.jsonl`, `checkpoints.jsonl`, cycle 2 output notes, `root-coordinator-routing.md`, `vaultforge-engine-builder.last-message.md`, `vaultforge-engine-reviewer-review.md`, root `git status --short`, engine `SIGN_UP.md`, and root `CHANGELOG.md`. Reviewer verification passed `py -B -m unittest discover -s tests` with 24 tests OK, the smoke config dry-run stayed no-live/no-write, normal empty gallery-index wrote only an explicitly requested temp zero-entry JSON, and `--gallery-index --dry-run` rejected with exit code 2 without creating output.
- Blocker or decision: no hard gate was recorded for this cycle. The contact-sheet renderer remains `#live-required` until real sidecar examples or a root-approved contact-sheet fixture strategy exists. No live generation, generated art, renderer implementation, fixture-policy decision, paid/API work, or cross-lane ownership change was run or approved. No `.workflow-b.lock` existed at recorder verification time. The generated resume command still omits `--execute`, `--commit-mode review`, and `--hard-gate-mode switch-safe`, so executable resumes should add them manually until `root-workflow-b-resume-execute-flag` is fixed. Productive next work should route to that root resume-command task or to another already scoped safe lane.
- Resume prompt: continue Workflow B with a root-capable pass on `root-workflow-b-resume-execute-flag`, or select another approved docs-only/dry-run/build slice. If engine remains selected, keep contact-sheet rendering parked unless real sidecar examples exist or Nath approves a fixture strategy. Executable resumes should add `--execute --commit-mode review --hard-gate-mode switch-safe` manually.

## Multi-Agent Handoff

- Task: Workflow B cycle 1 recorder closure for run `20260510T005905-run-approved-section-local-build-slices-while-an`
- Current role: root recorder
- Last verified state: controller reached the cycle 1 root-recorder slot after creating an executable review-mode plan, updating the workflow review snapshot, and producing four cycle 1 prompts. Status and checkpoint streams are readable. Root coordinator recorded no hard gate and routed the safe slice to `vaultforge-xp4l` for docs-only rules-surface consolidation. XP4L builder added the section-local rules-surface note. XP4L reviewer found no blocking issues, ran the XP4L checks, and committed the reviewed XP4L section change as `cdb65e6`.
- Files touched: root `CHANGELOG.md`, root `WORKFLOW_REVIEW.md`, and `vaultforge-xp4l/SIGN_UP.md` by this recorder pass. Cycle work also touched `vaultforge-xp4l/XP_RULES_SURFACE.md`, `README.md`, `ENGINE_BOUNDARIES.md`, `VERIFICATION_CRITERIA.md`, `TASKS.md`, `CHANGELOG.md`, and `SIGN_UP.md` in XP4L commit `cdb65e6`, plus the run-packet outputs `root-coordinator-routing.md` and `vaultforge-xp4l-reviewer-review.md`.
- Verification run: inspected `workflow-b-plan.md`, `workflow-b-live-status.md`, `status.jsonl`, `checkpoints.jsonl`, cycle 1 output notes, `root-coordinator-routing.md`, `vaultforge-xp4l-builder.last-message.md`, `vaultforge-xp4l-reviewer-review.md`, root `git status --short`, XP4L `git status --short`, XP4L `git show --stat --name-only cdb65e6`, XP4L `TASKS.md`, XP4L `SIGN_UP.md`, and XP4L `CHANGELOG.md`. Reviewer verification passed `python -m unittest discover -s tests -v` with 21 tests OK.
- Blocker or decision: no hard gate was recorded for this cycle. No runtime behavior change, live `E:\XP4Life` write, scoring value/config change, event-contract/source change, parser behavior change, fixture/test change, persistent progression design change, paid/API work, or cross-lane ownership change was run or approved. No `.workflow-b.lock` existed at recorder verification time. The generated resume command still omits `--execute`, `--commit-mode review`, and `--hard-gate-mode switch-safe`, so executable resumes should add them manually until `root-workflow-b-resume-execute-flag` is fixed.
- Resume prompt: continue Workflow B with heuristic-boundary documentation, vault-output-shape alignment, or narrow coverage gaps. Keep live vault writes, XP scoring semantics and values, event-contract/source changes, persistent progression design changes, paid/API work, and cross-lane ownership changes gated unless Nath explicitly approves them. Executable resumes should add `--execute --commit-mode review --hard-gate-mode switch-safe` manually.

## Multi-Agent Handoff

- Task: Workflow B cycle 1 recorder closure for run `20260510T005900-run-approved-section-local-build-slices-while-an`
- Current role: root recorder
- Last verified state: controller reached the cycle 1 root-recorder slot after creating an executable review-mode plan, updating the workflow review snapshot, and producing four cycle 1 prompts. Status and checkpoint streams are readable. Root coordinator recorded no hard gate and routed the safe slice to `vaultforge-engine` as verification/evidence only. Engine builder recorded evidence only and left `engine-contact-sheet-renderer` parked as `#live-required`. Engine reviewer found no blocking issues, reran the engine checks, and committed the reviewed engine section change as `d400135`.
- Files touched: root `CHANGELOG.md`, root `WORKFLOW_REVIEW.md`, and `vaultforge-engine/SIGN_UP.md` by this recorder pass. Cycle work also touched `vaultforge-engine/SIGN_UP.md` and `vaultforge-engine/VERIFICATION.md` in engine commit `d400135`, plus the run-packet outputs `root-coordinator-routing.md` and `vaultforge-engine-reviewer-review.md`.
- Verification run: inspected `workflow-b-plan.md`, `workflow-b-live-status.md`, `status.jsonl`, `checkpoints.jsonl`, cycle 1 output notes, `root-coordinator-routing.md`, `vaultforge-engine-reviewer-review.md`, root `git status --short`, active `.workflow-b.lock`, engine `SIGN_UP.md`, `git show --stat --name-only d400135`, and root `CHANGELOG.md`. Reviewer verification passed `py -B -m unittest discover -s tests` with 24 tests OK, the committed smoke config dry-run stayed no-live/no-write, normal empty gallery-index wrote only an explicitly requested temp zero-entry JSON, and `--gallery-index --dry-run` rejected without creating output.
- Blocker or decision: no hard gate was recorded for this cycle. The contact-sheet renderer remains `#live-required` until real sidecar examples or a root-approved contact-sheet fixture strategy exists. No live generation, generated art, renderer implementation, fixture-policy decision, paid/API work, or cross-lane ownership change was run or approved. `.workflow-b.lock` points at newer run `20260510T005905-run-approved-section-local-build-slices-while-an` and was left untouched. The generated resume command still omits `--execute`, `--commit-mode review`, and `--hard-gate-mode switch-safe`, so executable resumes should add them manually until `root-workflow-b-resume-execute-flag` is fixed.
- Resume prompt: continue Workflow B with another approved safe slice. If engine remains selected, keep the contact-sheet renderer parked unless real sidecar examples exist or Nath approves a fixture strategy. Executable resumes should add `--execute --commit-mode review --hard-gate-mode switch-safe` manually.

## Multi-Agent Handoff

- Task: Workflow B cycle 1 recorder closure for run `20260510T005903-run-approved-section-local-build-slices-while-an`
- Current role: root recorder
- Last verified state: controller reached the cycle 1 root-recorder slot after creating an executable review-mode plan, updating the workflow review snapshot, and producing four cycle 1 prompts. Status and checkpoint streams are readable. Root coordinator recorded no hard gate and routed the safe slice to `vaultforge-icon` as verification/evidence only for the inactive media-style proposal decision. Icon builder made no file changes. Icon reviewer found no blocking issues, verified the media style note remains reference-only/inactive, confirmed no media proposal output directory exists, and made no commit because the icon lane was clean.
- Files touched: root `CHANGELOG.md`, root `WORKFLOW_REVIEW.md`, and `vaultforge-icon/SIGN_UP.md` by this recorder pass. Cycle work also wrote run-packet outputs `root-coordinator-routing.md` and `vaultforge-icon-reviewer-review.md`. No icon-lane source file was changed by the builder or reviewer in this cycle.
- Verification run: inspected `workflow-b-plan.md`, `workflow-b-live-status.md`, `status.jsonl`, `checkpoints.jsonl`, cycle 1 output notes, `root-coordinator-routing.md`, `vaultforge-icon-reviewer-review.md`, root `git status --short`, active `.workflow-b.lock`, icon `SIGN_UP.md`, icon `TASKS.md`, icon `CHANGELOG.md`, `git show --stat --name-only afabeb0`, and `git log --oneline -8`.
- Blocker or decision: no hard gate was recorded for this cycle. The media-style proposal decision remains inactive/no-generation; `run_icon_proposal.ps1`, paid/API generation, generated media proposal outputs, selected/applied outputs, asset operations, folder-icon application, live generation, and cross-lane ownership changes were not run or approved. The remaining Gallable proposal-selection task is still `#nath` and should stay parked until Nath makes the taste/selection decision. `.workflow-b.lock` points at newer run `20260510T005905-run-approved-section-local-build-slices-while-an` and was left untouched. The generated resume command still omits `--execute`, `--commit-mode review`, and `--hard-gate-mode switch-safe`, so executable resumes should add them manually until `root-workflow-b-resume-execute-flag` is fixed.
- Resume prompt: continue Workflow B with another approved safe slice. If staying in `vaultforge-icon`, do not switch into Gallable selection without Nath approval; keep media-style proposal generation inactive unless a future task explicitly changes the status and approves generation. Executable resumes should add `--execute --commit-mode review --hard-gate-mode switch-safe` manually.

## Multi-Agent Handoff

- Task: Workflow B cycle 1 recorder closure for run `20260510T004631-run-approved-section-local-build-slices-while-an`
- Current role: root recorder
- Last verified state: controller reached the cycle 1 root-recorder slot after creating an executable review-mode plan, updating the workflow review snapshot, and producing four cycle 1 prompts. Status and checkpoint streams are readable. Root coordinator recorded no hard gate and routed the safe slice to `vaultforge-engine` as verification/evidence only. Engine builder recorded live-required gate evidence for the contact-sheet renderer without implementing it. Engine reviewer found no blocking issues, ran the engine checks, and committed the reviewed engine section change as `a7e92e3`.
- Files touched: root `CHANGELOG.md`, root `WORKFLOW_REVIEW.md`, and `vaultforge-engine/SIGN_UP.md` by this recorder pass. Cycle work also touched `vaultforge-engine/SIGN_UP.md` and `vaultforge-engine/VERIFICATION.md` in engine commit `a7e92e3`, plus the run-packet outputs `root-coordinator-routing.md` and `vaultforge-engine-reviewer-review.md`.
- Verification run: inspected `workflow-b-plan.md`, `workflow-b-live-status.md`, `status.jsonl`, `checkpoints.jsonl`, cycle 1 output notes, `root-coordinator-routing.md`, `vaultforge-engine-reviewer-review.md`, root `git status --short`, active `.workflow-b.lock`, engine `SIGN_UP.md`, engine `TASKS.md`, `git show --stat a7e92e3`, and `git log --oneline -5`.
- Blocker or decision: no hard gate was recorded for this cycle. The contact-sheet renderer remains `#live-required` until real sidecar examples or a root-approved contact-sheet fixture strategy exists. No live generation, generated art, renderer implementation, fixture-policy decision, paid/API work, or cross-lane ownership change was run or approved. `.workflow-b.lock` points at newer run `20260510T005106-run-approved-section-local-build-slices-while-an` and was left untouched. The generated resume command still omits `--execute`, so executable resumes should add it manually until `root-workflow-b-resume-execute-flag` is fixed.
- Resume prompt: continue Workflow B by switching to another approved safe slice. If engine remains selected, keep the contact-sheet renderer parked unless real sidecar examples exist or Nath approves a fixture strategy; executable resumes should add `--execute` manually.

## Multi-Agent Handoff

- Task: Workflow B cycle 1 recorder closure for run `20260510T004645-run-approved-section-local-build-slices-while-an`
- Current role: root recorder
- Last verified state: controller reached the cycle 1 root-recorder slot after creating an executable review-mode plan, updating the workflow review snapshot, and producing four cycle 1 prompts. Status and checkpoint streams are readable. Root coordinator recorded no hard gate and routed the safe slice to `vaultforge-xp4l` for docs-only output-contract consolidation. XP4L builder added the section-local output contract. XP4L reviewer found no blocking issues, ran the XP4L checks, and committed the reviewed XP4L section change as `9c0dfa2`.
- Files touched: root `CHANGELOG.md`, root `WORKFLOW_REVIEW.md`, and `vaultforge-xp4l/SIGN_UP.md` by this recorder pass. Cycle work also touched `vaultforge-xp4l/OUTPUT_CONTRACT.md`, `README.md`, `ENGINE_BOUNDARIES.md`, `VERIFICATION_CRITERIA.md`, `TASKS.md`, `CHANGELOG.md`, and `SIGN_UP.md` in XP4L commit `9c0dfa2`, plus the run-packet outputs `root-coordinator-routing.md` and `vaultforge-xp4l-reviewer-review.md`.
- Verification run: inspected `workflow-b-plan.md`, `workflow-b-live-status.md`, `status.jsonl`, `checkpoints.jsonl`, cycle 1 output notes, `root-coordinator-routing.md`, `vaultforge-xp4l-reviewer-review.md`, root `git status --short`, active `.workflow-b.lock`, XP4L `git status --short`, XP4L `git show --stat --name-only 9c0dfa2`, XP4L `TASKS.md`, XP4L `SIGN_UP.md`, and XP4L `CHANGELOG.md`. Reviewer verification passed `python -m unittest discover -s tests -v` with 21 tests OK.
- Blocker or decision: no hard gate was recorded for this cycle. No runtime behavior change, live `E:\XP4Life` write, scoring semantics change, event-contract/source change, parser behavior change, fixture/test change, persistent progression design change, paid/API work, or cross-lane ownership change was run or approved. At recorder verification time, `.workflow-b.lock` pointed at a newer active Workflow B run and was left untouched. The generated resume command still omits `--execute`, so executable resumes should add it manually until `root-workflow-b-resume-execute-flag` is fixed.
- Resume prompt: continue Workflow B with rules-surface documentation, vault-output-shape alignment, or narrow coverage gaps. Keep live vault writes, XP scoring semantics, event-contract/source changes, persistent progression design changes, paid/API work, and cross-lane ownership changes gated unless Nath explicitly approves them.










