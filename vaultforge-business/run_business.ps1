param(
    [Parameter(Mandatory=$true, Position=0)][string]$Prompt,
    [string]$Client = "unsorted",
    [string]$AssetType = "brand",
    [string]$Job = "manual",
    [string]$Tag = "",
    [string]$Preset = "business-logo",
    [string[]]$Style = @("clean-corporate"),
    [string[]]$Mod = @(),
    [int]$Variants = 1,
    [string]$Size = "1024x1024",
    [ValidateSet("low","medium","high")][string]$Quality = "medium",
    [ValidateSet("jpeg","png","webp")][string]$Format = "png",
    [ValidateSet("auto","transparent","opaque")][string]$Background = "auto",
    [switch]$TransparentSafe,
    [string]$Tweak = "",
    [string]$InputImage = "",
    [string]$ReferenceImage = "",
    [string]$SourcePromptFile = "",
    [string]$OutputRoot = ".\generated",
    [Alias("ArtRoot")][string]$EngineRoot = "E:\tools\vaultforge\vaultforge-engine",
    [switch]$DryRun,
    [switch]$WriteMetadata,
    [switch]$WhatIf
)

function ConvertTo-Slug {
    param([string]$Value, [string]$Fallback = "item")
    $slug = $Value.ToLowerInvariant()
    $slug = $slug -replace "[^a-z0-9]+", "-"
    $slug = $slug.Trim("-")
    if ([string]::IsNullOrWhiteSpace($slug)) { return $Fallback }
    return $slug
}

function Get-FullPath {
    param([string]$Path)
    return $ExecutionContext.SessionState.Path.GetUnresolvedProviderPathFromPSPath($Path)
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

function Get-EnginePreset {
    param([string]$BusinessPreset)
    switch ($BusinessPreset) {
        "business-icon" { "icon" }
        "business-cover" { "obsidian-cover" }
        "social-brand-tile" { "artifact-card" }
        "brand-board" { "artifact-card" }
        default { "vaultforge" }
    }
}

function Get-EngineStyle {
    param([string]$BusinessStyle)
    switch ($BusinessStyle) {
        "luxury-minimal" { "fine-line" }
        "modern-startup" { "geometric" }
        "bold-retro-brand" { "pixel" }
        "friendly-flat" { "geometric" }
        "premium-3d" { "photoreal" }
        "mono-mark" { "fine-line" }
        "vector-crisp" { "geometric" }
        "editorial-brand" { "painterly" }
        "neon-signage" { "cinematic" }
        default { "geometric" }
    }
}

function ConvertTo-ValueList {
    param([string[]]$Values)

    $items = New-Object System.Collections.Generic.List[string]
    foreach ($value in @($Values)) {
        if ([string]::IsNullOrWhiteSpace([string]$value)) { continue }
        foreach ($part in ([string]$value -split ",")) {
            $trimmed = $part.Trim()
            if (-not [string]::IsNullOrWhiteSpace($trimmed)) {
                $items.Add($trimmed)
            }
        }
    }

    return @($items.ToArray())
}

function Get-BusinessPrompt {
    $styleText = ($Style | Where-Object { -not [string]::IsNullOrWhiteSpace($_) }) -join ", "
    $modText = ($Mod | Where-Object { -not [string]::IsNullOrWhiteSpace($_) }) -join ", "
    $tagText = $Tag

    $parts = @(
        "Client: $Client."
        "Asset type: $AssetType."
        "Business preset: $Preset."
    )

    if ($styleText) { $parts += "Business styles: $styleText." }
    if ($modText) { $parts += "Business modifiers: $modText." }
    if ($tagText) { $parts += "Tags and industry context: $tagText." }
    if ($TransparentSafe) {
        $parts += "Make the result transparent-background friendly, readable at small sizes, and avoid mockup scenes."
    }
    if ($Tweak) { $parts += "Tweak request: $Tweak." }
    if ($InputImage) { $parts += "Input image path noted for future edit workflow: $InputImage." }
    if ($ReferenceImage) { $parts += "Reference image path noted for future reference workflow: $ReferenceImage." }

    $parts += ""
    $parts += $Prompt
    return ($parts -join [Environment]::NewLine)
}

if ($Variants -lt 1) {
    Write-Host "Variants must be 1 or greater." -ForegroundColor Red
    exit 1
}

if (-not (Test-Path $EngineRoot)) {
    Write-Host "VaultForge Engine root not found: $EngineRoot" -ForegroundColor Red
    exit 1
}

$Style = @(ConvertTo-ValueList $Style)
if ($Style.Count -eq 0) { $Style = @("clean-corporate") }
$Mod = @(ConvertTo-ValueList $Mod)

$clientSlug = ConvertTo-Slug $Client "unsorted"
$assetSlug = ConvertTo-Slug $AssetType "brand"
$presetSlug = ConvertTo-Slug $Preset "preset"
$primaryStyle = (($Style | Select-Object -First 1) -join " ")
$styleSlug = ConvertTo-Slug $primaryStyle "style"
$jobSlug = ConvertTo-Slug $Job "manual"
$tagSlug = ConvertTo-Slug $Tag "tag"
$metadataTagSlug = if ([string]::IsNullOrWhiteSpace($Tag)) { "" } else { $tagSlug }
$dateSlug = Get-Date -Format "yyyy-MM-dd"

$runDir = Join-Path $OutputRoot (Join-Path $clientSlug (Join-Path $assetSlug (Join-Path $presetSlug (Join-Path $styleSlug (Join-Path $dateSlug "job-$jobSlug")))))
$runDirFull = Get-FullPath $runDir
$writeRunFiles = (-not $DryRun) -or $WriteMetadata

$composedPrompt = Get-BusinessPrompt
$promptPath = Join-Path $runDir "prompt.txt"
$promptPathFull = Get-FullPath $promptPath

$sourcePromptPath = ""
$enginePreset = Get-EnginePreset $Preset
$engineStyle = Get-EngineStyle ($Style | Select-Object -First 1)
$effectiveBackground = if ($TransparentSafe) { "transparent" } else { $Background }
$engineOutputDir = $runDirFull
$dryRunTempRoot = ""
if ($DryRun -and -not $WriteMetadata) {
    $dryRunTempRoot = Join-Path ([System.IO.Path]::GetTempPath()) ("vaultforge-business-dryrun-" + [System.Guid]::NewGuid().ToString("N"))
    $engineOutputDir = $dryRunTempRoot
}

$metadata = [ordered]@{
    timestamp = (Get-Date).ToString("s")
    client = $Client
    client_slug = $clientSlug
    asset_type = $AssetType
    asset_slug = $assetSlug
    job = $Job
    job_slug = $jobSlug
    tag = $Tag
    tag_slug = $metadataTagSlug
    business_preset = $Preset
    business_preset_slug = $presetSlug
    business_styles = $Style
    primary_style_slug = $styleSlug
    business_mods = $Mod
    engine_preset = $enginePreset
    engine_style = $engineStyle
    variants = $Variants
    size = $Size
    quality = $Quality
    format = $Format
    background = $effectiveBackground
    output_dir = $runDirFull
    prompt_file = $promptPathFull
    source_prompt_file = $sourcePromptPath
    tweak = $Tweak
    input_image = $InputImage
    reference_image = $ReferenceImage
    note = "input_image, reference_image, and tweak are prompt-level bridge fields until the shared engine supports edit APIs directly."
}

$galleryEntry = [ordered]@{
    client = $Client
    client_slug = $clientSlug
    asset_type = $AssetType
    asset_slug = $assetSlug
    preset = $Preset
    preset_slug = $presetSlug
    style = $Style
    primary_style_slug = $styleSlug
    tag = $Tag
    tag_slug = $metadataTagSlug
    job = $Job
    job_slug = $jobSlug
    run_dir = $runDirFull
    created = (Get-Date).ToString("s")
}

if ($writeRunFiles -and -not $WhatIf) {
    New-Item -ItemType Directory -Force -Path $runDirFull | Out-Null
    $composedPrompt | Out-File -FilePath $promptPathFull -Encoding utf8

    if (-not [string]::IsNullOrWhiteSpace($SourcePromptFile)) {
        if (Test-Path -LiteralPath $SourcePromptFile) {
            $sourcePromptPath = (Resolve-Path -LiteralPath $SourcePromptFile).Path
            Copy-Item -LiteralPath $sourcePromptPath -Destination (Join-Path $runDirFull "prompt.source.md") -Force
            $metadata["source_prompt_file"] = $sourcePromptPath
        }
        else {
            Write-Host "Source prompt file not found, continuing without prompt.source.md: $SourcePromptFile" -ForegroundColor Yellow
        }
    }

    $metadata | ConvertTo-Json -Depth 6 | Out-File -FilePath (Join-Path $runDirFull "run.json") -Encoding utf8
    $galleryEntry | ConvertTo-Json -Depth 6 | Out-File -FilePath (Join-Path $runDirFull "gallery-entry.json") -Encoding utf8
}
elseif ($DryRun -and -not $WhatIf) {
    Write-Host "Dry run: business metadata is not written. Add -WriteMetadata to keep prompt/run/gallery files." -ForegroundColor Yellow
}

for ($i = 1; $i -le $Variants; $i++) {
    $variant = "{0:D2}" -f $i
    $filenameBits = @($clientSlug, $assetSlug, $presetSlug, $styleSlug)
    if ($tagSlug -ne "tag") { $filenameBits += $tagSlug }
    $filenameBits += "v$variant"
    $filename = ($filenameBits -join "__")

    $args = @(
        ".\src\generate.py",
        $composedPrompt,
        "--preset", $enginePreset,
        "--style", $engineStyle,
        "--size", $Size,
        "--quality", $Quality,
        "--format", $Format,
        "--background", $effectiveBackground,
        "--output-dir", $engineOutputDir,
        "--filename", $filename
    )

    if ($DryRun) { $args += "--dry-run" }

    Write-Host ""
    Write-Host "VaultForge Business -> Shared engine variant $variant" -ForegroundColor Cyan
    Write-Host "Business output: $runDirFull"

    if ($DryRun -and -not $WriteMetadata) {
        Write-Host "Engine dry-run scratch output: $engineOutputDir"
    }

    if ($WhatIf) {
        Write-Host ("py " + (ConvertTo-DisplayCommand $args))
        continue
    }

    Push-Location $EngineRoot
    try {
        & py @args
        $exitCode = $LASTEXITCODE
    }
    finally {
        Pop-Location
    }

    if ($exitCode -ne 0) {
        if ($dryRunTempRoot -and (Test-Path -LiteralPath $dryRunTempRoot)) {
            Remove-Item -LiteralPath $dryRunTempRoot -Recurse -Force
        }
        Write-Host "Shared engine failed with exit code $exitCode" -ForegroundColor Red
        exit $exitCode
    }
}

if ($dryRunTempRoot -and (Test-Path -LiteralPath $dryRunTempRoot)) {
    Remove-Item -LiteralPath $dryRunTempRoot -Recurse -Force
}

Write-Host ""
if ($WhatIf) {
    Write-Host "Business what-if complete. No files were written." -ForegroundColor Green
}
elseif ($DryRun -and -not $WriteMetadata) {
    Write-Host "Business dry run complete. No business files were written." -ForegroundColor Green
}
else {
    Write-Host "Business run complete: $runDirFull" -ForegroundColor Green
}
