# Make Icon No-Write Interface Plan

Status: interface plan only. No script exists. Later review accepted this
shape for no-write planning, not for implementation.

## Scope

This document plans the future `$make-icon` no-write interface after two manual
briefs and one metadata/output review proved the planning shape repeatable.

It does not approve:

- `make_icon.py`
- `run_make_icon.bat`
- image generation
- API calls
- paid calls
- secrets or cloud auth
- asset moves or deletion
- folder icon application

## Coordinator Brief

- Target: define a future no-write interface shape for `$make-icon`.
- Budget: one Coordinator -> Builder -> Reviewer -> Recorder rotation, with up
  to two small related docs tasks allowed in the same rotation.
- Success check: a future worker can see expected inputs, preview output,
  dry-run behavior, and output-path assumptions without needing code.
- Stop condition: stop before script creation, live generation, paid API calls,
  asset writes, or folder-icon application.

## Proposed Command Shape

This is a planned interface, not a command to run.

`$make-icon` is a workflow/tool label in these docs. A future implementation
review must still choose the real invocation form.

```text
$make-icon --target <path-or-name> --purpose <short-purpose> --use <intended-use> --no-write
```

Optional future flags:

```text
--style <style-note>
--brief <existing-brief.md>
--concept-count <1-3>
--output-root <planned-output-folder>
--format markdown
```

Required safety flag:

```text
--no-write
```

The first real interface should refuse to continue unless `--no-write` is
present.

## Required Inputs

- `target`: existing folder path or stable target name.
- `purpose`: short description of what the icon should represent.
- `use`: intended use, such as folder icon, lane identity, subtool identity, or
  client concept.
- `no-write`: explicit confirmation that the run is preview-only.

## Optional Inputs

- `brief`: existing Markdown brief to review or reuse.
- `style`: one or more style constraints.
- `concept-count`: one to three concept directions.
- `output-root`: planned future output location.
- `format`: preview format, initially Markdown.

## No-Write Preview Output

A no-write run should print or draft only this shape:

```text
MAKE ICON PREVIEW
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

blocked_actions:
  - no image generation
  - no API call
  - no asset move/delete
  - no folder icon application
  - no script creation during this planning task
```

## Dry-Run Behavior

The future dry-run/no-write behavior should:

- validate that required inputs are present
- normalize the target into a safe display name
- show planned Markdown and metadata paths
- show concept-count limits
- show blocked actions
- exit without writing files
- report `mode: no-write`

It should not:

- create directories
- create Markdown files
- create JSON files
- call image APIs
- inspect secrets
- apply icons
- move or delete assets

## Output Path Assumptions

These paths are assumptions for future planning only:

- planned briefs: `vaultforge-icon/generated/briefs/`
- planned metadata: `vaultforge-icon/generated/metadata/`
- planned image outputs: parked until live generation is approved
- planned applied icons: parked until `$apply-icon` has an approved apply-plan

The `generated/` folder should not be created by this task. A later approved
implementation task must decide whether those paths are correct.

## Reviewer Decision

The no-write interface shape is now clear enough for a future implementation
discussion, but not for implementation itself.

`make_icon.py` remains parked until Nath approves moving from interface plan to
script work.

## Recorder Handoff

Next work should choose one of these:

- review this interface plan and either approve, revise, or reject the command
  shape
- define the exact dry-run transcript acceptance check
- park `$make-icon` and switch to the `$apply-icon` apply-plan contract
