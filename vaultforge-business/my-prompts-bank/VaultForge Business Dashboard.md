---
dashboard: vaultforge-business
status: active
---

# VaultForge Business Dashboard

## Draft Queue

```dataview
table client, asset_type, preset, styles, mods, tags, job, rating
from "my-prompts-bank"
where file.folder != "my-prompts-bank/_template"
where status = "draft" or !status
sort client asc, asset_type asc, file.name asc
```

## Ready To Review

```dataview
table client, asset_type, preset, styles, tags, job, rating, image
from "my-prompts-bank"
where file.folder != "my-prompts-bank/_template"
where status = "generated" or status = "review"
sort rating desc, file.mtime desc
```

## By Client

```dataview
table rows.file.link as prompts
from "my-prompts-bank"
where file.folder != "my-prompts-bank/_template"
group by client
sort key asc
```

## Style Signals

```dataview
table client, asset_type, preset, job, rating
from "my-prompts-bank"
where file.folder != "my-prompts-bank/_template"
where contains(styles, "luxury-minimal") or contains(styles, "vector-crisp") or contains(styles, "clean-corporate")
sort rating desc, file.mtime desc
```

## Image Field Gallery

Add an `image:` path to a prompt note after review, then use this table as the
lightweight visual index.

```dataview
table client, asset_type, preset, embed(link(image)) as preview, rating
from "my-prompts-bank"
where file.folder != "my-prompts-bank/_template"
where image
sort file.mtime desc
```
