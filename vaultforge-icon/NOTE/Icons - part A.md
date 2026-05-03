# Icons - Part A

## Intent

XP4Life Icons Part A establishes the first reusable icon lane for XP4Life.

The goal is to turn the note from idea-stage thinking into a prompt bank and a repeatable generation path for:

- quests
- achievements
- titles
- rewards

## Design Target

The visual target is a mythic productivity icon language:

- clean and centered
- readable at small sizes
- strong silhouette
- minimal clutter
- dark charcoal base
- gold, cyan, and selective purple accents
- no text inside the icon

## Category Scope

### Quests

Use symbols that imply direction, journey, or active progress:

- scroll
- compass
- path
- footsteps

### Achievements

Use earned-looking badge language:

- medal
- star
- shield
- laurel

### Titles

Use more emblematic or crest-like forms:

- crown
- crest
- sigil
- rune

### Rewards

Use compact reward symbols:

- coin
- gem
- energy orb
- spark

## Tier Direction

Part A is prompt-bank-first, but the intended tier logic is already clear:

- Bronze: simple linework, low glow
- Silver: subtle extra detail
- Gold: stronger glow and refinement
- Mythic: more unique patterning with selective purple accents

## Implementation Decision

This workspace will not duplicate the image generator.

Instead, the system is:

1. Keep the concept and quick guidance in `NOTE/`.
2. Keep the prompt files in `ICON/XP4Life/part-a/prompts/` as `.md` or `.txt`.
3. Keep outputs in `ICON/XP4Life/part-a/generated/`.
4. Use `run-icons-part-a.bat` as the vault-local entry point.
5. Delegate actual image generation to `E:\tools\image_generation\vaultforge-art\generate_art.py`.

## Why This Route

This approach keeps the workflow:

- local to the vault
- editable in Markdown
- easy to review inside Obsidian
- compatible with the existing art pipeline
- reversible if the icon lane needs to change later
