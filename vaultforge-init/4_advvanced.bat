@echo off
setlocal EnableDelayedExpansion

REM  This one is closer to what you're already doing with your pipelines 👀
REM   Special eye char might throw error. if this doesnt work remove eyes above then rerun


echo ================================
echo   PYTHON SCRIPT RUNNER
echo ================================
echo.

set "SCRIPT_DIR=%~dp0"
cd /d "%SCRIPT_DIR%"

REM Collect all passed arguments
set "ARGS="

:loop
if "%~1"=="" goto run
set "ARGS=!ARGS! %1"
shift
goto loop

:run
echo Running with args: %ARGS%
python your_script.py %ARGS%

echo.
echo Finished.
pause

REM Example Usage: run.bat --rerun --style pixel