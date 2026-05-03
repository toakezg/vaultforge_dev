@echo off
setlocal

set "SCRIPT_DIR=%~dp0"
set "LOCAL_PY=%SCRIPT_DIR%.venv\Scripts\python.exe"

if exist "%LOCAL_PY%" (
    "%LOCAL_PY%" "%SCRIPT_DIR%svg_forge.py" %*
) else (
    py "%SCRIPT_DIR%svg_forge.py" %*
)

exit /b %ERRORLEVEL%
