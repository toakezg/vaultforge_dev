# mini-stiks Design

## Summary

`mini-stiks` is a lane-local subdirectory inside `vaultforge-image` that gives
the user a quick way to generate small sticker-oriented images without
repeating the same prompt constraints every time.

This first pass stays wrapper-only. The shared engine already supports `--size`
and `--quality`, so the new work should reuse those flags instead of widening
the engine contract.

## Goals

- Add a `mini-stiks` launcher surface under `vaultforge-image\mini-stiks\`.
- Support three size modes:
  - `micro` -> `256x256`
  - `small` -> `384x384`
  - `medium` -> `512x512`
- Force `--quality high` for all `mini-stiks` runs.
- Prepend a built-in mini-sticker prompt brief so the user does not need to
  repeat the same constraints on every run.
- Keep `mini-stiks` input/output routing inside a lane-local
  `vaultforge-image\mini-stiks\i-o\` tree.
- Add `--batch` support for folder-based runs.
- Make the first pass easy to test with dry-run and one live smoke run.

## Non-Goals

- No shared engine changes in this pass.
- No pool system yet.
- No loop launcher implementation yet.
- No future engine alias work unless the wrapper-only approach proves too
  narrow later.

## Design

### Launcher shape

Create a dedicated launcher in `vaultforge-image\mini-stiks\` that acts as a
thin wrapper around the existing image lane launcher.

The canonical user-facing form should be:

```text
run_mini_stiks.bat --mini-stiks micro "user prompt here"
run_mini_stiks.bat --mini-stiks small "user prompt here"
run_mini_stiks.bat --mini-stiks medium "user prompt here"
run_mini_stiks.bat --batch
```

The launcher should:

- parse the `--mini-stiks` mode
- map the mode to the correct `--size`
- add `--quality high`
- prepend the built-in sticker brief to the user prompt
- forward the final args into the existing lane image path
- when `--batch` is used, read prompt files from the lane-local active input
  folder

### Prompt composition

The built-in brief should be treated as a fixed wrapper fragment, not as a
user-editable per-run prompt decoration.

Canonical brief:

```text
Generate a high quality image that will be used as a mini sized sticker
(approx 20mm x 20mm). Keep the image simple and uncrowded. The color palette
should be black/white and/or greys/grey-washed.
```

The composed prompt order should be:

1. built-in mini-sticker brief
2. user prompt

That order keeps the run focused on sticker constraints first while still
letting the user control the subject.

### Pathing and I/O layout

The `mini-stiks` sublane should use its own lane-local pathing system so the
user can keep the input/output structure consistent and easy to follow.

Expected structure:

```text
.\i-o\in
.\i-o\in\active        (default)
.\i-o\in\templates
.\i-o\in\archive

.\i-o\out
.\i-o\out\generated    (default)
.\i-o\out\runs         (not yet implemented)
.\i-o\out\runs\*.json  (not yet implemented)
```

For the first pass:

- `.\i-o\in\active` is the default batch input folder
- `.\i-o\out\generated` is the default output folder
- `runs\` and its JSON contents are reserved for later

### Output and routing

The new launcher should not write directly to the lane root output folder for
this sublane. It should route through the `mini-stiks\i-o\` tree so the
sub-lane can keep its own input and output organization.

If filename prefixes or other mode markers are needed for clarity, they should
stay lightweight and local to the launcher. The wrapper should not force a new
directory layout in this pass.

### Files expected in scope

- `vaultforge-image\mini-stiks\run_mini_stiks.bat`
- `vaultforge-image\mini-stiks\README.md`
- `vaultforge-image\mini-stiks\mini-stiks_idea-build.txt`
- `vaultforge-image\mini-stiks\i-o\`
- `vaultforge-image\CHANGELOG.md`
- `vaultforge-image\README.md`

The existing idea note remains the source seed for the mini-stiks contract.

## Verification

The first pass should be verified in two layers:

1. Dry-run for each mode
   - `--mini-stiks micro`
   - `--mini-stiks small`
   - `--mini-stiks medium`
   - confirm the composed prompt contains the sticker brief
   - confirm the size maps to the expected value
   - confirm `--quality high` is always present
2. Live smoke run
   - run one low-risk sample prompt in a single mode
   - confirm the lane key is used
   - confirm an image is written under `vaultforge-image\mini-stiks\i-o\out\generated\`
   - confirm the mode-specific prompt behavior is visible in the run output or
     sidecar metadata if present

## Follow-Up

Once the wrapper-only pass is stable, the next rescope candidate is the pool
system.

If the wrapper feels too narrow for future reuse, the later option is to move
the shared `mini-stiks` preset shape into the engine and keep the launcher as a
thin mode translator.
