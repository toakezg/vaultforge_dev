@echo off
setlocal

echo ================================
echo   PYTHON VENV LAUNCHER
echo ================================
echo.

set "SCRIPT_DIR=%~dp0"
cd /d "%SCRIPT_DIR%"

REM Activate virtual environment
call "%SCRIPT_DIR%.venv\Scripts\activate.bat"

REM Run script
python your_script.py

echo.
echo Done.
pause

REM 👉 Swap .venv if your env is elsewhere. 
REM Check if comments bellow pause cuase error