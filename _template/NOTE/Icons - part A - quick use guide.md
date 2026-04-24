# Icons - Part A - Quick Use Guide

This guide is the short operator version of the XP4Life Icons Part A pipeline.

## What This Pipeline Does

- reads Markdown prompt notes from `ICON/XP4Life/part-a/prompts/`
- sends them to the existing `vaultforge-art` image generator
- writes results into `ICON/XP4Life/part-a/generated/`

## Dependency

This launcher expects the art project to exist here:

```text
E:\tools\image_generation\vaultforge-art
```

It calls:

```text
E:\tools\image_generation\vaultforge-art\.venv\Scripts\python.exe
E:\tools\image_generation\vaultforge-art\generate_art.py
```

## Main Commands

Dry-run everything:

```bat
run-icons-part-a.bat --dry-run
```

Run every category live:

```bat
run-icons-part-a.bat
```

Run one category:

```bat
run-icons-part-a.bat quests
run-icons-part-a.bat achievements
run-icons-part-a.bat titles
run-icons-part-a.bat rewards
```

Force a single prompt file to rerun:

```bat
run-icons-part-a.bat quests --rerun quest-scroll
run-icons-part-a.bat achievements --rerun medal-star
```

Ask for command help:

```bat
run-icons-part-a.bat help
```

## Output Folders

- `ICON/XP4Life/part-a/generated/quests/`
- `ICON/XP4Life/part-a/generated/achievements/`
- `ICON/XP4Life/part-a/generated/titles/`
- `ICON/XP4Life/part-a/generated/rewards/`

## Recommended Prompts

### Quests

- `quest-scroll.md`: minimal glyph quest scroll with glowing gold linework
- `forward-compass.md`: forward-looking compass with gold and cyan accents
- `footsteps-path.md`: symbolic footsteps and path-forward journey icon

### Achievements

- `medal-star.md`: circular medal with central star and earned feel
- `laurel-badge.md`: laurel wreath badge with symmetrical glow
- `shield-star.md`: shield with star center for bold achievement language

### Titles

- `crown-emblem.md`: crown emblem with elegant fantasy crest logic
- `rune-sigil.md`: mythic rune sigil with selective purple accents

### Rewards

- `coin-reward.md`: compact coin reward symbol in gold
- `energy-orb.md`: smooth energy orb with cyan glow

## Prompt Source Files

The batch prompt notes live here:

```text
ICON\XP4Life\part-a\prompts\quests\
ICON\XP4Life\part-a\prompts\achievements\
ICON\XP4Life\part-a\prompts\titles\
ICON\XP4Life\part-a\prompts\rewards\
```

## Suggested First Run

1. Run `run-icons-part-a.bat --dry-run`
2. Run `run-icons-part-a.bat quests`
3. Review the outputs
4. Adjust prompts only after looking at real results

## First Validated Run

The first successful full run landed on 2026-04-11.

Example outputs are reviewed in:

```text
NOTE\Icons - part A - output review.md
```

If you want to use the generated icons in another vault, follow:

```text
NOTE\How to - Create XP4Life Icon set (obsidian).md
```
