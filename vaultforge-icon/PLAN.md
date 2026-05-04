# Icon Plan

## Section Thread Model

- `vaultforge-icon` is a promoted lightweight section under root.
- Root coordinates promotion, routing, and cross-lane decisions.
- Icon threads execute focused icon workflow, notes, and subtool validation.

## Current Direction

- Keep the lane small while it proves its value.
- Treat XP4Life icon notes and VaultForge Icons planning as the current source
  material.
- Treat `svg-forge` as the first active subtool, not a rewrite target.
- Validate existing dry-run paths before adding features.
- Use build-note ideas as manual workflow guidance before turning them into
  formal skills or scripts.
- Keep the current role set to Coordinator, Builder, Reviewer, Recorder, and an
  optional bounded Inspiration Scout after verification.
- Leave live image generation, paid API usage, deletion, and cloud work behind
  explicit decision gates.

## Active Workflow Rules From Build Notes

- Every larger icon-lane run should start with a short Coordinator brief:
  target, likely files, success check, stop/ask condition, and cycle budget.
- Reviewer must check scope drift, ownership drift, missing verification, and
  whether a proposed tool or skill is premature.
- Recorder must update `SIGN_UP.md`, `TASKS.md`, `CHANGELOG.md`, and the next
  resume prompt when a run changes lane state.
- Style/taste checks stay manual for now: compare work against lane direction,
  Nath/VaultForge taste, and the current docs before proposing more output.
- Smoke-test recording means exact command, exit code, no-write proof when
  relevant, and blocker text if the check cannot fully pass.
- One cycle means one full ordered role rotation, not one role. A 7-cycle run is
  a scope rule of thumb for larger deliverables that can benefit from seven
  repeated rotations. Tiny documentation passes should state their lower cycle
  estimate and stop cleanly when the deliverable is complete.
- Within one normal rotation, the active task may be completed with up to two
  small related additional tasks if they stay docs-only, share the same lane
  scope, and do not require Nath approval.
- A review note or future approval need is not automatically a stop. Park it as
  a `#nath` task, keep the handoff current, and continue to the next
  `#approved` docs-only or dry-run task when one exists.
- Tag tasks with `#nath` whenever Nath must approve, decide, unblock, or step
  in before the task can safely proceed.
- Use `#approved` for tasks Nath has explicitly cleared; keep the tag separate
  from the task id marker so task queries can read it.

## Parked Skill And Tool Candidates

- `$review-handoff-writer`: activate after two more icon-lane runs need the same
  SIGN_UP/TASKS/CHANGELOG/handoff shape.
- `$smoke-test-recorder`: activate after SVG-Forge or icon wrapper checks repeat
  enough that exact command/exit/no-write notes become mechanical.
- `$vaultforge-section-router`: keep root-owned unless icon work repeatedly
  needs cross-lane routing help.
- `$build-brief-maker`: activate only if Coordinator briefs become frequent and
  repetitive across icon-lane work.
- `$match-theme` / `$vstyle`: keep manual until there is a stable written style
  checklist for VaultForge icons.
- `$inspiration-scout`: keep as an optional role until at least one 7-cycle run
  proves it helps without derailing scope.
- `$make-icon`, `make_icon.py`, and `run_make_icon.bat`: `MAKE_ICON_CONTRACT.md`
  is the current no-paid-call contract. Two manual briefs and one review now
  show the brief/metadata shape is stable enough to plan a no-write interface.
  `MAKE_ICON_INTERFACE_PLAN.md` now defines the planned no-write command shape.
  `MAKE_ICON_INTERFACE_REVIEW.md` accepts that shape for planning only. Do not
  build the script until the dry-run transcript check passes, output paths are
  accepted, ownership is clear, and Nath approves implementation.
- `$apply-icon`, `apply_icon.py`, and `run_apply_icon.bat`: do not build until
  there are selected icons plus a reviewed dry-run apply-plan format.

## Watchpoints

- The icon lane can sprawl if it absorbs general art, business, or engine work.
- The multi-agent workflow can also stall if every review note becomes a hard
  stop; only live generation, paid calls, secrets, asset moves/deletes, folder
  icon application, ownership changes, and real taste decisions should force a
  Nath pause.
- SVG conversion work should stay practical: input discovery, dry-run behavior,
  output safety, and operator clarity before polish.
- Existing generated assets and moved notes may already be in a dirty worktree;
  do not clean them up as part of lane promotion.
- Build notes are reference material, not an instruction to create every role,
  skill, or script immediately.

## Forward Look

- Review whether SVG-Forge needs a setup helper, sample refresh, or README fix.
- Run one bounded 7-cycle icon-lane workflow only after the next task has a
  concrete deliverable and a clear verification path.
- Later, decide whether XP4Life icon packaging or broader VaultForge Icons
  client templates should become the next icon-lane task.
