@echo off
setlocal

set "ROOT_DIR=%~dp0"
set "ENGINE_BAT=%ROOT_DIR%..\vaultforge-engine\run_engine.bat"
set "ENV_FILE=%ROOT_DIR%.env"

if not exist "%ENGINE_BAT%" (
    echo Engine launcher not found at "%ENGINE_BAT%".
    exit /b 1
)

if exist "%ENV_FILE%" (
    for /f "usebackq eol=# tokens=1,* delims==" %%A in ("%ENV_FILE%") do (
        if not "%%A"=="" set "%%A=%%B"
    )
)

set "VAULTFORGE_ENGINE_PROJECT_ROOT=%ROOT_DIR%"

call "%ENGINE_BAT%" --api-key-env ART_KEY --api-key-env VAULTFORGE_ART_OPENAI_API_KEY --output-dir output %*
set "EXIT_CODE=%ERRORLEVEL%"
exit /b %EXIT_CODE%
