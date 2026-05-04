@echo off
setlocal
cd /d "%~dp0"

if not exist ".venv\Scripts\python.exe" (
  echo Missing local venv. Run setup_venv.bat first.
  exit /b 1
)

set /p INPUT_DIR=Input image file or folder: 
set /p OUTPUT_DIR=Output ICO file or folder: 

".venv\Scripts\python.exe" "%~dp0image_to_ico.py" --batch --input "%INPUT_DIR%" --output "%OUTPUT_DIR%"
exit /b %errorlevel%
