@echo off
setlocal

set "ROOT_DIR=%~dp0"

call "%ROOT_DIR%setup_venv.bat"
if errorlevel 1 exit /b 1

call "%ROOT_DIR%install_requirements.bat"
if errorlevel 1 exit /b 1

call "%ROOT_DIR%open_venv_terminal.bat"
exit /b %ERRORLEVEL%
