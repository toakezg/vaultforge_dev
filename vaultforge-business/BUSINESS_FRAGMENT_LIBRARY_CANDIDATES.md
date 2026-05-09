# Business Fragment Library Candidates

Date: 2026-05-09

## Purpose

This note is the business-owned review surface for the remaining
`business-fragment-library-move` task.

The actual move into `vaultforge-engine` is a cross-lane ownership change. This
business slice records the current candidate set, migration risk, and the next
handoff so a later engine/root pass can decide the shared-library shape without
guessing from wrapper code alone.

## Current Business Fragments

Business presets:

- `business-logo`
- `business-icon`
- `business-cover`
- `brand-mark`
- `brand-board`
- `client-pack`
- `social-brand-tile`
- `mascot-logo`
- `wordmark`
- `badge-emblem`

Business styles:

- `clean-corporate`
- `luxury-minimal`
- `modern-startup`
- `bold-retro-brand`
- `friendly-flat`
- `premium-3d`
- `mono-mark`
- `vector-crisp`
- `editorial-brand`
- `neon-signage`

Business mods:

- `trustworthy`
- `premium`
- `playful`
- `bold`
- `elegant`
- `local-friendly`
- `high-contrast`
- `small-size-readable`
- `print-safe`
- `transparent-bg-ready`

## Current Engine Shape

The shared engine currently keeps prompt fragments in `src/generate.py`:

- `PRESET_PROMPTS`: broad generation shapes such as `icon`, `vaultforge`,
  `artifact-card`, `obsidian-cover`, and `sacred-scene`.
- `STYLE_PROMPTS`: rendering/style language such as `geometric`, `fine-line`,
  `cinematic`, `painterly`, `photoreal`, `blueprint`, and `pixel`.
- `MOOD_PROMPTS`: emotional tone modifiers such as `peaceful`, `hopeful`, and
  `compassionate`.

The business wrapper maps business-facing names to the closest current engine
preset/style while keeping the business names in `run.json` and
`gallery-entry.json`.

## Prompt-Bank Usage Snapshot

Current runnable markdown prompt notes use this subset:

Presets:

- `brand-board`: 3
- `business-cover`: 4
- `business-icon`: 5
- `business-logo`: 4
- `client-pack`: 3

Styles:

- `clean-corporate`: 7
- `editorial-brand`: 4
- `friendly-flat`: 1
- `modern-startup`: 4
- `mono-mark`: 2
- `vector-crisp`: 14

Mods:

- `bold`: 5
- `high-contrast`: 5
- `premium`: 7
- `print-safe`: 3
- `small-size-readable`: 6
- `transparent-bg-ready`: 4
- `trustworthy`: 9

## Candidate Assessment

Ready to define as business-owned shared-library candidates:

- `vector-crisp`, `clean-corporate`, `modern-startup`, and `editorial-brand`:
  these are used repeatedly and already map cleanly to style-like engine
  behavior.
- `business-icon`, `business-cover`, `brand-board`, and `social-brand-tile`:
  these map to existing engine preset shapes, but should remain business names
  unless the engine adds namespaced or lane-aware preset aliases.
- `small-size-readable`, `high-contrast`, `print-safe`, and
  `transparent-bg-ready`: these are stable production constraints, but they do
  not fit the current engine `MOOD_PROMPTS` meaning.

Keep business-owned for now:

- `client-pack`: this is a workflow/product bundle, not a single engine
  generation preset.
- `business-logo`, `brand-mark`, `mascot-logo`, `wordmark`, and
  `badge-emblem`: these need output review before they become shared engine
  presets instead of client-lane naming.
- `trustworthy`, `premium`, `playful`, `bold`, `elegant`, and
  `local-friendly`: these are business tone/market-position modifiers. They may
  become shareable, but they need a separate modifier class or namespace rather
  than being mixed into engine mood choices.

## Migration Gate

Do not directly add business mods to the current engine `--mod` choices yet.
The engine's modifier registry currently means emotional mood. Business mods
mix brand tone, production constraints, and delivery requirements. Moving them
as-is would change shared engine semantics and could leak business assumptions
into art/icon lanes.

Recommended next shape:

1. Keep business wrapper mappings as the production path.
2. In an engine/root-approved pass, add registry structure that can distinguish
   preset, style, mood, production constraint, and lane alias.
3. Move only the stable candidates after the engine registry shape exists.
4. Preserve business-facing names in business metadata even if the engine gains
   shared aliases.

## Resume Prompt

```text
Continue Workflow B for vaultforge-business and vaultforge-engine. Read
vaultforge-business/BUSINESS_FRAGMENT_LIBRARY_CANDIDATES.md, then decide the
engine registry shape for business fragment migration. Do not move business
mods into engine MOOD_PROMPTS directly; first choose whether the engine should
support lane-aware aliases or separate production-constraint fragments.
```
