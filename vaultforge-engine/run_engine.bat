@echo off
setlocal

set "ROOT_DIR=%~dp0"
set "SCRIPT_PATH=%ROOT_DIR%src\generate.py"
set "ENV_FILE=%ROOT_DIR%.env"
set "VENV_PYTHON=%ROOT_DIR%.venv\Scripts\python.exe"
set "NEEDS_API_KEY=1"

if not exist "%SCRIPT_PATH%" (
    echo Engine script not found at "%SCRIPT_PATH%".
    exit /b 1
)

if exist "%ENV_FILE%" (
    for /f "usebackq eol=# tokens=1,* delims==" %%A in ("%ENV_FILE%") do (
        if not "%%A"=="" set "%%A=%%B"
    )
)

for %%A in (%*) do (
    if /I "%%~A"=="--dry-run" set "NEEDS_API_KEY=0"
)

if "%NEEDS_API_KEY%"=="1" if "%IMAGE_GENERATION_KEY_B_OPENAI_API_KEY%"=="" (
    echo IMAGE_GENERATION_KEY_B_OPENAI_API_KEY is not set.
    echo Paste your key into "%ENV_FILE%" like this:
    echo   IMAGE_GENERATION_KEY_B_OPENAI_API_KEY=sk-your-key
    echo You can also set it for your Windows user profile with setx if preferred.
    exit /b 1
)

if exist "%VENV_PYTHON%" (
    "%VENV_PYTHON%" "%SCRIPT_PATH%" %*
) else (
    where py >nul 2>nul
    if errorlevel 1 (
        echo No local engine virtual environment was found at "%VENV_PYTHON%".
        echo The Windows Python launcher 'py' was also not found.
        echo Keep using launcher-based execution for now, or create a local ".venv" first.
        exit /b 1
    )
    py "%SCRIPT_PATH%" %*
)
set "EXIT_CODE=%ERRORLEVEL%"
exit /b %EXIT_CODE%
