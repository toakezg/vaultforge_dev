@echo off
setlocal

set "ROOT_DIR=%~dp0"
set "ACTIVATE=%ROOT_DIR%.venv\Scripts\activate.bat"
set "ENV_FILE=%ROOT_DIR%.env"

if not exist "%ACTIVATE%" (
    echo Local virtual environment not found.
    echo Run setup_venv.bat first, or run setup_all.bat.
    exit /b 1
)

if exist "%ENV_FILE%" (
    for /f "usebackq eol=# tokens=1,* delims==" %%A in ("%ENV_FILE%") do (
        if not "%%A"=="" set "%%A=%%B"
    )
)

start "VaultForge Art venv" /D "%ROOT_DIR%" cmd /k call "%ACTIVATE%"
exit /b 0
