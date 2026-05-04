# Make Icon Interface Review

Status: accepted for no-write planning. Not accepted for implementation.

## Scope

Review `MAKE_ICON_INTERFACE_PLAN.md` and decide whether the planned no-write
`$make-icon` command shape should be accepted, revised, or rejected before any
script implementation is considered.

This review does not approve `make_icon.py`, script creation, image generation,
API calls, paid calls, asset moves or deletion, or folder icon application.

## Coordinator Brief

- Target: decide the interface-plan status and record the Nath-task tag rule.
- Budget: one Coordinator -> Builder -> Reviewer -> Recorder rotation, with one
  small related docs task included for the new `#nath` rule.
- Success check: next task can define a dry-run transcript check without
  treating the plan as approved implementation.
- Stop condition: stop before creating scripts, creating output folders,
  calling APIs, generating images, moving/deleting assets, or applying icons.

## Review Decision

Accept the command shape for no-write planning.

Do not accept it for implementation yet.

The useful accepted pieces are:

- required target, purpose, intended-use, and no-write inputs
- explicit `--no-write` safety flag
- one to three concept directions
- preview-only Markdown/metadata output shape
- blocked-action list
- output paths marked as assumptions, not created folders

## Required Clarification

`$make-icon` is a workflow/tool name in the icon lane, not a live shell command.

A future implementation review must decide the real invocation form, such as a
script, batch wrapper, task runner, or Codex skill. Until then, docs may keep
using `$make-icon` as the workflow label, but should not imply it can be run.

## Keep Parked

Keep `make_icon.py` parked until all of these are true:

- dry-run transcript acceptance check is defined
- output paths are accepted or revised
- ownership between icon, art, and engine lanes is confirmed
- Nath approves script implementation

## Reviewer Notes

- Scope stayed docs-only.
- The plan is clear enough for the next validation task.
- The biggest risk is mistaking the planned `$make-icon` shape for an executable
  command; this review records that it is only a planning label for now.
- Nath-gated work should be tagged with `#nath` in `TASKS.md` so handoffs make
  approval needs obvious.

## Recorder Handoff

Next task should define the exact no-write dry-run transcript acceptance check.
It should not create the dry-run tool, create output folders, or write generated
brief/metadata artifacts.
