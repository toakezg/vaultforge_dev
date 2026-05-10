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
    [Alias("ArtRoot")][string]$EngineRoot = "",
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
        "business-icon" { "business-icon" }
        "business-cover" { "business-cover" }
        "social-brand-tile" { "social-brand-tile" }
        "brand-board" { "brand-board" }
        default { "vaultforge" }
    }
}

function Get-EngineStyle {
    param([string]$BusinessStyle)
    switch ($BusinessStyle) {
        "clean-corporate" { "clean-corporate" }
        "luxury-minimal" { "fine-line" }
        "modern-startup" { "modern-startup" }
        "bold-retro-brand" { "pixel" }
        "friendly-flat" { "geometric" }
        "premium-3d" { "photoreal" }
        "mono-mark" { "fine-line" }
        "vector-crisp" { "vector-crisp" }
        "editorial-brand" { "editorial-brand" }
        "neon-signage" { "cinematic" }
        default { "geometric" }
    }
}

function Get-EngineConstraints {
    param([string[]]$BusinessMods, [switch]$TransparentSafe)

    $allowed = @(
        "high-contrast",
        "print-safe",
        "small-size-readable",
        "transparent-bg-ready"
    )
    $constraints = New-Object System.Collections.Generic.List[string]

    foreach ($businessMod in @($BusinessMods)) {
        if ($allowed -contains $businessMod -and -not $constraints.Contains($businessMod)) {
            $constraints.Add($businessMod)
        }
    }

    if ($TransparentSafe -and -not $constraints.Contains("transparent-bg-ready")) {
        $constraints.Add("transparent-bg-ready")
    }

    return @($constraints.ToArray())
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
    if ($InputImage) { $parts += "Input image supplied to shared engine: $InputImage." }
    if ($ReferenceImage) { $parts += "Reference image supplied to shared engine: $ReferenceImage." }

    $parts += ""
    $parts += $Prompt
    return ($parts -join [Environment]::NewLine)
}

if ($Variants -lt 1) {
    Write-Host "Variants must be 1 or greater." -ForegroundColor Red
    exit 1
}

if ([string]::IsNullOrWhiteSpace($EngineRoot)) {
    $EngineRoot = Join-Path $PSScriptRoot "..\vaultforge-engine"
}
$EngineRoot = Get-FullPath $EngineRoot

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
$inputImageEnginePath = if ([string]::IsNullOrWhiteSpace($InputImage)) { "" } else { Get-FullPath $InputImage }
$referenceImageEnginePath = if ([string]::IsNullOrWhiteSpace($ReferenceImage)) { "" } else { Get-FullPath $ReferenceImage }

$runDir = Join-Path $OutputRoot (Join-Path $clientSlug (Join-Path $assetSlug (Join-Path $presetSlug (Join-Path $styleSlug (Join-Path $dateSlug "job-$jobSlug")))))
$runDirFull = Get-FullPath $runDir
$writeRunFiles = (-not $DryRun) -or $WriteMetadata

$composedPrompt = Get-BusinessPrompt
$promptPath = Join-Path $runDir "prompt.txt"
$promptPathFull = Get-FullPath $promptPath

$sourcePromptPath = ""
$enginePreset = Get-EnginePreset $Preset
$engineStyle = Get-EngineStyle ($Style | Select-Object -First 1)
$engineConstraints = @(Get-EngineConstraints -BusinessMods $Mod -TransparentSafe:$TransparentSafe)
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
    engine_constraints = $engineConstraints
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
    input_image_resolved = $inputImageEnginePath
    reference_image = $ReferenceImage
    reference_image_resolved = $referenceImageEnginePath
    note = "input_image and reference_image are passed to the shared engine when supplied; tweak remains business prompt context until a shared tweak/edit contract exists."
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

$filenameBits = @($clientSlug, $assetSlug, $presetSlug, $styleSlug)
if ($tagSlug -ne "tag") { $filenameBits += $tagSlug }
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
    "--filename", $filename,
    "--client", $Client,
    "--job", $Job,
    "--variants", ([string]$Variants)
)

if (-not [string]::IsNullOrWhiteSpace($Tag)) {
    $args += @("--tag", $Tag)
}

foreach ($engineConstraint in $engineConstraints) {
    $args += @("--constraint", $engineConstraint)
}

if (-not [string]::IsNullOrWhiteSpace($inputImageEnginePath)) {
    $args += @("--input-image", $inputImageEnginePath)
}

if (-not [string]::IsNullOrWhiteSpace($referenceImageEnginePath)) {
    $args += @("--reference-image", $referenceImageEnginePath)
}

if ($DryRun) { $args += "--dry-run" }

Write-Host ""
Write-Host "VaultForge Business -> Shared engine" -ForegroundColor Cyan
if ($Variants -gt 1) {
    Write-Host "Business variants: $Variants"
}
Write-Host "Business output: $runDirFull"

if ($DryRun -and -not $WriteMetadata) {
    Write-Host "Engine dry-run scratch output: $engineOutputDir"
}

if ($WhatIf) {
    Write-Host ("py " + (ConvertTo-DisplayCommand $args))
}
else {
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
