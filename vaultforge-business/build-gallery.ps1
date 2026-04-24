param(
    [string]$GeneratedRoot = (Join-Path $PSScriptRoot "generated"),
    [string]$OutFile = "",
    [int]$Limit = 0
)

$ErrorActionPreference = "Stop"
$imageExtensions = @(".png", ".jpg", ".jpeg", ".webp")

function Format-Html {
    param([AllowNull()][object]$Value)

    if ($null -eq $Value) { return "" }
    return [System.Net.WebUtility]::HtmlEncode([string]$Value)
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

function ConvertTo-RelativeWebPath {
    param(
        [string]$FromDirectory,
        [string]$ToPath
    )

    $fromUri = [System.Uri]::new(([System.IO.Path]::GetFullPath($FromDirectory).TrimEnd("\") + "\"))
    $toUri = [System.Uri]::new([System.IO.Path]::GetFullPath($ToPath))
    return [System.Uri]::UnescapeDataString($fromUri.MakeRelativeUri($toUri).ToString())
}

try {
    $rootPath = (Resolve-Path -LiteralPath $GeneratedRoot -ErrorAction Stop).Path
}
catch {
    Write-Host "Generated root not found: $GeneratedRoot" -ForegroundColor Red
    exit 1
}

if ([string]::IsNullOrWhiteSpace($OutFile)) {
    $OutFile = Join-Path $rootPath "_gallery\index.html"
}
$outFileFull = $ExecutionContext.SessionState.Path.GetUnresolvedProviderPathFromPSPath($OutFile)
$outDir = Split-Path -Parent $outFileFull

$manifestFiles = @(Get-ChildItem -LiteralPath $rootPath -Recurse -Filter "gallery-entry.json" -File | Sort-Object FullName)
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

    $images = @(Get-ChildItem -LiteralPath $runDir -File | Where-Object {
        $imageExtensions -contains $_.Extension.ToLowerInvariant()
    } | Sort-Object Name)

    $contactSheet = Join-Path $runDir "contact-sheet.jpg"
    $preview = ""
    if (Test-Path -LiteralPath $contactSheet) {
        $preview = $contactSheet
    }
    elseif ($images.Count -gt 0) {
        $preview = $images[0].FullName
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
        Preset = Get-FirstValue $entry @("preset", "business_preset", "preset_slug") "preset"
        Style = Get-FirstValue $entry @("style", "business_styles", "primary_style_slug") "style"
        Job = Get-FirstValue $entry @("job", "job_slug") "manual"
        Tag = Get-FirstValue $entry @("tag", "tag_slug") ""
        ImageCount = $images.Count
        Preview = $preview
        RunDir = $runDir
        Manifest = $manifestFile.FullName
    })
}

$sortedRows = @($rows.ToArray() | Sort-Object Client, Asset, Preset, Style, CreatedDate -Descending)
if ($Limit -gt 0) {
    $sortedRows = @($sortedRows | Select-Object -First $Limit)
}

if (-not (Test-Path -LiteralPath $outDir)) {
    New-Item -ItemType Directory -Force -Path $outDir | Out-Null
}

$clients = @($rows.ToArray() | Select-Object -ExpandProperty Client -Unique | Sort-Object)
$imageTotal = 0
foreach ($row in $rows) {
    $imageTotal += [int]$row.ImageCount
}

$html = New-Object System.Collections.Generic.List[string]
$html.Add("<!doctype html>")
$html.Add("<html lang=""en"">")
$html.Add("<head>")
$html.Add("  <meta charset=""utf-8"">")
$html.Add("  <meta name=""viewport"" content=""width=device-width, initial-scale=1"">")
$html.Add("  <title>VaultForge Business Gallery</title>")
$html.Add("  <style>")
$html.Add("    body { margin: 0; font-family: Segoe UI, Arial, sans-serif; background: #f7f7f4; color: #232323; }")
$html.Add("    header { padding: 28px 32px 18px; background: #ffffff; border-bottom: 1px solid #deded8; }")
$html.Add("    h1 { margin: 0 0 8px; font-size: 28px; }")
$html.Add("    .meta { color: #666; font-size: 14px; }")
$html.Add("    main { padding: 24px 32px 40px; }")
$html.Add("    .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 18px; }")
$html.Add("    .card { background: #fff; border: 1px solid #d7d7d0; border-radius: 8px; overflow: hidden; }")
$html.Add("    .thumb { display: block; width: 100%; aspect-ratio: 4 / 3; object-fit: cover; background: #ecece6; }")
$html.Add("    .empty { display: flex; align-items: center; justify-content: center; width: 100%; aspect-ratio: 4 / 3; background: #ecece6; color: #777; }")
$html.Add("    .body { padding: 14px 14px 16px; }")
$html.Add("    h2 { margin: 0 0 8px; font-size: 18px; }")
$html.Add("    dl { display: grid; grid-template-columns: 76px 1fr; gap: 5px 10px; margin: 0; font-size: 13px; }")
$html.Add("    dt { color: #666; }")
$html.Add("    dd { margin: 0; }")
$html.Add("    a { color: #0f5f75; text-decoration: none; }")
$html.Add("    a:hover { text-decoration: underline; }")
$html.Add("  </style>")
$html.Add("</head>")
$html.Add("<body>")
$html.Add("  <header>")
$html.Add("    <h1>VaultForge Business Gallery</h1>")
$html.Add("    <div class=""meta"">Generated $(Format-Html (Get-Date -Format 'yyyy-MM-dd HH:mm:ss')) from $(Format-Html $rootPath). Runs: $($rows.Count). Images: $imageTotal. Clients: $($clients.Count).</div>")
$html.Add("  </header>")
$html.Add("  <main>")
$html.Add("    <div class=""grid"">")

foreach ($row in $sortedRows) {
    $runLink = ConvertTo-RelativeWebPath $outDir $row.RunDir
    $manifestLink = ConvertTo-RelativeWebPath $outDir $row.Manifest
    $previewMarkup = "<div class=""empty"">No images yet</div>"
    if (-not [string]::IsNullOrWhiteSpace($row.Preview)) {
        $previewLink = ConvertTo-RelativeWebPath $outDir $row.Preview
        $previewMarkup = "<a href=""$(Format-Html $runLink)""><img class=""thumb"" src=""$(Format-Html $previewLink)"" alt=""$(Format-Html ($row.Client + ' ' + $row.Asset))""></a>"
    }

    $html.Add("      <article class=""card"">")
    $html.Add("        $previewMarkup")
    $html.Add("        <div class=""body"">")
    $html.Add("          <h2>$(Format-Html $row.Client)</h2>")
    $html.Add("          <dl>")
    $html.Add("            <dt>Asset</dt><dd>$(Format-Html $row.Asset)</dd>")
    $html.Add("            <dt>Preset</dt><dd>$(Format-Html $row.Preset)</dd>")
    $html.Add("            <dt>Style</dt><dd>$(Format-Html $row.Style)</dd>")
    $html.Add("            <dt>Job</dt><dd>$(Format-Html $row.Job)</dd>")
    $html.Add("            <dt>Tag</dt><dd>$(Format-Html $row.Tag)</dd>")
    $html.Add("            <dt>Images</dt><dd>$($row.ImageCount)</dd>")
    $html.Add("            <dt>Created</dt><dd>$(Format-Html $row.Created)</dd>")
    $html.Add("            <dt>Files</dt><dd><a href=""$(Format-Html $runLink)"">run folder</a> / <a href=""$(Format-Html $manifestLink)"">manifest</a></dd>")
    $html.Add("          </dl>")
    $html.Add("        </div>")
    $html.Add("      </article>")
}

$html.Add("    </div>")
if ($warnings.Count -gt 0) {
    $html.Add("    <h2>Warnings</h2>")
    $html.Add("    <ul>")
    foreach ($warning in $warnings) {
        $html.Add("      <li>$(Format-Html $warning)</li>")
    }
    $html.Add("    </ul>")
}
$html.Add("  </main>")
$html.Add("</body>")
$html.Add("</html>")

($html.ToArray() -join [Environment]::NewLine) | Out-File -FilePath $outFileFull -Encoding utf8
Write-Host "Gallery written: $outFileFull" -ForegroundColor Green
