# Delivery Package Skeleton

This folder is the reusable VaultForge Business delivery package skeleton.

Copy the folder shape into a real client package only after outputs have been
reviewed and selected. Keep generated outputs, source prompts, business
manifests, engine sidecars, and delivery notes together so a future operator can
rebuild the reasoning behind the package.

## Folder Map

- `exports/final/` - final approved PNG/JPG/WebP/SVG files for client delivery.
- `exports/transparent/` - transparent-background exports.
- `exports/social/` - social profile, banner, tile, and platform-size exports.
- `exports/print/` - high-resolution or print-safe exports when approved.
- `previews/` - contact sheets, quick previews, and client browsing images.
- `usage-notes/` - client-facing notes copied or adapted from `CLIENT_README.md`.
- `sources/prompts/` - source prompt notes and copied `prompt.source.md` files.
- `sources/manifests/` - `run.json`, `gallery-entry.json`, and sidecar copies.
- `sources/references/` - approved input/reference images used for the job.
- `review/contact-sheets/` - internal review sheets used during selection.
- `review/selected/` - curated picks before final export packaging.
- `archive/` - older package versions, rejected alternates, or superseded files.

## Rules

- Do not put unreviewed raw generations directly into `exports/final/`.
- Keep client-facing notes in plain language and avoid engine or prompt jargon.
- Keep source prompts and manifests for reproducibility even when they are not
  sent to the client.
- Do not add pricing, licensing, public-use, or commercial rights wording until
  Nath approves it for the package.
