# Make Icon Dry-Run Transcript Check

Status: acceptance check only. No dry-run tool exists.

## Scope

Define the exact transcript shape a future no-write `$make-icon` preview must
produce before any implementation work is considered.

This document does not create `make_icon.py`, create output folders, write
generated artifacts, generate images, call APIs, move/delete assets, or apply
folder icons.

## Coordinator Brief

- Target: define the dry-run transcript acceptance check for the planned
  no-write `$make-icon` interface.
- Budget: one Coordinator -> Builder -> Reviewer -> Recorder rotation, with one
  small related docs task for the `#approved` stamp rule.
- Success check: a future reviewer can compare a dry-run transcript against this
  file and decide pass/fail without running live generation.
- Stop condition: stop before creating scripts, output folders, generated files,
  API calls, images, asset operations, or icon application.

## Acceptance Input

A future dry-run transcript must be reviewable from plain text. It should show
the planned request, planned outputs, and blocked actions.

Required sample target for the first acceptance check:

```text
target: vaultforge-icon/svg-forge
purpose: raster-to-SVG conversion subtool identity
intended_use: folder icon concept
mode: no-write
```

## Required Transcript Blocks

A passing transcript must include these blocks in order:

1. `MAKE ICON PREVIEW`
2. `request`
3. `planned_brief`
4. `planned_metadata`
5. `planned_outputs`
6. `blocked_actions`
7. `no_write_result`

## Required Transcript Shape

```text
MAKE ICON PREVIEW

request:
  target: vaultforge-icon/svg-forge
  purpose: raster-to-SVG conversion subtool identity
  intended_use: folder icon concept
  mode: no-write

planned_brief:
  title: Make Icon Brief - SVG-Forge
  sections:
    - Target
    - Context
    - Concept Directions
    - Style Notes
    - Prompt Drafts
    - Metadata Proposal
    - Follow-Up

planned_metadata:
  target: vaultforge-icon/svg-forge
  purpose: raster-to-SVG conversion subtool identity
  status: concept
  approval: draft
  source_brief: <planned-or-existing-brief-path>
  style_notes: <summary>

planned_outputs:
  markdown_brief: <output-root>/briefs/<safe-target-name>.md
  metadata: <output-root>/metadata/<safe-target-name>.json
  created_files: 0
  created_folders: 0

blocked_actions:
  - no image generation
  - no API call
  - no paid call
  - no secret lookup
  - no asset move/delete
  - no folder icon application
  - no script creation

no_write_result:
  pass: true
  wrote_files: false
  created_folders: false
  generated_images: false
  called_apis: false
  moved_or_deleted_assets: false
  applied_folder_icons: false
```

## Pass Criteria

A transcript passes only if:

- `mode: no-write` is present under `request`
- `created_files: 0` is present under `planned_outputs`
- `created_folders: 0` is present under `planned_outputs`
- every blocked action is listed
- every `no_write_result` boolean is safe
- there is no claim that `$make-icon` is a live runnable command
- output paths are shown as planned paths only

## Fail Criteria

A transcript fails if it:

- omits `mode: no-write`
- implies files or folders were created
- implies images were generated
- implies an API, paid service, secret, or cloud auth was used
- implies assets were moved or deleted
- implies a folder icon was applied
- treats `$make-icon` as an existing command rather than a planned workflow label
- omits the blocked-actions list

## Reviewer Notes

- This is a text-only acceptance check.
- The first passing transcript should still not create `make_icon.py`.
- The planned output folders remain assumptions until a later approved task
  accepts or revises them.

## Recorder Handoff

Next work may review output path assumptions or move to a different parked tool
contract. Script implementation remains blocked until Nath approves it.
