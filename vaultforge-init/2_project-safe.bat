@echo off
setlocal

REM This is 🔥 for VaultForge-style setups because:
REM Works even if launched from another directory
REM Keeps things portable

echo ================================
echo   PYTHON SCRIPT LAUNCHER
echo ================================
echo.

REM Get current script directory
echo Getting current script directory...
set "SCRIPT_DIR=%~dp0"

REM Optional: move into that directory
echo Moving to script directory...
cd /d "%SCRIPT_DIR%"

REM Run python file
echo Starting script run...
python "%SCRIPT_DIR%your_script.py"

echo.
echo Script finished.
pause

