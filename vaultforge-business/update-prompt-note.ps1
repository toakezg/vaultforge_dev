param(
    [string]$PromptPath = "",
    [string]$RunDir = "",
    [string]$Status = "generated",
    [string]$Image = "",
    [string]$Rating = "",
    [string]$Notes = "",
    [switch]$WhatIf
)

$ErrorActionPreference = "Stop"
$imageExtensions = @(".png", ".jpg", ".jpeg", ".webp")

function ConvertTo-RelativeVaultPath {
    param([string]$Path)

    $root = [System.IO.Path]::GetFullPath($PSScriptRoot).TrimEnd("\") + "\"
    $full = [System.IO.Path]::GetFullPath($Path)
    $rootUri = [System.Uri]::new($root)
    $pathUri = [System.Uri]::new($full)
    return [System.Uri]::UnescapeDataString($rootUri.MakeRelativeUri($pathUri).ToString()).Replace("/", "\")
}

function Format-YamlScalar {
    param([AllowNull()][string]$Value)

    if ([string]::IsNullOrWhiteSpace($Value)) { return "" }
    if ($Value -match "^[A-Za-z0-9_.\\/-]+$") { return $Value }

    return "'" + $Value.Replace("'", "''") + "'"
}

function Set-FrontMatterValue {
    param(
        [System.Collections.Generic.List[string]]$Lines,
        [string]$Key,
        [string]$Value
    )

    $replacement = if ([string]::IsNullOrWhiteSpace($Value)) { "${Key}:" } else { "${Key}: $(Format-YamlScalar $Value)" }
    for ($i = 1; $i -lt $Lines.Count; $i++) {
        if ($Lines[$i].Trim() -eq "---") { break }
        if ($Lines[$i] -match ("^\s*" + [regex]::Escape($Key) + "\s*:")) {
            $Lines[$i] = $replacement
            return
        }
    }

    $insertAt = 1
    for ($i = 1; $i -lt $Lines.Count; $i++) {
        if ($Lines[$i].Trim() -eq "---") {
            $insertAt = $i
            break
        }
    }
    $Lines.Insert($insertAt, $replacement)
}

if (-not [string]::IsNullOrWhiteSpace($RunDir)) {
    $runDirFull = (Resolve-Path -LiteralPath $RunDir -ErrorAction Stop).Path
    $runJson = Join-Path $runDirFull "run.json"
    if ((Test-Path -LiteralPath $runJson) -and [string]::IsNullOrWhiteSpace($PromptPath)) {
        $run = Get-Content -Raw -LiteralPath $runJson | ConvertFrom-Json
        if ($run.PSObject.Properties.Name -contains "source_prompt_file" -and -not [string]::IsNullOrWhiteSpace([string]$run.source_prompt_file)) {
            $PromptPath = [string]$run.source_prompt_file
        }
    }

    if ([string]::IsNullOrWhiteSpace($Image)) {
        $firstImage = @(Get-ChildItem -LiteralPath $runDirFull -File | Where-Object {
            ($imageExtensions -contains $_.Extension.ToLowerInvariant()) -and $_.Name -ne "contact-sheet.jpg"
        } | Sort-Object Name | Select-Object -First 1)
        if ($firstImage.Count -gt 0) {
            $Image = ConvertTo-RelativeVaultPath $firstImage[0].FullName
        }
    }
}

if ([string]::IsNullOrWhiteSpace($PromptPath)) {
    Write-Host "Provide -PromptPath or a -RunDir with run.json source_prompt_file." -ForegroundColor Red
    exit 1
}

$promptPathFull = (Resolve-Path -LiteralPath $PromptPath -ErrorAction Stop).Path
$content = Get-Content -Raw -LiteralPath $promptPathFull
$rawLines = New-Object System.Collections.Generic.List[string]
foreach ($line in ($content -split "`r?`n", -1)) {
    $rawLines.Add($line)
}

if ($rawLines.Count -eq 0 -or $rawLines[0].Trim() -ne "---") {
    $rawLines.Insert(0, "---")
    $rawLines.Insert(1, "---")
}
else {
    $frontMatterEnd = -1
    for ($i = 1; $i -lt $rawLines.Count; $i++) {
        if ($rawLines[$i].Trim() -eq "---") {
            $frontMatterEnd = $i
            break
        }
    }
    if ($frontMatterEnd -lt 0) {
        $rawLines.Insert(1, "---")
    }
}

if (-not [string]::IsNullOrWhiteSpace($Status)) { Set-FrontMatterValue $rawLines "status" $Status }
if (-not [string]::IsNullOrWhiteSpace($Image)) { Set-FrontMatterValue $rawLines "image" $Image }
if (-not [string]::IsNullOrWhiteSpace($Rating)) { Set-FrontMatterValue $rawLines "rating" $Rating }
if (-not [string]::IsNullOrWhiteSpace($Notes)) { Set-FrontMatterValue $rawLines "notes" $Notes }

$updated = $rawLines.ToArray() -join [Environment]::NewLine
if ($WhatIf) {
    Write-Host "Would update prompt note: $promptPathFull" -ForegroundColor Cyan
    Write-Output $updated
    exit 0
}

$updated | Out-File -FilePath $promptPathFull -Encoding utf8
Write-Host "Prompt note updated: $promptPathFull" -ForegroundColor Green
