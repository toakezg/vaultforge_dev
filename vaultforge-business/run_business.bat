@echo off
setlocal

if "%~1"=="" (
    echo Usage:
    echo   %~nx0 "PROMPT" [CLIENT] [ASSET_TYPE] [JOB] [TAG]
    echo.
    echo Example:
    echo   %~nx0 "Premium logo for Empower You Plan Management" "empower-you" "logo" "pack-01" "ndis,premium,local"
    exit /b 1
)

set "PROMPT=%~1"
set "CLIENT=%~2"
set "ASSETTYPE=%~3"
set "JOB=%~4"
set "TAG=%~5"

if "%CLIENT%"=="" set "CLIENT=unsorted"
if "%ASSETTYPE%"=="" set "ASSETTYPE=brand"
if "%JOB%"=="" set "JOB=manual"

powershell -ExecutionPolicy Bypass -File "%~dp0run_business.ps1" ^
  "%PROMPT%" ^
  -Client "%CLIENT%" ^
  -AssetType "%ASSETTYPE%" ^
  -Job "%JOB%" ^
  -Tag "%TAG%"
