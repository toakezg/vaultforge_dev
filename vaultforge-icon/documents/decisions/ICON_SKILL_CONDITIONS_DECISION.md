# Icon Skill Conditions Decision

Date: 2026-05-04

Status: decision only. No skills, scripts, generated artifacts, images, APIs,
asset moves/deletes, or folder icons were created.

## Scope

Decide the two parked icon-lane skill-condition tasks:

- `icon-skill-review-handoff-condition`
- `icon-skill-smoke-recorder-condition`

Reviewed evidence came from recent icon-lane handoff updates in `SIGN_UP.md`,
recent task/changelog rotations, the no-write dry-run transcript contract, and
the approved SVG-Forge real-sample smoke record.

## Decision

Do not create `$review-handoff-writer` or `$smoke-test-recorder` as real skills
now.

Both should stay parked as candidate skills, with activation conditions revised
from simple repetition counts to evidence-based gates.

## `$review-handoff-writer`

Decision: root-cooperative use is approved; keep real skill creation parked
until a task explicitly asks for the reusable skill/spec.

Why:

- The repeated `SIGN_UP.md`, `TASKS.md`, `CHANGELOG.md`, and handoff updates
  show a stable recorder shape.
- The current shape is still easy to execute manually inside the lane docs.
- Nath clarified that cooperation with root docs counts as real cross-lane
  VaultForge operation, because root coordination updates are required by the
  system.
- Making a real skill still deserves its own scoped task so the first version
  can target root handoff updates instead of becoming generic automation.

Revised activation condition:

The cross-lane/root-doc condition is now satisfied for a root-cooperative
handoff writer. A future scoped task may draft or build it when it targets:

- icon `SIGN_UP.md`, `TASKS.md`, and `CHANGELOG.md`
- root coordination docs when the icon-lane change affects root routing or
  VaultForge-level state
- explicit handoff/resume prompts
- no asset changes, API calls, folder-icon application, or taste decisions

Until that scoped task starts, keep the reusable shape as a checklist in lane
docs, not a generated skill file.

## `$smoke-test-recorder`

Decision: revise activation condition; keep parked.

Why:

- The lane now has useful smoke evidence: blocked no-write dry-run recording,
  dry-run transcript acceptance planning, and an approved live SVG-Forge sample
  conversion with command/exit/output evidence.
- The current examples mix no-write checks, write-scoped sample generation, and
  future wrapper checks. That is enough to define a recorder shape, but not
  enough to make a general skill without overfitting to SVG-Forge.

Revised activation condition:

Activate only after at least two more checks reuse the same recorder fields
across different cases, including at least one wrapper or no-write check. The
recorded fields should be:

- command and working directory
- expected write mode
- exit code
- written paths or no-write proof
- inspected evidence
- blocker text, when blocked
- cleanup expectation

Until then, keep smoke recording as a lane rule and task wording pattern, not a
skill.

## Current Reusable Rule

For now, Recorder should continue to write the exact evidence directly into
`TASKS.md`, `CHANGELOG.md`, `SIGN_UP.md`, and any task-specific decision doc
when useful.

This is enough for the current compact icon workflow rotation.
