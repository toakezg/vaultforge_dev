# Client pack runner

Files:
- run-client-pack.bat - quick launcher
- run-client-pack.ps1 - main runner
- logo-pack.txt - logo exploration batch
- icon-pack.txt - icon exploration batch
- cover-pack.txt - cover exploration batch
- pack-dryrun-safe.txt - single-direction dry-run fixture
- pack-dryrun-safe.json - structured dry-run fixture
- my-prompts-bank\README.md - prompt-bank inventory and maintenance notes
- run_business.bat / run_business.ps1 - business lane wrapper

## Basic usage

run-client-pack.bat "Empower You Plan Management" "empower-you" "logo-pack-01" "round1" ".\logo-pack.txt"

## With tweak text
The business wrapper supports -Tweak, so pack lines can use {TWEAK} and pass a sixth argument:

___
run-client-pack.bat "Empower You Plan Management" "empower-you" "logo-pack-01" "round2" ".\logo-pack.txt" "cleaner lines, stronger symbol"

## Direct PowerShell options

powershell -ExecutionPolicy Bypass -File .\run-client-pack.ps1 ^
  -InputValue "Empower You Plan Management" ^
  -Client "empower-you" ^
  -Project "logo-pack-01" ^
  -Tag "round1" ^
  -PromptFile ".\logo-pack.txt" ^
  -WhatIf
_____________________________________________________________

## the aboove powershell prompt builder - EDIT BELOW

powershell -ExecutionPolicy Bypass -File .\run-client-pack.ps1 ^
  -InputValue "Radio Show" ^
  -Client "Jubal" ^
  -Project "icon-pack-01" ^
  -Tag "test-003" ^
  -PromptFile ".\icon-pack.txt" ^
  -WWhatIf
_____________________________________________________________



Other switches:
- -WhatIf
- -StopOnError
- -PauseBetween
- -DelaySeconds 2

## Safer structured packs

Text packs still work by default. They are simple, but placeholders are expanded
inside a command-shaped line, so quote-heavy client input can make the line hard
to parse safely.

JSON packs opt into a structured format:

{
  "formatVersion": 1,
  "commands": [
    {
      "command": ".\\run_business.ps1",
      "args": [
        "{INPUT}",
        "-Client", "{CLIENT}",
        "-AssetType", "logo",
        "-Job", "{PROJECT}",
        "-Tag", "{TAG}",
        "-Preset", "business-logo",
        "-Style", "modern-startup",
        "-Mod", "trustworthy",
        "-Tweak", "{TWEAK}",
        "-DryRun"
      ]
    }
  ]
}

Each argument is expanded separately and passed as an argv value. This avoids
requiring pack authors to choose shell quotes around placeholders.

Dry-run the safe example:

powershell -ExecutionPolicy Bypass -File .\run-client-pack.ps1 ^
  -InputValue "Empower ""You"" Plan Management" ^
  -Client "empower-you" ^
  -Project "safe-pack-smoke" ^
  -Tag "round1" ^
  -PromptFile ".\pack-dryrun-safe.json" ^
  -Tweak "cleaner ""quote-safe"" lines" ^
  -WhatIf

## Logging

The runner writes a CSV log to:

.\logs\run-log.csv

Each row stores:
- timestamp
- client
- project (maps to `job` in `run_business.ps1`)
- tag
- input
- prompt file
- command
- status
- exit code

Rows are written through PowerShell CSV serialization so comma-heavy values like
`local, premium` stay in one column for downstream review.

## Business output

Pack commands now call `run_business.ps1`, which routes output to:

generated\{client_slug}\{asset_slug}\{business_preset_slug}\{primary_style_slug}\{date}\job-{job_slug}\

This keeps client work separate from the VaultForge Art playground output.

## Prompt bank maintenance

Keep the root pack filenames stable while `run-client-pack.ps1` reads plain text command packs directly. Add reusable markdown prompt notes under `my-prompts-bank` instead of adding more loose root text files, and check `my-prompts-bank\README.md` before changing pack categories or naming.
