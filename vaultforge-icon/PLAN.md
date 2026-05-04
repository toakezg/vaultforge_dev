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
- Local file/folder writes are now approved for icon-lane work when a task
  explicitly scopes them and the writes stay inside that lane/write scope.
- Leave generated artifacts, live image generation, paid/API usage, deletion,
  asset movement, cloud work, folder-icon application, ownership changes, and
  taste decisions out of dry-run/build passes unless a later task explicitly
  clears the relevant hard gate.

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
- A review note, future approval need, or future live-run need is not
  automatically a stop. Park live validation as `#live-required`, keep the
  handoff current, and continue to the next `#approved` docs-only, dry-run, or
  build task when one exists.
- Local writes are allowed during build work when the task names the write
  scope and the write stays inside it; this does not approve generated
  artifacts, asset operations, folder-icon application, secrets/cloud auth, or
  paid/API work.
- Tag tasks with `#nath` only when Nath must approve, decide, unblock, or step
  in at a hard gate before the task can safely proceed.
- Tag tasks with `#live-required` when the only missing piece is future
  non-dry-run validation; state the exact live run needed in the task text.
- Use `#approved` for tasks Nath has explicitly cleared; keep the tag separate
  from the task id marker so task queries can read it.

## Parked Skill And Tool Candidates

- `$review-handoff-writer`: root-cooperative use is approved by Nath.
  `documents/decisions/ICON_SKILL_CONDITIONS_DECISION.md` now treats root-doc
  cooperation as sufficient cross-lane need, but real skill/spec creation still
  needs its own scoped task.
- `$smoke-test-recorder`: keep parked. `documents/decisions/ICON_SKILL_CONDITIONS_DECISION.md`
  revises activation to require at least two more repeated smoke records across
  different cases, including at least one wrapper or no-write check, using the
  same command, write-mode, exit-code, evidence, blocker, and cleanup fields.
- `$vaultforge-section-router`: keep root-owned unless icon work repeatedly
  needs cross-lane routing help.
- `$build-brief-maker`: activate only if Coordinator briefs become frequent and
  repetitive across icon-lane work.
- `$match-theme` / `$vstyle`: keep manual until there is a stable written style
  checklist for VaultForge icons.
- `$inspiration-scout`: keep as an optional role until at least one 7-cycle run
  proves it helps without derailing scope.
- Inspired-agent proposal docs: approved as guidance for future icon proposal
  runs. `documents/decisions/INSPIRED_AGENT_PROPOSALS_DECISION.md` approves
  `vaultforge-icon/generated/proposals/` for proposal Markdown, supporting
  proposal metadata, generated proposal images, and run metadata. API/paid
  generation is approved for scoped proposal runs; printing secrets, adding new
  cloud auth, selected/applied outputs, folder-icon application, asset
  moves/deletes, and final taste decisions remain gated. The first scoped run at
  `generated/proposals/first-inspired-run/` now has proposal docs, three
  generated PNG proposal images, JSON metadata, and batch state.
- Proposal generation should use `run_icon_proposal.ps1` from the icon lane when
  possible. It reads `ICON_KEY` from `vaultforge-icon/.env` and maps it to the
  shared engine's expected key variable for the child process only, so icon
  usage can be managed separately from other VaultForge lanes.
- Proposal inbox: users or agents may drop rough ideas, folder lists, scoped
  directory descriptions, and style notes into `generated/proposals/inbox/`.
  `documents/contracts/ICON_SET_GENERATION_WORKFLOW_CONTRACT.md` defines how
  those inputs become icon-set proposal runs.
- `$make-icon`, `make_icon.py`, and `run_make_icon.bat`: `documents/contracts/MAKE_ICON_CONTRACT.md`
  is the current no-paid-call contract. Two manual briefs and one review now
  show the brief/metadata shape is stable enough to plan a no-write interface.
  `documents/contracts/MAKE_ICON_INTERFACE_PLAN.md` now defines the planned no-write command shape.
  `documents/reviews/MAKE_ICON_INTERFACE_REVIEW.md` accepts that shape for planning only. Building
  the dry-run/no-write side may continue when it stays aligned with the icon
  generator goal. `documents/reviews/MAKE_ICON_OUTPUT_PATH_REVIEW.md` keeps
  `vaultforge-icon/generated/briefs/` and
  `vaultforge-icon/generated/metadata/` as planned no-write preview defaults,
  but the folders remain parked and uncreated until an approved write task.
  Park live generation checks as `#live-required` until a later task explicitly
  allows them.
- `$apply-icon`, `apply_icon.py`, and `run_apply_icon.bat`:
  `documents/contracts/APPLY_ICON_APPLY_PLAN_CONTRACT.md` now defines the approved apply-plan
  format for review and dry-run planning only. Do not build the script, create
  generated apply-plan artifacts, or apply folder icons until selected icon
  sources exist, one manual apply-plan review holds, output writes are
  explicitly approved, rollback expectations are clear, and Nath approves
  moving from contract to script.

## Watchpoints

- The icon lane can sprawl if it absorbs general art, business, or engine work.
- The multi-agent workflow can also stall if every review note becomes a hard
  stop; only direction changes from the icon-generator goal, secrets/cloud
  permissions, paid/live work that cannot be deferred, asset moves/deletes,
  folder icon application, ownership changes, and real taste decisions should
  force a Nath pause.
- Local writes should stay boring and scoped: no generated outputs, asset
  movement, deletion, folder-icon application, API calls, cloud auth, or secret
  handling should be smuggled in under a generic write approval.
- SVG conversion work should stay practical: input discovery, dry-run behavior,
  output safety, and operator clarity before polish.
- Real SVG-Forge sample rasters are useful for future conversion smoke tests,
  but `tools\make_samples.py` is a write step. The explicitly approved
  `icon-svg-forge-real-sample-live-smoke` task proved the path with
  `output\real-sample-smoke`; future refreshes still need explicit write scope.
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
