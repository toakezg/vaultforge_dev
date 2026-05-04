# Icons - Part A - Todo

> Current lane note: this Part A todo is reference and inspiration material.
> Do not treat it as direct build requirements or the current `$make-icon`
> planning contract.

## Objective

Turn the XP4Life icon idea into a vault-local, repeatable pipeline that can be run from prompt notes without rebuilding the art engine.

## Attack Plan

- [x] Distill the source note into a clean implementation note.
- [x] Define the integration path before writing files.
- [x] Create core workspace docs so future Codex threads can boot quickly.
- [x] Create a quick operator guide with ready-to-run commands.
- [x] Create the first recommended prompt bank for quests, achievements, titles, and rewards.
- [x] Add a vault-local batch launcher for Part A.
- [x] Dry-run the full prompt bank to verify the launcher, prompt folders, and output folders.
- [x] Mirror the user-facing assets into `_template/` while keeping the implementation-planning notes at the workspace level.
- [ ] Live-run the prompt bank to validate the first actual outputs.
- [ ] Tune prompt wording based on real output review.
- [ ] Review whether the seeded template version should stay full, be reduced, or move into an optional pack later.

## Implementation Route

The route chosen for Part A is:

1. Notes define the system and the operator guidance.
2. Markdown prompt files act as the batch inputs.
3. A local launcher resolves vault-relative prompt and output folders.
4. The launcher calls the existing `vaultforge-art` Python generator directly.
5. Outputs stay in this vault so review and iteration can happen beside the notes.

## Why This Is Solid

- The source note is already clear about categories, style, and initial prompt direction.
- `vaultforge-art` already has the batch, preset, style, and output logic needed for Part A.
- The missing piece here was packaging, docs, and a local operator entry point rather than a new engine.

## Immediate Follow-Up

- Run `run-icons-part-a.bat --dry-run`.
- Run one category live once API access is ready.
- Capture the strongest results and decide how Part B should narrow the style.
