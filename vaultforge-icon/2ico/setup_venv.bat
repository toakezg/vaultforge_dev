@echo off
setlocal
cd /d "%~dp0"

py -m venv .venv
if errorlevel 1 exit /b %errorlevel%

".venv\Scripts\python.exe" -m pip install --upgrade pip
if errorlevel 1 exit /b %errorlevel%

".venv\Scripts\python.exe" -m pip install -r requirements.txt
exit /b %errorlevel%
