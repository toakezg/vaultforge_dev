param(
    [Parameter(Mandatory=$true)][string]$InputValue,
    [Parameter(Mandatory=$true)][string]$Client,
    [Parameter(Mandatory=$true)][string]$Project,
    [Parameter(Mandatory=$true)][string]$Tag,
    [string]$PromptFile = ".\logo-pack.txt",
    [string]$Tweak = "",
    [switch]$StopOnError,
    [switch]$PauseBetween,
    [int]$DelaySeconds = 0,
    [switch]$WhatIf,
    [switch]$LogWhatIf
)

function Get-CommandElementText {
    param([System.Management.Automation.Language.Ast]$Element)

    if ($Element -is [System.Management.Automation.Language.CommandParameterAst]) {
        return $Element.Extent.Text
    }

    try {
        $value = $Element.SafeGetValue()
        if ($null -eq $value) { return "" }
        return [string]$value
    }
    catch {
        return $Element.Extent.Text
    }
}

function ConvertTo-ParsedCommand {
    param([string]$CommandLine)

    $tokens = $null
    $errors = $null
    $ast = [System.Management.Automation.Language.Parser]::ParseInput($CommandLine, [ref]$tokens, [ref]$errors)

    if ($errors.Count -gt 0) {
        $message = ($errors | ForEach-Object { $_.Message }) -join "; "
        throw "Could not parse command line: $message"
    }

    if ($ast.EndBlock.Statements.Count -ne 1) {
        throw "Expected exactly one command per line."
    }

    $statement = $ast.EndBlock.Statements[0]
    if (-not ($statement -is [System.Management.Automation.Language.PipelineAst])) {
        throw "Expected a command pipeline."
    }

    if ($statement.PipelineElements.Count -ne 1) {
        throw "Pipelines with multiple commands are not supported in pack files."
    }

    $commandAst = $statement.PipelineElements[0]
    if (-not ($commandAst -is [System.Management.Automation.Language.CommandAst])) {
        throw "Unsupported command shape in pack file."
    }

    if ($commandAst.CommandElements.Count -lt 1) {
        throw "Pack file command did not contain an executable."
    }

    $command = Get-CommandElementText $commandAst.CommandElements[0]
    $arguments = New-Object System.Collections.Generic.List[string]
    $argumentIsParameter = New-Object System.Collections.Generic.List[bool]
    for ($i = 1; $i -lt $commandAst.CommandElements.Count; $i++) {
        $element = $commandAst.CommandElements[$i]
        $arguments.Add((Get-CommandElementText $element))
        $argumentIsParameter.Add(($element -is [System.Management.Automation.Language.CommandParameterAst]))
    }

    [pscustomobject]@{
        Command = $command
        Arguments = $arguments.ToArray()
        ArgumentIsParameter = $argumentIsParameter.ToArray()
    }
}

function Expand-PackPlaceholders {
    param([AllowNull()][string]$Text)

    if ($null -eq $Text) { return "" }

    $expanded = $Text
    $expanded = $expanded.Replace("{INPUT}", $InputValue)
    $expanded = $expanded.Replace("{CLIENT}", $Client)
    $expanded = $expanded.Replace("{PROJECT}", $Project)
    $expanded = $expanded.Replace("{TAG}", $Tag)
    $expanded = $expanded.Replace("{TWEAK}", $Tweak)
    return $expanded
}

function Format-DisplayArgument {
    param([AllowNull()][string]$Value)

    if ($null -eq $Value) { return "''" }
    if ($Value.Length -eq 0 -or $Value -match "\s" -or $Value.Contains('"') -or $Value.Contains("'")) {
        return "'" + $Value.Replace("'", "''") + "'"
    }

    return $Value
}

function ConvertTo-DisplayCommand {
    param($ParsedCommand)

    $parts = New-Object System.Collections.Generic.List[string]
    $parts.Add((Format-DisplayArgument $ParsedCommand.Command))
    foreach ($argument in $ParsedCommand.Arguments) {
        $parts.Add((Format-DisplayArgument ([string]$argument)))
    }

    return ($parts.ToArray() -join " ")
}

function ConvertFrom-StructuredPack {
    param([string]$Path)

    try {
        $pack = Get-Content -Raw -LiteralPath $Path | ConvertFrom-Json
    }
    catch {
        throw "Could not parse structured pack JSON: $($_.Exception.Message)"
    }

    if ($null -eq $pack.commands) {
        throw "Structured pack must contain a top-level 'commands' array."
    }

    $entries = New-Object System.Collections.Generic.List[object]
    $index = 0

    foreach ($commandSpec in @($pack.commands)) {
        $index++

        if ($null -eq $commandSpec.command -or [string]::IsNullOrWhiteSpace([string]$commandSpec.command)) {
            throw "Structured pack command #$index is missing 'command'."
        }

        $rawArguments = $commandSpec.args
        if ($null -eq $rawArguments -and $null -ne $commandSpec.arguments) {
            $rawArguments = $commandSpec.arguments
        }

        $arguments = New-Object System.Collections.Generic.List[string]
        $argumentIsParameter = New-Object System.Collections.Generic.List[bool]
        if ($null -ne $rawArguments) {
            foreach ($argument in @($rawArguments)) {
                $rawArgument = [string]$argument
                $arguments.Add((Expand-PackPlaceholders $rawArgument))
                $argumentIsParameter.Add(($rawArgument -match "^-{1,2}[A-Za-z][A-Za-z0-9_-]*$"))
            }
        }

        $parsedCommand = [pscustomobject]@{
            Command = Expand-PackPlaceholders ([string]$commandSpec.command)
            Arguments = $arguments.ToArray()
            ArgumentIsParameter = $argumentIsParameter.ToArray()
        }

        $entries.Add([pscustomobject]@{
            CommandText = ConvertTo-DisplayCommand $parsedCommand
            ParsedCommand = $parsedCommand
        })
    }

    return $entries.ToArray()
}

function ConvertFrom-TextPack {
    param([string]$Path)

    $entries = New-Object System.Collections.Generic.List[object]
    $lines = Get-Content -LiteralPath $Path

    foreach ($line in $lines) {
        $cmd = $line.Trim()

        if ([string]::IsNullOrWhiteSpace($cmd)) { continue }
        if ($cmd.StartsWith("#")) { continue }

        $cmd = Expand-PackPlaceholders $cmd

        $entries.Add([pscustomobject]@{
            CommandText = $cmd
            ParsedCommand = $null
        })
    }

    return $entries.ToArray()
}

function Get-PackEntries {
    param([string]$Path)

    $extension = [System.IO.Path]::GetExtension($Path).ToLowerInvariant()
    if ($extension -eq ".json") {
        return ConvertFrom-StructuredPack $Path
    }

    return ConvertFrom-TextPack $Path
}

function Invoke-PowerShellScriptFile {
    param(
        [string]$ScriptPath,
        [string[]]$Arguments,
        [bool[]]$ArgumentIsParameter = @()
    )

    if ($ArgumentIsParameter.Count -ne $Arguments.Count) {
        $ArgumentIsParameter = @(for ($i = 0; $i -lt $Arguments.Count; $i++) { $false })
    }

    $invocationParts = New-Object System.Collections.Generic.List[string]
    $invocationParts.Add("& ([string]`$payload.Path)")
    for ($i = 0; $i -lt $Arguments.Count; $i++) {
        $argument = [string]$Arguments[$i]
        if ($ArgumentIsParameter[$i] -and $argument -match "^-{1,2}[A-Za-z][A-Za-z0-9_-]*$") {
            $invocationParts.Add($argument)
        }
        else {
            $invocationParts.Add(('$scriptArgs[{0}]' -f $i))
        }
    }
    $invocationLine = $invocationParts.ToArray() -join " "

    $payload = [ordered]@{
        Path = $ScriptPath
        Arguments = @($Arguments)
    }
    $payloadJson = $payload | ConvertTo-Json -Compress -Depth 4
    $payloadBase64 = [Convert]::ToBase64String([System.Text.Encoding]::UTF8.GetBytes($payloadJson))
    $launcher = @"
`$payloadJson = [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String('$payloadBase64'))
`$payload = `$payloadJson | ConvertFrom-Json
`$scriptArgs = @()
foreach (`$argument in @(`$payload.Arguments)) {
    `$scriptArgs += [string]`$argument
}
$invocationLine
if (`$null -ne `$LASTEXITCODE) { exit `$LASTEXITCODE }
if (-not `$?) { exit 1 }
exit 0
"@
    & powershell -NoProfile -OutputFormat Text -ExecutionPolicy Bypass -Command $launcher | Out-Host
}

function Invoke-ParsedCommand {
    param($ParsedCommand)

    $commandPath = $ParsedCommand.Command
    if ($commandPath.StartsWith(".\") -or $commandPath.StartsWith("..\")) {
        $commandPath = (Resolve-Path -LiteralPath $commandPath).Path
    }

    $extension = [System.IO.Path]::GetExtension($commandPath).ToLowerInvariant()

    switch ($extension) {
        ".ps1" {
            Invoke-PowerShellScriptFile -ScriptPath $commandPath -Arguments @($ParsedCommand.Arguments) -ArgumentIsParameter @($ParsedCommand.ArgumentIsParameter)
            break
        }
        ".bat" {
            & cmd /c $commandPath @($ParsedCommand.Arguments) | Out-Host
            break
        }
        ".cmd" {
            & cmd /c $commandPath @($ParsedCommand.Arguments) | Out-Host
            break
        }
        default {
            & $commandPath @($ParsedCommand.Arguments) | Out-Host
            break
        }
    }

    if ($null -eq $LASTEXITCODE) {
        return 0
    }
    return $LASTEXITCODE
}

function Add-RunLogRow {
    param(
        [string]$Path,
        [string]$Timestamp,
        [string]$LogClient,
        [string]$LogProject,
        [string]$LogTag,
        [string]$LogInput,
        [string]$LogPromptFile,
        [string]$LogCommand,
        [string]$LogStatus,
        [int]$LogExitCode
    )

    [pscustomobject]@{
        timestamp = $Timestamp
        client = $LogClient
        project = $LogProject
        tag = $LogTag
        input = $LogInput
        prompt_file = $LogPromptFile
        command = $LogCommand
        status = $LogStatus
        exit_code = $LogExitCode
    } | ConvertTo-Csv -NoTypeInformation | Select-Object -Skip 1 | Add-Content -Path $Path -Encoding utf8
}

function Initialize-RunLog {
    param([string]$Path)

    $directory = Split-Path -Parent $Path
    if (-not (Test-Path $directory)) {
        New-Item -ItemType Directory -Path $directory | Out-Null
    }

    if (-not (Test-Path $Path)) {
        'timestamp,client,project,tag,input,prompt_file,command,status,exit_code' | Out-File -FilePath $Path -Encoding utf8
    }
}

if (-not (Test-Path $PromptFile)) {
    Write-Host "Prompt file not found: $PromptFile" -ForegroundColor Red
    exit 1
}

$packEntries = @(Get-PackEntries $PromptFile)
$logFile = Join-Path ".\logs" "run-log.csv"
$shouldWriteRunLog = (-not $WhatIf) -or $LogWhatIf
if ($shouldWriteRunLog) {
    Initialize-RunLog $logFile
}
elseif ($WhatIf) {
    Write-Host "WhatIf preview only: run log will not be updated. Add -LogWhatIf to record preview rows." -ForegroundColor Yellow
}

foreach ($entry in $packEntries) {
    $cmd = $entry.CommandText
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"

    Write-Host ""
    Write-Host "Running: $cmd" -ForegroundColor Cyan

    if ($WhatIf) {
        if ($LogWhatIf) {
            Add-RunLogRow $logFile $timestamp $Client $Project $Tag $InputValue $PromptFile $cmd "whatif" 0
        }
        continue
    }

    try {
        if ($null -ne $entry.ParsedCommand) {
            $parsedCommand = $entry.ParsedCommand
        }
        else {
            $parsedCommand = ConvertTo-ParsedCommand $cmd
        }

        $exitCode = Invoke-ParsedCommand $parsedCommand
    }
    catch {
        $exitCode = 1
        Write-Host "Command parsing/invocation failed: $($_.Exception.Message)" -ForegroundColor Red
    }

    $status = if ($exitCode -eq 0) { "success" } else { "failed" }
    Add-RunLogRow $logFile $timestamp $Client $Project $Tag $InputValue $PromptFile $cmd $status $exitCode

    if ($exitCode -ne 0) {
        Write-Host "Command failed with exit code $exitCode" -ForegroundColor Red
        if ($StopOnError) { exit $exitCode }
    }

    if ($PauseBetween) {
        Write-Host "Press Enter to continue..."
        [void][System.Console]::ReadLine()
    }

    if ($DelaySeconds -gt 0) {
        Start-Sleep -Seconds $DelaySeconds
    }
}
