# System

## Role

This folder is the operator lane for business and client work. It should stay thin, clear, and wrapper-oriented.

It is also a promoted section in the root/section thread model. Business threads should read root overhead context first, then work from this folder.

## Boundaries

- `vaultforge-engine` is the intended stable image generation engine.
- `vaultforge-art` is the art and playground lane.
- `vaultforge-business` is the client workflow, prompt bank, output router, and gallery/index layer.
- Do not duplicate the generation engine here.
- Keep Windows batch usage first-class.
- Prefer markdown prompt banks over loose text prompt lists.
- Update `CHANGELOG.md` for business changes and root `CHANGELOG.md` when business changes affect cross-lane coordination or engine contracts.
- Use `SIGN_UP.md` so dedicated business threads can leave a compact role/handoff trace.
- Every business task line must include at least one section tag and one task-type tag, for example `#business #docs`, `#business #gallery`, or `#business #clients`.
- Active and next business tasks should use Obsidian Tasks priority markers by business-local importance: 🔺 highest, ⏫ high, 🔼 medium, 🔽 low, ⏬ lowest. Leave no marker only for unranked inbox or backlog tasks.
- Active and next business tasks should also carry a short stable `🆔` id so `before this` and `after this` links stay usable.
- Use `🔁` only for genuine recurring work. Prefer `when done` for recurring maintenance or review loops.
- Use `⛔ task-id` for `before this` dependencies, and express `after this` by linking the follow-up task back to the current task's `🆔`.
- Hold `due`, `scheduled`, `start`, and `created` for a later rules pass.
- `TASKS.md` should keep an automatic `tasks` code block filtered with `tag includes business` above manual task sections.

## Lane Ownership

Keep these lane-owned until they prove stable:

- business prompt-bank templates and reusable prompt notes
- client/job/tag naming guidance
- business presets, styles, and mods
- business output routing and gallery/index metadata
- wrapper-only bridge fields such as `tweak`, `input_image`, and `reference_image`

Candidates to share later:

- slug creation once engine-native `--client`, `--job`, and `--tag` fields exist
- stable preset/style/mod fragment libraries
- generic gallery manifest fields used by both business and art lanes
- direct edit/reference image API support

## Naming Rules

- `client`, `asset_type`, and `job` are raw operator-facing metadata fields.
- `client_slug`, `asset_slug`, and `job_slug` are generated folder-safe fields for sorting.
- Folder names use slug fields; metadata keeps both raw and slug values.
- Use kebab-case for names when possible. Avoid punctuation-heavy client and job names.
- `Project` in the pack runner is a legacy batch name and maps to `job`.

## Business Presets

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

## Business Styles

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

## Business Mods

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

## Tag Rule

Tags are data until injected into the prompt. The wrapper injects `-Tag` as industry and sorting context so tags like `barber`, `plumber`, `carpenter`, or `air-balloon-pilot` can influence the image request.

Use short comma-separated tag strings in runnable packs, preferably without
spaces. Markdown prompt-bank templates keep `tags` as a YAML list until the
future markdown runner flattens them for `-Tag`.
