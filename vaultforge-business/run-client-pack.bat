@echo off
setlocal

if "%~1"=="" (
    echo Usage:
    echo   %~nx0 "INPUT" "CLIENT" "PROJECT" "TAG" ["PROMPTFILE"] ["TWEAK"]
    echo.
    echo Example:
    echo   %~nx0 "Empower You Plan Management" "empower-you" "logo-pack-01" "round1" ".\logo-pack.txt"
    exit /b 1
)

if "%~2"=="" (
    echo Missing CLIENT
    exit /b 1
)

if "%~3"=="" (
    echo Missing PROJECT
    exit /b 1
)

if "%~4"=="" (
    echo Missing TAG
    exit /b 1
)

set "INPUTVALUE=%~1"
set "CLIENT=%~2"
set "PROJECT=%~3"
set "TAG=%~4"
set "PROMPTFILE=%~5"
set "TWEAK=%~6"

if "%PROMPTFILE%"=="" set "PROMPTFILE=.\logo-pack.txt"

powershell -ExecutionPolicy Bypass -File "%~dp0run-client-pack.ps1" ^
  -InputValue "%INPUTVALUE%" ^
  -Client "%CLIENT%" ^
  -Project "%PROJECT%" ^
  -Tag "%TAG%" ^
  -PromptFile "%PROMPTFILE%" ^
  -Tweak "%TWEAK%"
