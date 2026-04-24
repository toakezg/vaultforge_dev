@echo off
setlocal

set "ROOT_DIR=%~dp0"
set "VENV_PYTHON=%ROOT_DIR%.venv\Scripts\python.exe"
set "REQUIREMENTS=%ROOT_DIR%requirements.txt"

if not exist "%VENV_PYTHON%" (
    echo Local virtual environment not found.
    echo Run setup_venv.bat first, or run setup_all.bat.
    exit /b 1
)

if exist "%REQUIREMENTS%" (
    echo Installing dependencies from requirements.txt...
    "%VENV_PYTHON%" -m pip install -r "%REQUIREMENTS%"
) else (
    echo requirements.txt was not found, installing this project in editable mode...
    "%VENV_PYTHON%" -m pip install -e "%ROOT_DIR%"
)

if errorlevel 1 (
    echo Dependency installation failed.
    exit /b 1
)

echo Requirements are installed.
exit /b 0
