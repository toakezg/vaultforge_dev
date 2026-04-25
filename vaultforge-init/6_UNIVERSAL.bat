@echo off
setlocal EnableDelayedExpansion

REM ____OVERALL STRUCTURE BRREAKDOWN_______
REM 1.  HEADER			.keep
REM 2.  SET ROOT 		.keep
REM 3.  FIRST ARG choses lane 	.keep
REM 4.  HELP ARG + GOTO HELP	.keep
REM 5.  COLLECT ARGS		.keep
REM 6.  ROUTING 		.editable
REM 7.  "%LANE%"=="A" goto A    .editable
REM 8.  "%LANE%"=="B" goto B	.editable 
REM 9.  :A 
REM 10. LANE PYTHON.EXE PATH    .editable
REM 11. LANE PY.FILE PATH	.editable
REM 12. GOTO RUN_PYTHON
REM 13. :B 
REM 14. LANE ""   exe     ""	.editable
REM 15. LANE ""   file    ""	.editable
REM 16. GOTO "" RUNPYTHON ""  
REM 17. RUN_PYTHON
REM 18. %PYTHON.EXE% %PYTHON.FILE% %ARGS%
REM 19. PAUSE
REM 20. :HELP
REM 21. EXIT
REM _______________________________________

REM ========================================
REM   UNIVERSAL PROJECT LAUNCHER
REM ========================================

REM Root = folder this .bat lives in
set "ROOT=%~dp0"
if "%ROOT:~-1%"=="\" set "ROOT=%ROOT:~0,-1%"

REM First argument chooses the lane
set "LANE=%~1"

if "%LANE%"=="" goto help
if /I "%LANE%"=="help" goto help
if /I "%LANE%"=="--help" goto help
if /I "%LANE%"=="-h" goto help

REM Remove lane from argument list
shift

REM Collect remaining args
set "ARGS="
:collect_args
if "%~1"=="" goto args_ready
set "ARGS=!ARGS! %~1"
shift
goto collect_args

:args_ready

REM ========================================
REM   ROUTES     : These are what you edit
REM ========================================

REM EDIT Here
if /I "%LANE%"=="art" goto art
if /I "%LANE%"=="xp4l" goto xp4l
if /I "%LANE%"=="coding" goto coding
if /I "%LANE%"=="test" goto test

echo Unknown lane: %LANE%
echo.
goto help


:art
REM Example:
REM run.bat art --rerun --style pixel

REM Edit Between %ROOT$\edit-here\.venv\Scripts..
set "PYTHON_EXE=%ROOT%\vaultforge-art\.venv\Scripts\python.exe"
REM Edit after %ROOT%\path-to-script-from-root.file
set "PY_FILE=%ROOT%\vaultforge-art\generate_art.py"

goto run_python


:xp4l
REM Example:
REM run.bat xp4l --dry-run

set "PYTHON_EXE=%ROOT%\vaultforge-xp4l\.venv\Scripts\python.exe"
set "PY_FILE=%ROOT%\vaultforge-xp4l\main.py"

goto run_python


:coding
REM Example:
REM run.bat coding --debug

set "PYTHON_EXE=%ROOT%\vaultforge-coding\.venv\Scripts\python.exe"
set "PY_FILE=%ROOT%\vaultforge-coding\main.py"

goto run_python


:test
REM Simple test lane

echo ROOT: %ROOT%
echo LANE: %LANE%
echo ARGS: %ARGS%
echo.
pause
exit /b 0


:run_python
echo ========================================
echo Running lane: %LANE%
echo Python: %PYTHON_EXE%
echo Script: %PY_FILE%
echo Args:   %ARGS%
echo ========================================
echo.

if not exist "%PYTHON_EXE%" (
    echo ERROR: Python venv not found:
    echo %PYTHON_EXE%
    echo.
    pause
    exit /b 1
)

if not exist "%PY_FILE%" (
    echo ERROR: Python file not found:
    echo %PY_FILE%
    echo.
    pause
    exit /b 1
)

"%PYTHON_EXE%" "%PY_FILE%" %ARGS%

echo.
echo Finished lane: %LANE%
pause
exit /b %ERRORLEVEL%


:help
echo Usage:
echo.
echo   run.bat art [args]
echo   run.bat xp4l [args]
echo   run.bat coding [args]
echo   run.bat test
echo.
echo Examples:
echo.
echo   run.bat art --rerun --style pixel
echo   run.bat xp4l --dry-run
echo   run.bat coding --debug
echo.
pause
exit /b 0