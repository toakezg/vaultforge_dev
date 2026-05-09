# Plan

## Section Thread Model

- Business is a promoted worker section under root coordination.
- Business threads should read root `CODEX_START.md`, root `SYSTEM.md`, and root `THREAD_MAP.md` before section docs.
- Business owns client-facing workflows, prompt banks, wrappers, generated output routing, galleries, contact sheets, and review surfaces.
- Business should hand engine-specific tasks upward or across to `vaultforge-engine` instead of building shared behavior locally.

## Phase 1 - Business Lane Alive

- ~~Add business wrapper scripts.~~
- ~~Route output into `generated\client\asset\preset\style\date\job`.~~
- ~~Write run metadata beside images.~~
- ~~Convert starter packs to use the business wrapper.~~
- ~~Add markdown prompt bank templates.~~

## Phase 2 - Prompt Bank Workflow

- ~~Added a PowerShell bank runner for `.md` files in the business lane.~~
- ~~Parse simple YAML frontmatter for `client`, `asset_type`, `preset`, `styles`, `mods`, `tags`, `job`, and generation fields.~~
- ~~Save `prompt.source.md` beside each run when the markdown runner provides a source note.~~
- ~~Support `status`, `rating`, `image`, and the starter Dataview dashboard fields.~~

## Phase 3 - Engine Integration

- ~~Business parity dry-run assessment passed on 2026-04-12; the cleanest future retarget is for `run_business.ps1` to call `vaultforge-engine\src\generate.py` directly, not `run_engine.bat`.~~
- ~~The tiny retarget landed on 2026-04-12 by pointing `run_business.ps1` directly at `vaultforge-engine\src\generate.py` while preserving existing output routing, prompt composition, and metadata behavior.~~
- ~~The engine now supports native `--client`, `--job`, `--tag`, and `--variants` primitives.~~
- ~~Pass native engine `--client`, `--job`, `--tag`, and `--variants` through the business wrapper while preserving business routing and wrapper-owned manifests.~~
- ~~Review the manifest split after native metadata adoption: business keeps `run.json` and `gallery-entry.json` authoritative, while engine sidecars remain per-image provenance.~~
- ~~Pass native `--input-image` and `--reference-image` fields through from business now that shared engine plumbing exists.~~
- The business wrapper now calls the shared engine once per business run and lets engine-native `--variants` fan out image outputs while business keeps its own output routing, prompt composition, `run.json`, and `gallery-entry.json`.
- Keep `--tweak` as business-owned prompt context until a shared edit contract makes it worth moving into the engine.
- Move business preset/style/mod fragments into engine libraries when stable.
- Keep backward compatibility with the current wrappers.

## Phase 4 - Gallery

- ~~Build a metadata-driven gallery from `gallery-entry.json`.~~
- ~~Start with markdown or HTML.~~
- ~~Add contact sheets for visual comparison.~~
- ~~Add Dataview dashboards for Obsidian browsing.~~
