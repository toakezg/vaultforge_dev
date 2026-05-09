# Business Client Ready Criteria

Date: 2026-05-09

## Purpose

This note defines what "finished and primed for real client use" means for the
VaultForge Business lane.

It turns the current `business-if-done.txt` direction into a business-owned
readiness target without treating it as approval to publish, price, sell, or
run live generation for clients. Those remain Nath-facing launch decisions.

## Current Read

VaultForge Business is approaching production-capable infrastructure, not yet a
finished paid-service product.

The strong base is already present:

- business wrappers separate client work from playground and art output
- markdown prompt banks can store reusable client packs
- dry-run and WhatIf paths are safer than the original manual workflow
- business manifests preserve client, job, tag, preset, style, and mod metadata
- gallery, contact-sheet, and review-summary tools can browse generated output
- image and reference inputs now pass through to the shared engine

The remaining jump is standardization, packaging discipline, launch readiness,
and repeatable client delivery.

## Working Definition

VaultForge Business is client-ready when it can reliably turn a client request
into a reviewed delivery package with minimal manual disorder.

The practical test is:

```text
client brief
-> intake note
-> prompt pack
-> generation or dry-run review
-> curated selections
-> export/package folders
-> delivery README
-> archived manifests and prompts
```

For paid use, the system should feel like a dependable production workflow, not
only a creative experiment that can generate interesting images.

## Minimum Client-Ready Criteria

- Product identity is clear: brand assets for small businesses, creators, and
  structured visual systems, with logos, icons, covers, brand boards, social
  tiles, and symbolic asset packs as the main offer.
- Intake is repeatable: a client request has a markdown template that captures
  business name, audience, asset types, style direction, colors, references,
  usage needs, and delivery expectations.
- Presets behave like products: the useful business presets, styles, and mods
  have short descriptions, best-use notes, and example prompt-bank references.
- Output quality has a review threshold: selections should be coherent,
  readable, commercially usable, and low-artifact enough to present publicly.
- Packaging exists: each client job can produce a clean delivery folder with
  exports, previews, source prompts/manifests, usage notes, and a README.
- Reproducibility is preserved: prompts, source notes, run manifests, gallery
  entries, sidecar provenance, references, and selected outputs stay archived.
- Turnaround is measurable: a simple client pack can move from intake to first
  review in a short, documented workflow.
- Human taste remains explicit: curation, rejection, rating, and final picks are
  part of the process instead of pretending the pipeline is fully autonomous.
- Launch docs exist: operator README, delivery standards, package structure,
  preset catalog, and review checklist are written enough for future Nath or a
  Codex thread to run the lane consistently.

## Product Boundaries

Good first paid-service lane:

- logos and brand marks
- app or community icons
- social tiles and covers
- brand boards
- symbolic or game-adjacent asset packs
- small client identity starter packs

Hold for later:

- broad agency-style brand strategy
- print production guarantees
- trademark/legal claims
- fully automated client submission or delivery
- cross-lane engine fragment migration without root/engine approval

## Next Safe Business Slices

1. Add a client intake markdown template under the business prompt-bank system.
2. Add a delivery package skeleton with folders and a client-facing README
   template.
3. Create a preset/style/mod service catalog from the current business wrapper
   names and prompt-bank usage.
4. Add a review checklist for selecting client-ready outputs from gallery
   entries and contact sheets.
5. Prepare a Nath decision note for pricing, public positioning, licensing, and
   publication before any paid launch.

## Hard Gates

Stop for Nath/root/engine approval before:

- pricing or public paid-service publication
- license, terms, or commercial-use claims
- live generation when costs or external API use are not explicitly approved
- moving business fragments into shared engine registries
- changing cross-lane ownership or output contracts

## Resume Prompt

```text
Continue Workflow B for vaultforge-business. Read
vaultforge-business/BUSINESS_CLIENT_READY_CRITERIA.md, then take the next safe
business-local slice: add either a client intake markdown template or a delivery
package skeleton. Keep changes inside vaultforge-business, do not run live
generation, and leave pricing/publication decisions as Nath gates.
```
