# Architecture - Engine Extraction

Date: 2026-04-11

## Current Status Update

As of 2026-04-12, the first copy-based shared engine prototype is live under:

```text
E:\tools\vaultforge\vaultforge-engine\src\generate.py
```

`vaultforge-business` now targets that shared engine directly. The art
compatibility bridge has also been proven in dry-run checks. Root XP4Life
wrappers still call the sibling art generator directly and should only be
retargeted in their own explicit compatibility pass.

## Decision

VaultForge should move toward three clear responsibilities:

- `vaultforge-engine` is the stable shared generation core.
- `vaultforge-art` is the art-facing, experimental, and playground lane.
- `vaultforge-business` is the business and client-facing generation lane.

The important shift is that `vaultforge-art` should not stay the long-term root for reusable generator behavior. It can keep being useful as an art lane, but the shared generator needs a cleaner home.

## Current Finding

In this workspace, `vaultforge-art` is not a child folder. The current working generator lives at:

```text
E:\tools\image_generation\vaultforge-art
```

That sibling worktree is dirty, so the first extraction step should avoid edits there.

The reusable generator behavior currently appears concentrated in:

```text
E:\tools\image_generation\vaultforge-art\generate_art.py
```

The current business lane also points at that sibling path through:

```text
vaultforge-business\run_business.ps1
```

## Engine Candidates

These concerns should migrate into `vaultforge-engine` once the extraction starts:

- CLI parser and argument-file support
- API key handling
- model fallback behavior
- prompt composition
- preset, style, and modifier registries
- batch folder resolution
- markdown prompt cleanup
- `.batch-state.json` read/write logic
- rerun target matching
- output path and filename building
- metadata writing
- image request and response extraction
- future edit/input-image plumbing
- tests covering shared behavior

Observed current functions/classes that are likely engine code:

- `ConfigFileArgumentParser`
- `slugify`
- `strip_optional_quotes`
- `resolve_project_path`
- `parse_args`
- `validate_args`
- `resolve_batch_folder`
- `get_api_key`
- `compose_prompt`
- `extract_image_bytes`
- `build_output_path`
- `load_batch_state`
- `save_batch_state`
- `build_batch_request_hash`
- `extract_markdown_prompt_text`
- `load_batch_prompts`
- `request_image`
- `generate_with_fallback`
- `run_batch`

## Art Lane Candidates

These should remain art-lane concerns:

- fantasy and sacred-scene prompt packs
- experimental art prompt banks
- playground output folders
- art-specific smoke prompts
- art wrappers such as `run_art.bat`
- Obsidian notes that are about art experiments
- any unstable prompt hacks or trials

## Business Lane Candidates

These should remain business-lane concerns:

- `vaultforge-business\my-prompts-bank`
- client pack templates
- business preset/style/mod naming
- client-oriented output routing
- Dataview dashboards
- gallery/index plans
- client metadata and delivery conventions
- wrappers such as `run_business.bat` and `run_business.ps1`

## Proposed Target Structure

```text
E:\tools\vaultforge\
  vaultforge-engine\
    README.md
    SYSTEM.md
    PLAN.md
    TASKS.md
    CODEX_START.md
    src\
    tests\
  vaultforge-business\
  vaultforge-art\              # later, if/when art lane is brought under this root

E:\tools\image_generation\
  vaultforge-art\              # current dirty source; inspect only until ready
```

The exact final filesystem location of the art lane can be decided later. The architectural boundary matters more than the immediate folder move.

## Staged Migration

### Phase 0 - Document Boundaries

Create `vaultforge-engine` as a planning skeleton and record what belongs there. Do not move generator code yet.

### Phase 1 - Copy, Do Not Rename

Copy the reusable generator into `vaultforge-engine` under a package/module shape. Keep the old `vaultforge-art` entrypoint working.

Suggested first copy targets:

- `generate_art.py` into an engine module or compatibility script
- `tests\test_generate_art.py` into engine tests
- `requirements.txt` and packaging metadata, adjusted for engine naming

### Phase 2 - Add Compatibility Wrappers

Leave `vaultforge-art\run_art.bat` working, but have it call the engine entrypoint. This keeps existing prompt banks and smoke checks usable.

### Phase 3 - Point Business At Engine

Update `vaultforge-business\run_business.ps1` so `-ArtRoot` becomes an engine root or a generic generator root. Preserve the current default until the engine has been verified.

### Phase 4 - Move Lane-Specific Libraries

Move only stable shared registries into the engine. Keep experimental and client-specific prompt fragments in their lanes until they prove reusable.

### Phase 5 - Gallery And Edit APIs

After the engine boundary is stable, add shared support for:

- `--client`
- `--job`
- `--tag`
- `--variants`
- `--tweak`
- `--input-image`
- `--reference-image`
- metadata manifests
- gallery/contact-sheet hooks

## First Recommended Implementation Slice

The safest slice is now complete when:

- `vaultforge-engine` exists as a documented skeleton.
- root docs describe the engine/art/business split.
- `vaultforge-business` docs stop treating `vaultforge-art` as the permanent engine.
- no dirty sibling files are modified.

The next code slice should be a copy-based prototype inside `vaultforge-engine`, followed by dry-run verification.

## Risks

- The current source generator is in a dirty sibling worktree.
- `vaultforge-business` currently hardcodes `E:\tools\image_generation\vaultforge-art`.
- The generator is still single-file, so extraction should be copy-first and test-backed.
- Business edit flags are currently wrapper-level metadata/prompt context, not native API edit behavior.

## Decision Rule

If both art and business would need it, it probably belongs in `vaultforge-engine`.
