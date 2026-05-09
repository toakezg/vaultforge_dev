# Business Paid Launch Decision Note

Date: 2026-05-10

## Purpose

This note prepares the Nath-facing decisions needed before VaultForge Business
is treated as a real paid or public service.

It does not approve pricing, licensing, publication, legal claims, commercial
rights promises, live client generation, automated delivery, or cross-lane
engine registry changes. It gives Nath a short decision surface so the next
operator pass can move cleanly instead of mixing product taste, business risk,
and tooling work in one thread.

## Current State

VaultForge Business is now ready for controlled client-style test packages, but
not yet ready to be broadly published as a finished paid service.

Already in place:

- client-facing wrapper lane separated from the art playground
- markdown prompt-bank workflow and non-runnable client intake template
- business-owned `run.json` and `gallery-entry.json` manifests
- dry-run and `-WhatIf` paths for safe previews
- service catalog for current presets, styles, and mods
- generated-output review checklist
- delivery package skeleton with client README template
- gallery, contact-sheet, and review-summary surfaces

Still decision-bound:

- pricing model
- public service positioning
- licensing and usage-rights wording
- publication channel and portfolio examples
- whether live paid/API generation is allowed for a named pilot job
- whether the first offer is private beta, soft launch, or public listing

## Recommended Launch Posture

Recommended first posture:

```text
Private paid pilot / controlled beta
```

This fits the current system because the workflow is structured enough to run a
real client-style job, but still benefits from Nath reviewing output quality,
packaging language, file naming, and revision handling before public promises
are made.

Avoid starting with:

- fully public marketplace listing
- broad agency-style design claims
- guaranteed trademark-safe logo service
- exact typography promises
- print-production guarantees
- fully automated client intake and delivery

## Decision 1 - Service Positioning

Choose one primary service identity for the first paid-facing version.

Option A - Brand asset starter packs:

- Best fit for the current lane.
- Covers logo directions, icons, covers, brand boards, and social tiles.
- Lets the service catalog and delivery skeleton work together.
- Recommended.

Option B - Icon and symbol packs:

- Narrower and easier to review.
- Strong fit for creators, apps, games, communities, and symbolic systems.
- Better if Nath wants the lowest-risk first public promise.

Option C - General AI design service:

- Too broad for the current proof level.
- Creates unclear pricing, rights, quality, and revision expectations.
- Not recommended yet.

Recommendation: start with Option A, with Option B as the first niche offer
inside it.

## Decision 2 - Pricing Shape

Pick the pricing model before writing any public sales copy.

Option A - Fixed pilot package:

- One small price for one defined starter pack.
- Easiest to explain and easiest to review.
- Good for the first few real clients.

Example internal shape:

```text
Starter pack: intake, one prompt-pack pass, curated selections, delivery folder,
source archive, and one revision note pass.
```

Option B - Tiered packages:

- Small / standard / expanded.
- Better later, after the pilot package exposes real timing and cleanup cost.

Option C - Hourly or custom quote only:

- Flexible, but less productized.
- Useful for complex clients, not ideal as the first repeatable offer.

Recommendation: use a fixed pilot package first, then derive tiers from real
job evidence.

## Decision 3 - Licensing And Usage Rights

This must be approved before any public or client-facing claim is used.

Minimum safe wording direction:

- describe what files are included
- describe intended use in plain language
- avoid promising trademark clearance
- avoid promising exclusive ownership unless specifically reviewed
- avoid claiming print readiness unless actual export checks were done
- keep source prompts and manifests archived for reproducibility

Decision needed from Nath:

```text
Should the first packages say "client may use delivered final assets for their
own brand, social, community, or project materials after review approval" while
explicitly excluding trademark/legal clearance guarantees?
```

Recommendation: yes, but treat final wording as a separate approval before it
appears in a client package.

## Decision 4 - Publication Channel

Choose the first public surface carefully.

Option A - Private outreach only:

- Lowest risk.
- Best while the package language and output quality are still being tested.
- Recommended first.

Option B - Portfolio/examples page:

- Good after at least 2-3 reviewed example packages exist.
- Needs clear example/client/privacy labels.

Option C - Public paid listing:

- Higher expectation burden.
- Wait until pricing, terms, examples, revision policy, and delivery standards
  are settled.

Recommendation: start with private outreach or a private pilot note, then build
portfolio examples from reviewed internal/demo packages.

## Decision 5 - Live Generation Approval

Nath has approved live generation and paid/API use for passing the current
Workflow B blocker. This note does not run generation by itself.

Before any live paid/API generation for a client-style package, record:

- client or demo client name
- job name
- prompt-bank path
- expected asset types
- max variants or run count
- budget ceiling
- output folder
- whether results are for internal review, private client review, or public use

Recommended first live run shape:

```text
one demo or pilot client
one starter pack
limited variants
review-only output
manual curation before packaging
```

## Decision 6 - Revision Policy

Pick a simple revision rule before taking paid work.

Recommended pilot rule:

```text
One included revision note pass after the first curated review set.
Extra direction changes become a new mini-brief or follow-up package.
```

Reason: this keeps the service from becoming open-ended while the workflow is
still being measured.

## Decision 7 - Client Privacy And Examples

Before publishing examples, decide whether examples are:

- internal demo only
- anonymized client-style examples
- real client work with permission
- public portfolio pieces

Recommendation: use demo or internal examples first. Do not publish real client
names, briefs, references, or outputs without explicit permission.

## Approval Checklist

Nath can use this checklist as the launch gate:

- [ ] Choose first service identity: starter packs, icon/symbol packs, or other.
- [ ] Choose first pricing shape: fixed pilot, tiers, or quote-only.
- [ ] Approve or revise client usage-rights wording.
- [ ] Choose first publication channel: private outreach, portfolio examples, or public listing.
- [ ] Approve the first live generation pilot scope and budget.
- [ ] Choose a revision policy.
- [ ] Choose whether examples are demo, anonymized, real-client, or public.

## Recommended 0 Or 1 Decision

If Nath wants the simplest next decision:

```text
0 = Keep VaultForge Business private/internal for now. Do not run a paid pilot.
1 = Approve one private paid-pilot/demo package with fixed scope, limited live
    generation, manual review, no public listing, and no legal/trademark claims.
```

Recommended answer: `1`, if the pilot scope is written before generation and
the first package remains private/review-only until Nath approves the wording
and selected outputs.

## Next Safe Action After Approval

If Nath chooses `1`, the next business-local action should be:

```text
Create one pilot package brief from `my-prompts-bank\_intake\client-intake-template.md`,
preview it with `-WhatIf`, run a dry-run, then request/record the exact live
generation budget and output path before any paid/API generation.
```

If Nath chooses `0`, the next safe action should be:

```text
Create 2-3 internal demo packages from existing prompt-bank examples and use
the output review checklist plus delivery skeleton to prove the workflow without
public launch pressure.
```
