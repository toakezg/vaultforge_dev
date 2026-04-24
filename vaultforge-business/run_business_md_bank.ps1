param(
    [string]$Path = ".\my-prompts-bank",
    [string]$OutputRoot = ".\generated",
    [string]$EngineRoot = "E:\tools\vaultforge\vaultforge-engine",
    [string]$Status = "draft",
    [int]$Limit = 0,
    [switch]$All,
    [switch]$IncludeTemplates,
    [switch]$DryRun,
    [switch]$WriteMetadata,
    [switch]$WhatIf,
    [switch]$StopOnError
)

$ErrorActionPreference = "Stop"

function ConvertFrom-FrontMatterScalar {
    param([AllowNull()][string]$Value)

    if ($null -eq $Value) { return "" }
    $text = $Value.Trim()
    if (($text.StartsWith('"') -and $text.EndsWith('"')) -or ($text.StartsWith("'") -and $text.EndsWith("'"))) {
        return $text.Substring(1, $text.Length - 2)
    }

    return $text
}

function ConvertFrom-SimpleFrontMatter {
    param([string]$Content)

    $lines = $Content -split "`r?`n"
    $metadata = @{}
    $bodyStart = 0

    if ($lines.Count -gt 0 -and $lines[0].Trim() -eq "---") {
        $frontMatterEnd = -1
        for ($i = 1; $i -lt $lines.Count; $i++) {
            if ($lines[$i].Trim() -eq "---") {
                $frontMatterEnd = $i
                break
            }
        }

        if ($frontMatterEnd -gt 0) {
            $currentKey = ""
            $listKeys = @("styles", "mods", "tags")

            for ($i = 1; $i -lt $frontMatterEnd; $i++) {
                $line = $lines[$i]
                if ([string]::IsNullOrWhiteSpace($line)) { continue }
                if ($line.TrimStart().StartsWith("#")) { continue }

                if ($line -match "^\s*([A-Za-z_][A-Za-z0-9_-]*)\s*:\s*(.*)$") {
                    $currentKey = $matches[1]
                    $value = ConvertFrom-FrontMatterScalar $matches[2]
                    if ([string]::IsNullOrWhiteSpace($value) -and ($listKeys -contains $currentKey)) {
                        $metadata[$currentKey] = New-Object System.Collections.ArrayList
                    }
                    else {
                        $metadata[$currentKey] = $value
                    }
                    continue
                }

                if ($line -match "^\s*-\s*(.*)$" -and -not [string]::IsNullOrWhiteSpace($currentKey)) {
                    if (-not ($metadata[$currentKey] -is [System.Collections.ArrayList])) {
                        $priorValue = $metadata[$currentKey]
                        $metadata[$currentKey] = New-Object System.Collections.ArrayList
                        if (-not [string]::IsNullOrWhiteSpace([string]$priorValue)) {
                            [void]$metadata[$currentKey].Add([string]$priorValue)
                        }
                    }

                    [void]$metadata[$currentKey].Add((ConvertFrom-FrontMatterScalar $matches[1]))
                }
            }

            foreach ($key in @($metadata.Keys)) {
                if ($metadata[$key] -is [System.Collections.ArrayList]) {
                    $metadata[$key] = @($metadata[$key].ToArray())
                }
            }

            $bodyStart = $frontMatterEnd + 1
        }
    }

    $bodyLines = New-Object System.Collections.Generic.List[string]
    for ($i = $bodyStart; $i -lt $lines.Count; $i++) {
        $bodyLines.Add($lines[$i])
    }

    while ($bodyLines.Count -gt 0 -and [string]::IsNullOrWhiteSpace($bodyLines[0])) {
        $bodyLines.RemoveAt(0)
    }

    if ($bodyLines.Count -gt 0 -and $bodyLines[0] -match "^\s*#\s+") {
        $bodyLines.RemoveAt(0)
        while ($bodyLines.Count -gt 0 -and [string]::IsNullOrWhiteSpace($bodyLines[0])) {
            $bodyLines.RemoveAt(0)
        }
    }

    return [pscustomobject]@{
        Metadata = $metadata
        Prompt = ($bodyLines.ToArray() -join [Environment]::NewLine).Trim()
    }
}

function Get-MetadataText {
    param(
        [hashtable]$Metadata,
        [string[]]$Names,
        [string]$Fallback = ""
    )

    foreach ($name in $Names) {
        if ($Metadata.ContainsKey($name)) {
            $value = $Metadata[$name]
            if ($value -is [System.Array]) {
                $items = @($value | Where-Object { -not [string]::IsNullOrWhiteSpace([string]$_) })
                if ($items.Count -gt 0) { return ($items -join ", ") }
            }
            elseif (-not [string]::IsNullOrWhiteSpace([string]$value)) {
                return [string]$value
            }
        }
    }

    return $Fallback
}

function Get-MetadataArray {
    param(
        [hashtable]$Metadata,
        [string]$Name,
        [string[]]$Fallback = @()
    )

    if (-not $Metadata.ContainsKey($Name)) { return @($Fallback) }

    $value = $Metadata[$Name]
    if ($value -is [System.Array]) {
        return @($value | Where-Object { -not [string]::IsNullOrWhiteSpace([string]$_) })
    }

    if ([string]::IsNullOrWhiteSpace([string]$value)) { return @($Fallback) }
    return @(([string]$value -split "," | ForEach-Object { $_.Trim() } | Where-Object { -not [string]::IsNullOrWhiteSpace($_) }))
}

function Get-MetadataBool {
    param(
        [hashtable]$Metadata,
        [string]$Name
    )

    if (-not $Metadata.ContainsKey($Name)) { return $false }
    $text = ([string]$Metadata[$Name]).Trim().ToLowerInvariant()
    return @("1", "true", "yes", "y", "on") -contains $text
}

function Test-IsPromptBankNote {
    param([hashtable]$Metadata)

    if ($Metadata.ContainsKey("dashboard")) { return $false }

    $promptKeys = @(
        "client",
        "asset_type",
        "asset",
        "preset",
        "business_preset",
        "styles",
        "mods",
        "tags",
        "tag",
        "job",
        "project",
        "status"
    )

    foreach ($key in $promptKeys) {
        if ($Metadata.ContainsKey($key)) { return $true }
    }

    return $false
}

function Format-Argument {
    param([AllowNull()][string]$Value)

    if ($null -eq $Value) { return "''" }
    if ($Value.Length -eq 0 -or $Value -match "\s" -or $Value.Contains('"') -or $Value.Contains("'")) {
        return "'" + $Value.Replace("'", "''") + "'"
    }

    return $Value
}

function ConvertTo-DisplayCommand {
    param([string[]]$Arguments)

    return (($Arguments | ForEach-Object { Format-Argument $_ }) -join " ")
}

$resolvedPath = $null
try {
    $resolvedPath = (Resolve-Path -LiteralPath $Path -ErrorAction Stop).Path
}
catch {
    Write-Host "Markdown bank path not found: $Path" -ForegroundColor Red
    exit 1
}

if ((Get-Item -LiteralPath $resolvedPath) -is [System.IO.DirectoryInfo]) {
    $promptFiles = @(Get-ChildItem -LiteralPath $resolvedPath -Recurse -File -Include "*.md", "*.markdown")
}
else {
    $promptFiles = @((Get-Item -LiteralPath $resolvedPath))
}

if (-not $IncludeTemplates) {
    $promptFiles = @($promptFiles | Where-Object { $_.FullName -notmatch "\\_template(\\|$)" })
}

$promptFiles = @($promptFiles | Sort-Object FullName)
if ($Limit -gt 0) {
    $promptFiles = @($promptFiles | Select-Object -First $Limit)
}

if ($promptFiles.Count -eq 0) {
    Write-Host "No markdown prompt files found under: $resolvedPath" -ForegroundColor Yellow
    exit 0
}

$businessScript = Join-Path $PSScriptRoot "run_business.ps1"
$ranCount = 0
$skippedCount = 0
$failedCount = 0

foreach ($file in $promptFiles) {
    $parsed = ConvertFrom-SimpleFrontMatter (Get-Content -Raw -LiteralPath $file.FullName)
    $metadata = $parsed.Metadata
    $prompt = $parsed.Prompt

    if (-not (Test-IsPromptBankNote $metadata)) {
        Write-Host "Skipping non-prompt markdown: $($file.FullName)"
        $skippedCount++
        continue
    }

    if ([string]::IsNullOrWhiteSpace($prompt)) {
        Write-Host "Skipping empty prompt body: $($file.FullName)" -ForegroundColor Yellow
        $skippedCount++
        continue
    }

    $noteStatus = Get-MetadataText $metadata @("status") ""
    if (-not $All -and -not [string]::IsNullOrWhiteSpace($Status)) {
        if ([string]::IsNullOrWhiteSpace($noteStatus) -or $noteStatus.ToLowerInvariant() -ne $Status.ToLowerInvariant()) {
            Write-Host "Skipping status '$noteStatus': $($file.FullName)"
            $skippedCount++
            continue
        }
    }

    $client = Get-MetadataText $metadata @("client") "unsorted"
    $assetType = Get-MetadataText $metadata @("asset_type", "asset") "brand"
    $job = Get-MetadataText $metadata @("job", "project") ([System.IO.Path]::GetFileNameWithoutExtension($file.Name))
    $preset = Get-MetadataText $metadata @("preset", "business_preset") "business-logo"
    $styles = @(Get-MetadataArray $metadata "styles" @("clean-corporate"))
    $mods = @(Get-MetadataArray $metadata "mods" @())
    $tags = Get-MetadataText $metadata @("tags", "tag") ""
    $size = Get-MetadataText $metadata @("size") "1024x1024"
    $quality = Get-MetadataText $metadata @("quality") "medium"
    $format = Get-MetadataText $metadata @("format") "png"
    $background = Get-MetadataText $metadata @("background") "auto"
    $variantsText = Get-MetadataText $metadata @("variants") "1"
    $variants = 1
    if (-not [int]::TryParse($variantsText, [ref]$variants) -or $variants -lt 1) {
        $variants = 1
    }

    $runArgs = New-Object System.Collections.Generic.List[string]
    $runArgs.Add("-NoProfile")
    $runArgs.Add("-ExecutionPolicy")
    $runArgs.Add("Bypass")
    $runArgs.Add("-File")
    $runArgs.Add($businessScript)
    $runArgs.Add($prompt)
    $runArgs.Add("-Client")
    $runArgs.Add($client)
    $runArgs.Add("-AssetType")
    $runArgs.Add($assetType)
    $runArgs.Add("-Job")
    $runArgs.Add($job)
    $runArgs.Add("-Tag")
    $runArgs.Add($tags)
    $runArgs.Add("-Preset")
    $runArgs.Add($preset)
    $runArgs.Add("-Style")
    $runArgs.Add(($styles -join ","))
    if ($mods.Count -gt 0) {
        $runArgs.Add("-Mod")
        $runArgs.Add(($mods -join ","))
    }
    $runArgs.Add("-Variants")
    $runArgs.Add([string]$variants)
    $runArgs.Add("-Size")
    $runArgs.Add($size)
    $runArgs.Add("-Quality")
    $runArgs.Add($quality)
    $runArgs.Add("-Format")
    $runArgs.Add($format)
    $runArgs.Add("-Background")
    $runArgs.Add($background)
    $runArgs.Add("-OutputRoot")
    $runArgs.Add($OutputRoot)
    $runArgs.Add("-EngineRoot")
    $runArgs.Add($EngineRoot)
    $runArgs.Add("-SourcePromptFile")
    $runArgs.Add($file.FullName)

    $tweak = Get-MetadataText $metadata @("tweak") ""
    if (-not [string]::IsNullOrWhiteSpace($tweak)) {
        $runArgs.Add("-Tweak")
        $runArgs.Add($tweak)
    }

    $inputImage = Get-MetadataText $metadata @("input_image") ""
    if (-not [string]::IsNullOrWhiteSpace($inputImage)) {
        $runArgs.Add("-InputImage")
        $runArgs.Add($inputImage)
    }

    $referenceImage = Get-MetadataText $metadata @("reference_image") ""
    if (-not [string]::IsNullOrWhiteSpace($referenceImage)) {
        $runArgs.Add("-ReferenceImage")
        $runArgs.Add($referenceImage)
    }

    if ((Get-MetadataBool $metadata "transparent_safe") -or ($background.ToLowerInvariant() -eq "transparent")) {
        $runArgs.Add("-TransparentSafe")
    }

    if ($DryRun) {
        $runArgs.Add("-DryRun")
    }

    if ($WriteMetadata) {
        $runArgs.Add("-WriteMetadata")
    }

    Write-Host ""
    Write-Host "Markdown bank prompt: $($file.FullName)" -ForegroundColor Cyan
    Write-Host "Client=$client Asset=$assetType Preset=$preset Styles=$($styles -join ', ') Job=$job"

    if ($WhatIf) {
        Write-Host ("powershell " + (ConvertTo-DisplayCommand $runArgs.ToArray()))
        $ranCount++
        continue
    }

    & powershell @($runArgs.ToArray()) | Out-Host
    $exitCode = if ($null -eq $LASTEXITCODE) { 0 } else { $LASTEXITCODE }
    if ($exitCode -ne 0) {
        $failedCount++
        Write-Host "Markdown prompt failed with exit code $exitCode`: $($file.FullName)" -ForegroundColor Red
        if ($StopOnError) { exit $exitCode }
    }
    else {
        $ranCount++
    }
}

Write-Host ""
Write-Host "Markdown bank complete. Ran: $ranCount Skipped: $skippedCount Failed: $failedCount" -ForegroundColor Green
if ($failedCount -gt 0) {
    exit 1
}
