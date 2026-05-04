param(
    [string]$Batch = "generated\proposals\first-inspired-run\prompts",
    [string]$Output = "generated\proposals\first-inspired-run\images",
    [string]$Client = "VaultForge Icon",
    [string]$Job = "first-inspired-run",
    [string]$Tag = "proposal,inspired-agent",
    [string]$Quality = "low",
    [switch]$DryRun
)

$ErrorActionPreference = "Stop"

$IconRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$RepoRoot = Split-Path -Parent $IconRoot
$EnvPath = Join-Path $IconRoot ".env"
$EngineScript = Join-Path $RepoRoot "vaultforge-engine\src\generate.py"

if (-not (Test-Path -LiteralPath $EnvPath)) {
    throw "Missing icon-lane .env: $EnvPath"
}

$iconKey = $null
foreach ($line in Get-Content -LiteralPath $EnvPath) {
    $trimmed = $line.Trim()
    if (-not $trimmed -or $trimmed.StartsWith("#") -or -not $trimmed.Contains("=")) {
        continue
    }

    $name, $value = $trimmed -split "=", 2
    if ($name.Trim() -eq "ICON_KEY") {
        $iconKey = $value.Trim().Trim('"').Trim("'")
        break
    }
}

if ([string]::IsNullOrWhiteSpace($iconKey)) {
    throw "ICON_KEY is missing from icon-lane .env"
}

$BatchPath = Resolve-Path -LiteralPath (Join-Path $IconRoot $Batch)
$OutputPath = Join-Path $IconRoot $Output
New-Item -ItemType Directory -Force -Path $OutputPath | Out-Null
$OutputPath = (Resolve-Path -LiteralPath $OutputPath).Path

$env:IMAGE_GENERATION_KEY_B_OPENAI_API_KEY = $iconKey

$args = @(
    $EngineScript,
    "--batch", $BatchPath.Path,
    "--preset", "icon",
    "--style", "geometric",
    "--size", "1024x1024",
    "--quality", $Quality,
    "--format", "png",
    "--background", "transparent",
    "--output-dir", $OutputPath,
    "--client", $Client,
    "--job", $Job,
    "--tag", $Tag
)

if ($DryRun) {
    $args += "--dry-run"
}

py @args
exit $LASTEXITCODE
