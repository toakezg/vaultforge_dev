@echo off
setlocal

set "ROOT_DIR=%~dp0"
set "VENV_DIR=%ROOT_DIR%.venv"

call "%VENV_DIR%\Scripts\activate.bat"

python main.py

pause