@echo off
setlocal

set "BASE=E:\tools\vaultforge"
set "TEMPLATE=%BASE%\_template"

:: Try common Obsidian install locations
set "OBSIDIAN=%LocalAppData%\Programs\Obsidian\Obsidian.exe"
if not exist "%OBSIDIAN%" set "OBSIDIAN=%ProgramFiles%\Obsidian\Obsidian.exe"
if not exist "%OBSIDIAN%" set "OBSIDIAN=%ProgramFiles(x86)%\Obsidian\Obsidian.exe"

set /p "VAULTNAME=Enter new vault name: "

if "%VAULTNAME%"=="" (
    echo No vault name entered.
    pause
    exit /b
)

set "NEWVAULT=%BASE%\%VAULTNAME%"

if exist "%NEWVAULT%" (
    echo Folder already exists:
    echo %NEWVAULT%
    pause
    exit /b
)

mkdir "%NEWVAULT%"

xcopy "%TEMPLATE%\*" "%NEWVAULT%\" /E /I /Y /H

if not exist "%NEWVAULT%\Home.md" (
    >"%NEWVAULT%\Home.md" echo # %VAULTNAME%
)

:: Open folder in Explorer
start "" explorer "%NEWVAULT%"

:: Open vault in Obsidian
if exist "%OBSIDIAN%" (
    start "" "%OBSIDIAN%" -- "%NEWVAULT%"
) else (
    echo.
    echo Obsidian.exe not found automatically.
    echo Install path tried:
    echo %OBSIDIAN%
    echo.
    echo Open this folder manually in Obsidian:
    echo %NEWVAULT%
    pause
)

endlocal