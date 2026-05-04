# VaultForge Multi-Agent Workflow

Use this as the first lightweight operating model for a simple build that needs
more than one Codex pass without losing the thread.

The goal is not to build a full agent platform yet. The goal is to make one
build run inspectable, resumable, and easy to hand back to Nath when a decision
matters.

## First Shape

Start with four roles:

- Coordinator: owns the task brief, routes work, keeps the handoff current, and
  decides whether to continue, pause, or ask Nath.
- Builder: makes the smallest useful code or doc change inside one section.
- Reviewer: checks the Builder's result for bugs, drift, missing tests, and
  scope creep.
- Recorder: updates the repo-facing notes, changelog, task status, and next
  handoff prompt.

For Codex chat work, one agent can play multiple roles when the task is tiny.
The important part is that the roles happen in order and leave evidence.

## Simple Build Run

1. Pick one task from root or section `TASKS.md`.
2. Write a short build brief before editing:
   - target section
   - files likely to change
   - success check
   - stop/ask condition
3. Coordinator routes the task through `THREAD_MAP.md`.
4. Builder implements the smallest useful version.
5. Reviewer runs a meaningful verification.
6. Recorder updates the handoff notes and changelog.
7. Coordinator decides one of:
   - continue
   - pause with a clean handoff
   - ask Nath for a decision

## Rotation Continuation

The workflow should not stop just because one role found a review note or a
future approval need.

Use this split:

- Hard gate: stop and ask Nath.
- Soft gate: record the blocker or decision need as a task, then continue if
  there is an approved safe next slice.

A run may continue into another Coordinator -> Builder -> Reviewer -> Recorder
rotation when all of these are true:

- the next slice is already scoped in `TASKS.md`
- the next slice is docs-only, dry-run, or otherwise safe
- the next slice does not require a new Nath decision
- the current handoff stays updated
- the run remains inside its stated cycle budget

When a task requires Nath to approve, decide, unblock, or step in, tag it with
`#nath` in the relevant `TASKS.md`. When Nath has explicitly cleared a task,
tag it with `#approved`.

For tiny docs-only runs, a single rotation may land the active task plus up to
two small related tasks. Larger runs should state the intended cycle budget up
front and continue until that budget is spent or a hard gate appears.

## Decision Gates

Stop and ask Nath when the workflow reaches one of these gates:

- the next step changes architecture or ownership between sections
- a live/non-dry-run action could cost money or create hard-to-clean outputs
- a secret, account, or external service needs a new permission
- there are two reasonable paths and the tradeoff is product/workflow taste
- there are two reasonable paths and the tradeoff is quantity/quality taste
- the task needs cloud notifications, remote runners, or persistent background
  work

When a gate happens, leave a short decision note with:

- what was done
- what is blocked
- the options
- the recommended option
- esitmated token usage so far and to contnue toward next milestone 
- the exact command or prompt to resume

If the gate is not blocking the current safe work, park it as a `#nath` task and
continue with the next `#approved` docs-only or dry-run task instead of ending
the run immediately.

## Handoff File Pattern

For a simple build, create or update a handoff note near the work:

- root coordination: `CURRENT_STATE.md` andor a short root note
- engine work: `vaultforge-engine/SIGN_UP.md` andor `vaultforge-engine/TASKS.md` 
- business work: `vaultforge-business/SIGN_UP.md` andor `vaultforge-business/TASKS.md`
- coding bridge work: `vaultforge-coding/SIGN_UP.md` andor
  `vaultforge-coding/TASKS.
- icon bridge work: `vaultforge-icon/SIGN_UP.md` andor
  `vaultforge-icon/TASKS.md` 



Keep the handoff short enough that a new thread can read it quickly.

Recommended shape:

```md
## Multi-Agent Handoff

- Task:
- Current role:
- Last verified state:
- Files touched:
- Verification run:
- Blocker or decision:
- Resume prompt:
```

## Skill Adoption Loop

Use skills only after a workflow repeats enough to deserve one.

1. Do the workflow manually once.
2. Record the exact prompts, files, checks, and failure points.
3. Repeat it on a second small task.
4. Extract only the stable parts into a skill.
5. Keep repo-specific routing in VaultForge docs, not inside a generic skill.

Good first skill candidates:

- build-brief-maker
- review-handoff-writer
- vaultforge-section-router
- smoke-test-recorder

## Cloud Notification Later

Cloud work is a later adapter, not the first dependency.

The first useful notification loop would be:

1. Local or cloud runner reaches a decision gate.
2. It writes the decision note into the repo or a small queue.
3. It sends Nath a notification with the short options.
4. Nath replies with a decision.
5. The runner resumes from the recorded prompt.

Until that exists, the repo handoff is the notification surface.

## Starter Prompt

Use this when starting a small multi-agent build in Codex:

```text
Use the VaultForge multi-agent workflow for a simple build.

Read CODEX_START.md, CURRENT_STATE.md, THREAD_MAP.md, TASKS.md, and
MULTI_AGENT_WORKFLOW.md first.

Act as Coordinator first. Pick or confirm the target task, write a short build
brief, then move through Builder, Reviewer, and Recorder roles. Stop for Nath
only at a decision gate. Keep changes small, verify what you can, and leave a
resume handoff if the run cannot finish. 
```
