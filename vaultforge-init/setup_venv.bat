@echo off
setlocal

set "ROOT_DIR=%~dp0"
set "VENV_DIR=%ROOT_DIR%.venv"
set "VENV_PYTHON=%VENV_DIR%\Scripts\python.exe"
set "PYTHON_LAUNCHER=py"

where %PYTHON_LAUNCHER% >nul 2>nul
if errorlevel 1 (
    echo Python launcher 'py' was not found.
    echo Install Python for Windows and make sure the launcher is available, then run this script again.
    exit /b 1
)

if not exist "%VENV_PYTHON%" (
    echo Creating local virtual environment in "%VENV_DIR%"...
    %PYTHON_LAUNCHER% -m venv "%VENV_DIR%"
    if errorlevel 1 (
        echo Failed to create the virtual environment.
        exit /b 1
    )
) else (
    echo Reusing existing virtual environment in "%VENV_DIR%".
)

echo Upgrading pip...
"%VENV_PYTHON%" -m pip install --upgrade pip
if errorlevel 1 (
    echo Failed to upgrade pip.
    exit /b 1
)

if exist "%ROOT_DIR%requirements.txt" (
    echo Installing dependencies from requirements.txt...
    "%VENV_PYTHON%" -m pip install -r "%ROOT_DIR%requirements.txt"
    if errorlevel 1 (
        echo Failed to install dependencies from requirements.txt.
        exit /b 1
    )
) else (
    echo requirements.txt was not found, installing from pyproject.toml...
    "%VENV_PYTHON%" -m pip install -e "%ROOT_DIR%"
    if errorlevel 1 (
        echo Failed to install dependencies from pyproject.toml.
        exit /b 1
    )
)

echo Environment setup complete.
exit /b 0
