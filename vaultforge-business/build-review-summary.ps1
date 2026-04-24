param(
    [string]$GeneratedRoot = (Join-Path $PSScriptRoot "generated"),
    [string]$OutFile = "",
    [int]$Limit = 0
)

$ErrorActionPreference = "Stop"
$imageExtensions = @(".png", ".jpg", ".jpeg", ".webp")

function Format-TableCell {
    param([AllowNull()][object]$Value)

    if ($null -eq $Value) { return "" }

    $text = [string]$Value
    $text = $text.Replace("`r", " ").Replace("`n", " ")
    $text = $text.Replace("|", "\|")
    if ($text.Length -eq 0) { return "" }

    return $text
}

function Get-FirstValue {
    param(
        [object]$Entry,
        [string[]]$Names,
        [string]$Fallback = ""
    )

    foreach ($name in $Names) {
        if ($Entry.PSObject.Properties.Name -contains $name) {
            $value = $Entry.$name
            if ($null -eq $value) { continue }

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

$rootPath = $null
try {
    $rootPath = (Resolve-Path -LiteralPath $GeneratedRoot -ErrorAction Stop).Path
}
catch {
    Write-Host "Generated root not found: $GeneratedRoot" -ForegroundColor Red
    exit 1
}

$manifestFiles = @(Get-ChildItem -LiteralPath $rootPath -Recurse -Filter "gallery-entry.json" -File)
$rows = New-Object System.Collections.Generic.List[object]
$warnings = New-Object System.Collections.Generic.List[string]

foreach ($manifestFile in $manifestFiles) {
    try {
        $entry = Get-Content -Raw -LiteralPath $manifestFile.FullName | ConvertFrom-Json
    }
    catch {
        $warnings.Add("Could not read $($manifestFile.FullName): $($_.Exception.Message)")
        continue
    }

    $runDir = Get-FirstValue $entry @("run_dir") $manifestFile.DirectoryName
    if (-not (Test-Path -LiteralPath $runDir)) {
        $runDir = $manifestFile.DirectoryName
    }

    $images = @()
    if (Test-Path -LiteralPath $runDir) {
        $images = @(Get-ChildItem -LiteralPath $runDir -File | Where-Object { $imageExtensions -contains $_.Extension.ToLowerInvariant() })
    }

    $createdText = Get-FirstValue $entry @("created", "timestamp") ""
    $createdDate = [datetime]::MinValue
    if (-not [string]::IsNullOrWhiteSpace($createdText)) {
        [void][datetime]::TryParse($createdText, [ref]$createdDate)
    }

    $rows.Add([pscustomobject]@{
        Created = $createdText
        CreatedDate = $createdDate
        Client = Get-FirstValue $entry @("client", "client_slug") "unsorted"
        Asset = Get-FirstValue $entry @("asset_type", "asset_slug") "brand"
        Preset = Get-FirstValue $entry @("preset", "business_preset", "preset_slug", "business_preset_slug") "preset"
        Style = Get-FirstValue $entry @("style", "business_styles", "primary_style_slug") "style"
        Job = Get-FirstValue $entry @("job", "job_slug") "manual"
        Tag = Get-FirstValue $entry @("tag", "tag_slug") ""
        ImageCount = $images.Count
        FirstImage = if ($images.Count -gt 0) { ($images | Sort-Object Name | Select-Object -First 1).Name } else { "" }
        RunDir = $runDir
        Manifest = $manifestFile.FullName
    })
}

$allRows = @($rows.ToArray())
$sortedRows = @($allRows | Sort-Object CreatedDate, Client, Asset, Preset, Style -Descending)
if ($Limit -gt 0) {
    $sortedRows = @($sortedRows | Select-Object -First $Limit)
}

$clients = @($allRows | Select-Object -ExpandProperty Client -Unique | Sort-Object)
$jobs = @($allRows | Select-Object -ExpandProperty Job -Unique | Sort-Object)
$imageTotal = 0
foreach ($row in $allRows) {
    $imageTotal += [int]$row.ImageCount
}

$lines = New-Object System.Collections.Generic.List[string]
$lines.Add("# VaultForge Business Review Summary")
$lines.Add("")
$lines.Add("Generated: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')")
$lines.Add("Source root: $rootPath")
$lines.Add("")
$lines.Add("## Totals")
$lines.Add("")
$lines.Add("- Runs: $($allRows.Count)")
$lines.Add("- Image files: $imageTotal")
$lines.Add("- Clients: $($clients.Count)")
$lines.Add("- Jobs: $($jobs.Count)")
$lines.Add("")
$lines.Add("## Runs")
$lines.Add("")
$lines.Add("| Created | Client | Asset | Preset | Style | Job | Tag | Images | First image | Run dir |")
$lines.Add("| --- | --- | --- | --- | --- | --- | --- | ---: | --- | --- |")

foreach ($row in $sortedRows) {
    $runLine = "| {0} | {1} | {2} | {3} | {4} | {5} | {6} | {7} | {8} | {9} |" -f `
        (Format-TableCell $row.Created),
        (Format-TableCell $row.Client),
        (Format-TableCell $row.Asset),
        (Format-TableCell $row.Preset),
        (Format-TableCell $row.Style),
        (Format-TableCell $row.Job),
        (Format-TableCell $row.Tag),
        (Format-TableCell $row.ImageCount),
        (Format-TableCell $row.FirstImage),
        (Format-TableCell $row.RunDir)
    $lines.Add($runLine)
}

if ($warnings.Count -gt 0) {
    $lines.Add("")
    $lines.Add("## Warnings")
    $lines.Add("")
    foreach ($warning in $warnings) {
        $lines.Add("- $warning")
    }
}

if ($Limit -gt 0 -and $allRows.Count -gt $sortedRows.Count) {
    $lines.Add("")
    $lines.Add("Showing $($sortedRows.Count) of $($allRows.Count) runs. Re-run without -Limit for the full summary.")
}

$summaryText = $lines.ToArray() -join [Environment]::NewLine

if (-not [string]::IsNullOrWhiteSpace($OutFile)) {
    $outParent = Split-Path -Parent $OutFile
    if (-not [string]::IsNullOrWhiteSpace($outParent) -and -not (Test-Path -LiteralPath $outParent)) {
        New-Item -ItemType Directory -Force -Path $outParent | Out-Null
    }

    $summaryText | Out-File -FilePath $OutFile -Encoding utf8
    Write-Host "Review summary written: $OutFile" -ForegroundColor Green
}
else {
    Write-Output $summaryText
}
