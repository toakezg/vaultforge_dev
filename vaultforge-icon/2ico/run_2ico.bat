@echo off
setlocal
cd /d "%~dp0"

if not exist ".venv\Scripts\python.exe" (
  echo Missing local venv. Run setup_venv.bat first.
  exit /b 1
)

".venv\Scripts\python.exe" "%~dp0image_to_ico.py" %*
exit /b %errorlevel%
