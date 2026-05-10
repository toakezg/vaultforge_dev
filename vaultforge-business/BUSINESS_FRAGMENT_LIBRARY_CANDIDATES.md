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

Resolved for the approved subset on 2026-05-10: the engine accepted a narrow
registry shape with business-facing preset/style aliases and a separate
`--constraint` registry for production constraints. Business mods were not
added to engine `--mod`; that registry still means emotional mood.

Do not directly add the remaining business mods to the engine `--mod` choices.
Business mods mix brand tone, market positioning, production constraints, and
delivery requirements. Moving them as-is would change shared engine semantics
and could leak business assumptions into art/icon lanes.

Implemented shared shape:

1. Engine supports selected business preset aliases: `business-icon`,
   `business-cover`, `brand-board`, and `social-brand-tile`.
2. Engine supports selected business style aliases: `clean-corporate`,
   `modern-startup`, `vector-crisp`, and `editorial-brand`.
3. Engine supports selected production constraints: `high-contrast`,
   `print-safe`, `small-size-readable`, and `transparent-bg-ready`.
4. Business preserves business-facing names in business metadata and passes the
   accepted aliases/constraints through for engine provenance.

Still business-owned:

- `client-pack`, `business-logo`, `brand-mark`, `mascot-logo`, `wordmark`, and
  `badge-emblem`.
- `trustworthy`, `premium`, `playful`, `bold`, `elegant`, and
  `local-friendly`.
- `tweak` wording and any future client-lane delivery requirements until a
  shared engine contract explicitly adopts them.

## Resume Prompt

```text
Continue Workflow B for vaultforge-business and vaultforge-engine. Read
vaultforge-business/BUSINESS_FRAGMENT_LIBRARY_CANDIDATES.md, then review the
accepted alias/constraint bridge. Do not move the remaining business-only
presets or brand-tone modifiers into engine registries without a new scoped
approval and review.
```
