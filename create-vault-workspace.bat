@echo off
setlocal

set "BASE=E:\tools\vaultforge"
set "TEMPLATE=%BASE%\_template"
set "OBSIDIANCLI="

:: Try common Obsidian CLI redirector locations on Windows
if exist "%LocalAppData%\Programs\Obsidian\Obsidian.com" set "OBSIDIANCLI=%LocalAppData%\Programs\Obsidian\Obsidian.com"
if not defined OBSIDIANCLI if exist "%ProgramFiles%\Obsidian\Obsidian.com" set "OBSIDIANCLI=%ProgramFiles%\Obsidian\Obsidian.com"
if not defined OBSIDIANCLI if exist "%ProgramFiles(x86)%\Obsidian\Obsidian.com" set "OBSIDIANCLI=%ProgramFiles(x86)%\Obsidian\Obsidian.com"

set /p "VAULTNAME=Enter new vault name: "

if "%VAULTNAME%"=="" (
    echo No vault name entered.
    pause
    exit /b 1
)

set "NEWVAULT=%BASE%\%VAULTNAME%"

if exist "%NEWVAULT%" (
    echo Folder already exists:
    echo %NEWVAULT%
    pause
    exit /b 1
)

mkdir "%NEWVAULT%"
if errorlevel 1 (
    echo Failed to create:
    echo %NEWVAULT%
    pause
    exit /b 1
)

xcopy "%TEMPLATE%\*" "%NEWVAULT%\" /E /I /Y /H >nul
if errorlevel 2 (
    echo Failed to copy template from:
    echo %TEMPLATE%
    pause
    exit /b 1
)

if not exist "%NEWVAULT%\Home.md" (
    >"%NEWVAULT%\Home.md" echo # %VAULTNAME%
)

:: Open folder in Explorer
start "" explorer "%NEWVAULT%"
obsidian

cd /d "%NEWVAULT%" 
obsidian .

