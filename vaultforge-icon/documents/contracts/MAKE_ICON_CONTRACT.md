# Make Icon Contract

Status: contract only. Do not build `make_icon.py` yet.

## Purpose

`$make-icon` is a future icon-lane workflow for turning a folder, lane, client,
project, or task purpose into reviewable icon concepts.

The first useful version should help plan icon ideas safely. It should not
generate images, spend API money, apply folder icons, move assets, delete
assets, or decide project ownership by itself.

## Current Safe Shape

For now, `$make-icon` means a manual contract-guided workflow:

1. Read the target context.
2. Write a short icon brief.
3. Draft one to three icon concept directions.
4. Record suggested prompts or style notes.
5. Stop before generation or asset application.

## Inputs

Required:

- target path or target name
- icon purpose
- intended use, such as folder icon, lane identity, client concept, or task icon
- no-paid-call confirmation

Optional:

- existing icon references
- style constraints
- size or format goal
- notes from `build-notes`
- related VaultForge lane docs

## Outputs

Allowed outputs before a real tool exists:

- Markdown icon brief
- concept list
- prompt draft
- style/taste notes
- metadata proposal
- follow-up task recommendation

Not allowed without a later approved task:

- image generation
- API calls
- `make_icon.py`
- `run_make_icon.bat`
- asset moves or deletes
- folder icon application
- edits to `apply_icon.py` or apply-plan files

## No-Paid-Call Rule

The workflow must stay local and text-only unless Nath explicitly approves a
live generation task.

Before any future generated-image path exists, it must document:

- which command would run
- which key or service it would use
- where outputs would land
- how cost or quota risk is limited
- how a dry-run or preview proves intent first

## Metadata Draft

A future generated result should be able to carry:

- `target`
- `purpose`
- `source_brief`
- `style_notes`
- `prompt`
- `created_by`
- `created_at`
- `status`, such as `concept`, `generated`, `selected`, or `applied`
- `approval`, such as `draft`, `reviewed`, or `approved`

This metadata shape is a draft only. Do not lock it into code until one real
manual run proves the fields are useful.

## Stop Gates

Stop and ask Nath before:

- live generation
- paid API calls
- secrets or cloud auth
- creating `make_icon.py`
- applying icons to folders
- moving or deleting icon assets
- choosing between multiple visual directions where taste matters
- changing ownership between icon, art, business, or engine lanes

## Activation Conditions

Keep `make_icon.py` parked until all of these are true:

- two manual `$make-icon` briefs have been useful enough to repeat
- the metadata draft has survived at least one review without major changes
- the no-write interface plan has been reviewed and accepted
- the no-paid-call dry-run behavior is defined and accepted
- text output paths are agreed for preview and a later approved write task
  explicitly allows creating them
- generation ownership is clear between icon lane, art lane, and engine
- Nath approves moving from contract to script

## First Manual Run Candidate

A good first manual run would be a docs-only icon brief for one existing
VaultForge lane folder. It should produce a Markdown brief and no assets.
