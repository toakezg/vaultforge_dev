@echo off
setlocal
cd /d "%~dp0"

if not exist ".venv\Scripts\python.exe" (
  echo Missing local venv. Run setup_venv.bat first.
  exit /b 1
)

set /p INPUT_PATH=Input image file or folder: 
set /p OUTPUT_PATH=Output ICO file or folder: 
set /p ICO_SIZES=ICO sizes [16,24,32,48,64,128,256]: 

if "%ICO_SIZES%"=="" set ICO_SIZES=16,24,32,48,64,128,256

".venv\Scripts\python.exe" "%~dp0image_to_ico.py" --input "%INPUT_PATH%" --output "%OUTPUT_PATH%" --sizes "%ICO_SIZES%"
exit /b %errorlevel%
