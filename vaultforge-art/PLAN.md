# Plan

## Section Thread Model

- `vaultforge-art` is a promoted worker section under root coordination.
- section threads should read root startup docs before section docs.
- this section owns focused art work rather than root-wide coordination.

## Current Direction

- Keep the lane art-focused and lightweight.
- Use the shared engine for generation work.
- Keep direct prompts and inbox batch prompts easy to repeat.
- Keep output routing local to `output\`.

## Watchpoints

- Do not clone shared engine behavior into this lane.
- Keep `ART_KEY` lane-owned and documented.
- Avoid pulling client/business rules into art prompt work.
- Keep batch and direct prompt paths simple enough to dry-run first.

## Forward Look

- Add art-specific presets and style packs only when the lane actually needs them.
- Add review and curation surfaces after the first steady run of outputs.
- Expand tests only once the lane starts carrying more than the minimal wrapper.
