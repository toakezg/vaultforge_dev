# VaultForge Icons - Branch Plan

## Intent

VaultForge Icons is the broader commercial/client-facing branch that grows out of the XP4Life icon pipeline.

XP4Life Icons proves the local generation workflow.

VaultForge Icons turns the same method into reusable icon packs, logo directions, client folders, stats, delivery notes, and possible side-hustle workflows.

## Working Name

```text
Name: VaultForge Icons
ID: vaultforge-icons
```

## Recommended Direction

Build this as a branch of the existing art workflow, not as a totally separate engine at first.

Recommended shape:

```text
vaultforge-art
  presets/profiles: logo, icon, business, client pack

vaultforge
  docs, prompts, client templates, launchers, generated assets
```

Do this in phases:

1. Use the XP4Life pipeline as the proof.
2. Add client template and storage docs.
3. Add usage/cost tracking.
4. Add image-input and tweak support.
5. Add price guide and ad copy once the workflow feels repeatable.

## CLI Ideas

Possible future flags:

```bat
--vaultforge-icon
--profile business
--profile logo
--profile xp4life
--many 5
--quality high
--client "client-slug"
--output-dir ".\clients\client-slug\generated"
```

Possible future image-reference flags:

```bat
--input-image "E:\path\reference.png"
--input-image-prompt "Use the same broad shape but make it yellow and cleaner"
--tweak "keep the icon shape, make the background purple"
--tweak-background remove
--tweak-background-color "#6B3FF2"
```

## Image Input Notes

OpenAI's current image generation docs support image references and image edits, including input images, masks, background control, quality settings, and input fidelity.

Planning implication:

- `--input-image` is a valid future direction.
- `--tweak` should be treated as edit-mode behavior, not the same as plain generation.
- usage tracking should count input image tokens separately from output image tokens.

Docs checked:

- https://developers.openai.com/api/docs/guides/image-generation

## Client Template

Recommended format: YAML first.

YAML is easier to edit by hand in Obsidian than JSON, and it can still be parsed later.

```yaml
client:
  slug: toakezg
  name: Toakezg
  preferred_name: Toa
  business_name: Toa & Kez Pty
  industry: creative tools
  services:
    - icon generation
    - logo concepts
  website: https://example.com
  vibe: taking it easy, playful, clean
  contact: toa@example.com
  attachments:
    - reference.png

job:
  paid_status: unpaid
  package: starter
  profile: business
  quantity_requested: 5
  notes: ""
```

## Info Storage

Recommended client folder:

```text
clients\
  client-slug\
    client.yaml
    prompt.md
    references\
    generated\
    selected\
    delivery\
    usage.csv
    notes.md
```

Track:

- client info
- generated images
- selected images
- prompt/settings used
- paid/unpaid status
- package bought
- feedback/revision notes
- final delivery files

## Stats To Track

Track per:

- icon
- bundle/pack
- preset
- style
- profile
- client

Useful fields:

- prompt text tokens
- input image tokens
- output image tokens
- estimated cost
- actual price charged
- time spent
- generated count
- selected count
- delivered count
- ad source
- lead status
- client status

## Reference Docs To Add

- `Reference/VaultForge Icons - price guide.md`
- `Reference/VaultForge Icons - facebook ads.md`
- `Reference/VaultForge Icons - usage stats.md`
- `Reference/VaultForge Icons - client template.md`

## Recommendation

Do not build all of this at once.

The next smart step is a small Part B:

1. Package the best XP4Life outputs into `selected/`.
2. Write one clean client template.
3. Add a simple usage CSV shape.
4. Add one business/logo prompt pack.
5. Test one fake client job end to end.
