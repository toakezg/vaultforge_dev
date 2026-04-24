# Plan

## Section Thread Model

- [x] Promote `vaultforge-engine` as a dedicated worker base under root coordination.
- [x] Require engine threads to read root `CODEX_START.md`, root `SYSTEM.md`, root `THREAD_MAP.md`, and then engine docs.
- [x] Use the dedicated engine thread to handle the engine-specific step 7 handoff from business notes.
- [ ] Keep root informed when engine CLI contracts, metadata behavior, or wrappers affect business/art.

## Phase 0 - Boundary Skeleton

- [x] Create `vaultforge-engine` documentation skeleton.
- [x] Record the engine/art/business split in the root architecture note.
- [x] Leave dirty `vaultforge-art` untouched.

## Phase 1 - Copy-Based Prototype

- [x] Copy reusable generator code from `E:\tools\image_generation\vaultforge-art`.
- [x] Package it as first-pass engine code without breaking the original source.
- [x] Copy and adapt existing generator tests.
- [x] Run dry-run and unit-test checks from the new engine folder.
- [x] Rename the shared engine entrypoint from `src\generate_art.py` to `src\generate.py`.

## Phase 2 - Compatibility

- [x] Add an engine launcher.
- [x] Add an art compatibility wrapper that can call the engine.
- [x] Keep existing `vaultforge-art` commands working while the transition is underway.
- [x] Verify direct engine, art launcher, art batch-smoke, art config, and root XP4Life dry-run paths.
- [x] Keep engine execution launcher/direct-script based for now so lane wrappers can keep targeting `src\generate.py` without a required editable install.

## Phase 3 - Business Target

- [x] Complete business parity dry-run assessment.
- [x] Update `vaultforge-business` to target the engine when the engine prototype passes dry-run checks.
- [x] Preserve current business output routing.
- [ ] Keep business presets/styles/mods lane-owned until they prove reusable.

## Phase 4 - Shared Feature Growth

- [x] Add native support for variants and client/job/tag metadata.
- [ ] Add native support for tweaks, input images, and references after the edit/reference API contract is ready.
- [ ] Add shared gallery/contact-sheet primitives only after metadata shape settles.
