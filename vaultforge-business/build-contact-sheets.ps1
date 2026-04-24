param(
    [string]$GeneratedRoot = (Join-Path $PSScriptRoot "generated"),
    [string]$OutName = "contact-sheet.jpg",
    [int]$Columns = 0,
    [int]$ThumbnailSize = 220,
    [int]$Padding = 18,
    [int]$LabelHeight = 34,
    [int]$Limit = 0,
    [switch]$Force
)

$ErrorActionPreference = "Stop"
$imageExtensions = @(".png", ".jpg", ".jpeg", ".webp")

Add-Type -AssemblyName System.Drawing

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

function Get-FitRectangle {
    param(
        [System.Drawing.Image]$Image,
        [int]$X,
        [int]$Y,
        [int]$Size
    )

    $scale = [Math]::Min($Size / $Image.Width, $Size / $Image.Height)
    $width = [Math]::Max(1, [int]($Image.Width * $scale))
    $height = [Math]::Max(1, [int]($Image.Height * $scale))
    $drawX = $X + [int](($Size - $width) / 2)
    $drawY = $Y + [int](($Size - $height) / 2)

    return [System.Drawing.Rectangle]::new($drawX, $drawY, $width, $height)
}

function New-ContactSheet {
    param(
        [System.IO.FileInfo[]]$Images,
        [string]$OutFile,
        [string]$Title,
        [int]$RequestedColumns
    )

    $imageCount = $Images.Count
    if ($imageCount -lt 1) { return $false }

    $columnsToUse = $RequestedColumns
    if ($columnsToUse -lt 1) {
        $columnsToUse = [Math]::Min(4, [Math]::Ceiling([Math]::Sqrt($imageCount)))
    }
    $columnsToUse = [Math]::Max(1, $columnsToUse)
    $rows = [Math]::Ceiling($imageCount / $columnsToUse)

    $titleHeight = 46
    $cellWidth = $ThumbnailSize + $Padding
    $cellHeight = $ThumbnailSize + $LabelHeight + $Padding
    $sheetWidth = ($Padding * 2) + ($columnsToUse * $cellWidth)
    $sheetHeight = ($Padding * 2) + $titleHeight + ($rows * $cellHeight)

    $bitmap = [System.Drawing.Bitmap]::new($sheetWidth, $sheetHeight)
    $graphics = [System.Drawing.Graphics]::FromImage($bitmap)
    $font = [System.Drawing.Font]::new("Segoe UI", 10)
    $titleFont = [System.Drawing.Font]::new("Segoe UI", 13, [System.Drawing.FontStyle]::Bold)
    $brush = [System.Drawing.SolidBrush]::new([System.Drawing.Color]::FromArgb(35, 35, 35))
    $mutedBrush = [System.Drawing.SolidBrush]::new([System.Drawing.Color]::FromArgb(90, 90, 90))
    $borderPen = [System.Drawing.Pen]::new([System.Drawing.Color]::FromArgb(210, 210, 210), 1)
    $backgroundBrush = [System.Drawing.SolidBrush]::new([System.Drawing.Color]::White)
    $tileBrush = [System.Drawing.SolidBrush]::new([System.Drawing.Color]::FromArgb(248, 248, 248))

    try {
        $graphics.Clear([System.Drawing.Color]::White)
        $graphics.TextRenderingHint = [System.Drawing.Text.TextRenderingHint]::ClearTypeGridFit
        $graphics.DrawString($Title, $titleFont, $brush, $Padding, $Padding)
        $graphics.DrawString("$imageCount image(s)", $font, $mutedBrush, $Padding, $Padding + 24)

        for ($index = 0; $index -lt $imageCount; $index++) {
            $imageFile = $Images[$index]
            $row = [Math]::Floor($index / $columnsToUse)
            $column = $index % $columnsToUse
            $cellX = $Padding + ($column * $cellWidth)
            $cellY = $Padding + $titleHeight + ($row * $cellHeight)

            $tileRect = [System.Drawing.Rectangle]::new($cellX, $cellY, $ThumbnailSize, $ThumbnailSize)
            $graphics.FillRectangle($tileBrush, $tileRect)
            $graphics.DrawRectangle($borderPen, $tileRect)

            $image = $null
            try {
                $image = [System.Drawing.Image]::FromFile($imageFile.FullName)
                $drawRect = Get-FitRectangle $image $cellX $cellY $ThumbnailSize
                $graphics.DrawImage($image, $drawRect)
            }
            finally {
                if ($null -ne $image) { $image.Dispose() }
            }

            $label = $imageFile.Name
            if ($label.Length -gt 34) {
                $label = $label.Substring(0, 31) + "..."
            }
            $graphics.DrawString($label, $font, $brush, $cellX, $cellY + $ThumbnailSize + 5)
        }

        $bitmap.Save($OutFile, [System.Drawing.Imaging.ImageFormat]::Jpeg)
    }
    finally {
        $graphics.Dispose()
        $font.Dispose()
        $titleFont.Dispose()
        $brush.Dispose()
        $mutedBrush.Dispose()
        $borderPen.Dispose()
        $backgroundBrush.Dispose()
        $tileBrush.Dispose()
        $bitmap.Dispose()
    }

    return $true
}

try {
    $rootPath = (Resolve-Path -LiteralPath $GeneratedRoot -ErrorAction Stop).Path
}
catch {
    Write-Host "Generated root not found: $GeneratedRoot" -ForegroundColor Red
    exit 1
}

$manifestFiles = @(Get-ChildItem -LiteralPath $rootPath -Recurse -Filter "gallery-entry.json" -File | Sort-Object FullName)
if ($Limit -gt 0) {
    $manifestFiles = @($manifestFiles | Select-Object -First $Limit)
}

$built = 0
$skipped = 0
$failed = 0

foreach ($manifestFile in $manifestFiles) {
    try {
        $entry = Get-Content -Raw -LiteralPath $manifestFile.FullName | ConvertFrom-Json
        $runDir = Get-FirstValue $entry @("run_dir") $manifestFile.DirectoryName
        if (-not (Test-Path -LiteralPath $runDir)) {
            $runDir = $manifestFile.DirectoryName
        }

        $images = @(Get-ChildItem -LiteralPath $runDir -File | Where-Object {
            ($imageExtensions -contains $_.Extension.ToLowerInvariant()) -and $_.Name -ne $OutName
        } | Sort-Object Name)

        if ($images.Count -eq 0) {
            $skipped++
            continue
        }

        $outFile = Join-Path $runDir $OutName
        if ((Test-Path -LiteralPath $outFile) -and -not $Force) {
            $newestImage = @($images | Sort-Object LastWriteTime -Descending | Select-Object -First 1)[0]
            $sheet = Get-Item -LiteralPath $outFile
            if ($sheet.LastWriteTime -ge $newestImage.LastWriteTime) {
                $skipped++
                continue
            }
        }

        $titleParts = @(
            (Get-FirstValue $entry @("client", "client_slug") "unsorted"),
            (Get-FirstValue $entry @("asset_type", "asset_slug") "brand"),
            (Get-FirstValue $entry @("preset", "business_preset", "preset_slug") "preset"),
            (Get-FirstValue $entry @("job", "job_slug") "manual")
        )
        $title = ($titleParts -join " / ")
        if (New-ContactSheet -Images $images -OutFile $outFile -Title $title -RequestedColumns $Columns) {
            Write-Host "Contact sheet written: $outFile" -ForegroundColor Green
            $built++
        }
    }
    catch {
        $failed++
        Write-Host "Contact sheet failed for $($manifestFile.FullName): $($_.Exception.Message)" -ForegroundColor Red
    }
}

Write-Host "Contact sheets complete. Built: $built Skipped: $skipped Failed: $failed"
if ($failed -gt 0) {
    exit 1
}
