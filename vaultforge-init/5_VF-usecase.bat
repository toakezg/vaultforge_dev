@echo off
setlocal EnableDelayedExpansion

REM since --rerun --style pixel... heres tailored version

echo ================================
echo   VAULTFORGE ART RUNNER
echo ================================
echo.

set "SCRIPT_DIR=%~dp0"
cd /d "%SCRIPT_DIR%"

set "PYTHON_EXE=%SCRIPT_DIR%.venv\Scripts\python.exe"
set "SCRIPT_FILE=%SCRIPT_DIR%generate_art.py"

REM Collect args
set "ARGS="

:collect
if "%~1"=="" goto execute
set "ARGS=!ARGS! %1"
shift
goto collect

:execute
echo Running:
echo %PYTHON_EXE% %SCRIPT_FILE% %ARGS%
echo.

"%PYTHON_EXE%" "%SCRIPT_FILE%" %ARGS%

echo.
echo Done.
pause