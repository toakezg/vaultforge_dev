# How to - Create an XP4Life Icon Set for Obsidian

This guide explains how to turn the generated XP4Life icon outputs into a reusable icon set that can travel into the separate XP4Life vault or any other Obsidian vault.

## Goal

Create an icon pack that can be used in:

- Obsidian notes
- image embeds
- dashboards
- file explorer folders
- file explorer notes
- other vaults that copy the same icon folder

## Recommended Folder Structure

Keep the reusable icon set in one clear folder:

```text
ICON\XP4Life\part-a\
  generated\
    quests\
    achievements\
    titles\
    rewards\
  selected\
    quests\
    achievements\
    titles\
    rewards\
  prompts\
```

Use `generated/` for raw outputs.

Use `selected/` for icons that are approved for real use.

## Step 1 - Generate the Icons

From the vault root, run:

```bat
run-icons-part-a.bat --dry-run
```

If the dry run looks right, run a category:

```bat
run-icons-part-a.bat quests
run-icons-part-a.bat achievements
run-icons-part-a.bat titles
run-icons-part-a.bat rewards
```

The generated files land in:

```text
ICON\XP4Life\part-a\generated\
```

## Step 2 - Select the Good Icons

Do not use every generated image.

Pick the strongest results and copy them into `selected/`.

Suggested naming:

```text
xp4l-quest-scroll.png
xp4l-quest-compass.png
xp4l-achievement-medal.png
xp4l-title-crown.png
xp4l-reward-coin.png
```

Keep names lowercase, simple, and stable.

## Step 3 - Use Icons Inside Notes

Embed an icon in a note:

```md
![[ICON/XP4Life/part-a/selected/quests/xp4l-quest-scroll.png]]
```

Use a smaller visual card:

```md
| Icon | XP4L Item | Type |
| --- | --- | --- |
| ![[ICON/XP4Life/part-a/selected/quests/xp4l-quest-scroll.png\|64]] | Daily Quest | Quest |
```

## Step 4 - Use Icons in Explorer Tree

For file and folder icons, use the Iconic community plugin.

Required plugin:

```text
Plugin name: Iconic
Plugin ID: iconic
Purpose: customize icons and colors for files, folders, tabs, bookmarks, tags, properties, and ribbon commands
```

Iconic is best for assigning icons inside Obsidian's file explorer and UI.

Important limitation:

- Iconic is excellent for assigning built-in Obsidian/Lucide-style icons and colors.
- For generated PNG artwork, keep the PNGs in notes, dashboards, and gallery pages first.
- If PNG-as-tree-icon support is needed later, test that separately before making it the core method.

## Step 5 - Transfer to Another Vault

To move the icon set into the XP4Life vault:

1. Copy the folder:

```text
ICON\XP4Life\part-a\
```

2. Paste it into the target vault root.

3. Copy this guide or the quick use guide into:

```text
NOTE\
```

4. Install or enable the required plugin if file explorer icons are needed:

```text
iconic
```

5. Update note embeds if the target vault uses a different folder path.

## Transfer Package Checklist

- `ICON/XP4Life/part-a/selected/`
- `ICON/XP4Life/part-a/prompts/`
- `NOTE/Icons - part A - quick use guide.md`
- `NOTE/How to - Create XP4Life Icon set (obsidian).md`
- optional: `run-icons-part-a.bat`

## Best Current Method

Use generated PNG icons as visual assets inside notes first.

Use Iconic for file/folder UI icons where built-in symbolic icons are enough.

If the goal becomes fully custom PNG icons in the file explorer, make that a separate test task instead of assuming every plugin supports it cleanly.
