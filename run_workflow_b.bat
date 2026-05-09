@echo off
setlocal

set "ROOT=%~dp0"
if "%ROOT:~-1%"=="\" set "ROOT=%ROOT:~0,-1%"

set "PYTHON_EXE=%ROOT%\.venv\Scripts\python.exe"
if not exist "%PYTHON_EXE%" set "PYTHON_EXE=python"
if not "%PYTHON_EXE%"=="python" (
    "%PYTHON_EXE%" --version >nul 2>nul
    if errorlevel 1 set "PYTHON_EXE=python"
)

set "PY_FILE=%ROOT%\workflow_b_controller.py"

if not exist "%PY_FILE%" (
    echo ERROR: Workflow B controller not found:
    echo %PY_FILE%
    exit /b 1
)

echo ========================================
echo VaultForge Workflow B controller
echo Root:   %ROOT%
echo Python: %PYTHON_EXE%
echo Args:   %*
echo ========================================
echo.

"%PYTHON_EXE%" "%PY_FILE%" --root "%ROOT%" %*
exit /b %ERRORLEVEL%
