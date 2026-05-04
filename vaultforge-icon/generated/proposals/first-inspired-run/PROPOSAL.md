# First Inspired-Agent Icon Proposal Run

Date: 2026-05-04

Task id: `icon-inspired-agent-first-proposal-run`

Status: proposal docs and generated proposal images written.
This folder is for proposal material only.

## Scope

Create the first inspired-agent icon proposal pass using the icon lane's
approved proposal destination:

- target folder: `vaultforge-icon/generated/proposals/first-inspired-run/`
- source direction: `vaultforge-icon/build-notes/` role notes
- source briefs:
  - `vaultforge-icon/NOTE/Make Icon Brief - SVG-Forge.md`
  - `vaultforge-icon/NOTE/Make Icon Brief - Build Notes.md`
- output intent: three generated proposal images plus run metadata

## Boundaries

This run does not approve or perform:

- secret printing
- new cloud auth
- asset moves or deletes
- folder icon application
- selected or applied icon outputs
- final taste or winner decisions

## Inspiration Scout Direction Used

The first run uses Inspiration Scout as a bounded proposal role, not as a
selection authority. The aim is to produce three inspectable visual directions:

1. A practical raster-to-vector utility mark for SVG-Forge.
2. A quiet process-notes identity for Build Notes.
3. A combined VaultForge icon-lane mark that bridges conversion craft and
   organized planning.

## Proposal Set

### Proposal 01: SVG-Forge Raster Bridge

- Prompt file: `prompts/01-svg-forge-raster-bridge.txt`
- Source brief: `Make Icon Brief - SVG-Forge`
- Concept: pixel material resolving into a clean vector path
- Review use: judge whether the conversion subtool reads clearly at small size

### Proposal 02: Build Notes Workflow Cards

- Prompt file: `prompts/02-build-notes-workflow-cards.txt`
- Source brief: `Make Icon Brief - Build Notes`
- Concept: tidy note cards with a small future-candidate marker
- Review use: judge whether the process-note folder reads as calm and parked

### Proposal 03: Icon Lane Forge Notes

- Prompt file: `prompts/03-icon-lane-forge-notes.txt`
- Source briefs: both manual make-icon briefs
- Concept: restrained folder/tool identity combining vector craft and notes
- Review use: compare whether a broader lane identity is useful later

## Planned Engine Settings

- command mode: batch prompt files
- engine: `vaultforge-engine/src/generate.py`
- preset: `icon`
- style: `geometric`
- size: `1024x1024`
- quality: `low`
- format: `png`
- background: `transparent`
- variants: `1`
- output dir: `vaultforge-icon/generated/proposals/first-inspired-run/images`
- metadata: enabled by `--client`, `--job`, and `--tag`

## Review Notes

These images are proposal artifacts. They can inform a future review or next
proposal pass, but this run stops before selection, conversion, application,
or packaging.

## Run Result

- Proposal Markdown and prompt files were created.
- Initial live generation using the general `OPENAI_API_KEY` failed because
  that key lacked `api.responses.write`.
- `run_icon_proposal.ps1` then loaded `ICON_KEY` from `vaultforge-icon/.env`
  and mapped it to `IMAGE_GENERATION_KEY_B_OPENAI_API_KEY` for the child engine
  process only.
- Dry-run passed with 3 prompt files planned and 0 skipped.
- Live generation exited `0` and wrote three PNG proposal images plus three JSON
  metadata files under `images/`.
- No selected outputs, applied outputs, moved assets, deleted assets, folder
  icons, or final taste decisions were created.
