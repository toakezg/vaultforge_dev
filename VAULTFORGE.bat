 @echo off
setlocal EnableExtensions EnableDelayedExpansion

REM ========================================
REM   VAULTFORGE GLOBAL LAUNCHER
REM ========================================
REM This file is path-safe: it resolves the VaultForge root from its own
REM location, so VAULTFORGE.bat can be called from any working directory.

set "VAULTFORGE_ROOT=%~dp0"
if "%VAULTFORGE_ROOT:~-1%"=="\" set "VAULTFORGE_ROOT=%VAULTFORGE_ROOT:~0,-1%"
set "ROOT=%VAULTFORGE_ROOT%"
set "VAULTFORGE_COMMAND=%~f0"

set "LANE=%~1"

if "%LANE%"=="" goto help
if /I "%LANE%"=="help" goto help
if /I "%LANE%"=="--help" goto help
if /I "%LANE%"=="-h" goto help
if /I "%LANE%"=="install" goto install_global
if /I "%LANE%"=="install-global" goto install_global
if /I "%LANE%"=="global" goto install_global
if /I "%LANE%"=="where" goto show_where
if /I "%LANE%"=="root" goto show_where

shift /1

set "FORWARD_ARGS="
:collect_args
if "%~1"=="" goto args_ready
set "NEXT_ARG=%~1"
set "FORWARD_ARGS=!FORWARD_ARGS! "!NEXT_ARG!""
shift /1
goto collect_args

:args_ready

REM ========================================
REM   ROUTES
REM ========================================

if /I "%LANE%"=="workflow-b" goto workflow_b
if /I "%LANE%"=="workflow" goto workflow_b
if /I "%LANE%"=="wb" goto workflow_b
if /I "%LANE%"=="workflow-b-watch" goto workflow_b_watch
if /I "%LANE%"=="wb-watch" goto workflow_b_watch
if /I "%LANE%"=="watch" goto workflow_b_watch

if /I "%LANE%"=="business" goto business
if /I "%LANE%"=="biz" goto business
if /I "%LANE%"=="business-bank" goto business_bank
if /I "%LANE%"=="bank" goto business_bank
if /I "%LANE%"=="business-md" goto business_md
if /I "%LANE%"=="mdbank" goto business_md
if /I "%LANE%"=="business-pack" goto business_pack
if /I "%LANE%"=="pack" goto business_pack

if /I "%LANE%"=="engine" goto engine
if /I "%LANE%"=="eng" goto engine
if /I "%LANE%"=="xp4l" goto xp4l
if /I "%LANE%"=="coding" goto coding
if /I "%LANE%"=="code" goto coding

if /I "%LANE%"=="image-gen" goto image_gen
if /I "%LANE%"=="icons" goto icons_part_a
if /I "%LANE%"=="icon-part-a" goto icons_part_a
if /I "%LANE%"=="svg" goto svg_forge
if /I "%LANE%"=="svg-forge" goto svg_forge
if /I "%LANE%"=="loop-rewards" goto loop_rewards

if /I "%LANE%"=="test" goto test

echo Unknown VaultForge lane: %LANE%
echo.
goto help


:workflow_b
set "BAT_FILE=%ROOT%\run_workflow_b.bat"
set "WORKDIR=%ROOT%"
goto run_batch


:workflow_b_watch
set "BAT_FILE=%ROOT%\run_workflow_b_watch.bat"
set "WORKDIR=%ROOT%"
goto run_batch


:business
set "BAT_FILE=%ROOT%\vaultforge-business\run_business.bat"
set "WORKDIR=%ROOT%\vaultforge-business"
goto run_batch


:business_bank
set "BAT_FILE=%ROOT%\vaultforge-business\run_business_bank.bat"
set "WORKDIR=%ROOT%\vaultforge-business"
goto run_batch


:business_md
set "BAT_FILE=%ROOT%\vaultforge-business\run_business_md_bank.bat"
set "WORKDIR=%ROOT%\vaultforge-business"
goto run_batch


:business_pack
set "BAT_FILE=%ROOT%\vaultforge-business\run-client-pack.bat"
set "WORKDIR=%ROOT%\vaultforge-business"
goto run_batch


:engine
set "BAT_FILE=%ROOT%\vaultforge-engine\run_engine.bat"
set "WORKDIR=%ROOT%\vaultforge-engine"
goto run_batch


:xp4l
set "WORKDIR=%ROOT%\vaultforge-xp4l"
set "PY_MODULE=vaultforge_xp4l"
goto run_python_module


:coding
set "WORKDIR=%ROOT%\vaultforge-coding"
set "PY_MODULE=vf_code_bridge"
goto run_python_module


:image_gen
set "WATCH_BAT=%ROOT%\vaultforge-image\scripts\watch-vf-image-output.bat"
set "BAT_FILE=%ROOT%\vaultforge-image\run_image.bat"
set "OUTPUT_DIR=%ROOT%\vaultforge-image\output"
goto run_image_gen

set "WORKDIR=%VAULTFORGE_ART_ROOT%"
set "PY_FILE=%VAULTFORGE_ART_ROOT%\generate_art.py"
goto run_python_file


:icons_part_a
set "BAT_FILE=%ROOT%\run-icons-part-a.bat"
set "WORKDIR=%ROOT%"
goto run_batch


:svg_forge
set "BAT_FILE=%ROOT%\vaultforge-icon\svg-forge\run_svg_forge.bat"
set "WORKDIR=%ROOT%\vaultforge-icon\svg-forge"
goto run_batch


:loop_rewards
set "BAT_FILE=%ROOT%\run_loop_rewards.bat"
set "WORKDIR=%ROOT%"
goto run_batch


:test
echo VAULTFORGE_ROOT: %ROOT%
echo VAULTFORGE_COMMAND: %VAULTFORGE_COMMAND%
echo LANE: %LANE%
echo ARGS:%FORWARD_ARGS%
exit /b 0


:show_where
echo VAULTFORGE_ROOT=%ROOT%
echo VAULTFORGE_COMMAND=%VAULTFORGE_COMMAND%
echo.
echo Call examples:
echo   VAULTFORGE workflow-b --help
echo   VAULTFORGE business "Prompt text" client brand job tag
echo   VAULTFORGE xp4l --help
exit /b 0


:install_global
echo Installing user-level VaultForge command access...
echo Root: %ROOT%
echo.

powershell -NoProfile -ExecutionPolicy Bypass -Command "$root=$env:VAULTFORGE_ROOT; [Environment]::SetEnvironmentVariable('VAULTFORGE_ROOT',$root,'User'); $scope='User'; $path=[Environment]::GetEnvironmentVariable('Path',$scope); $items=@(); if($path){$items=$path -split ';' | Where-Object { $_ }}; $norm=$items | ForEach-Object { $_.TrimEnd('\') }; if($norm -notcontains $root.TrimEnd('\')){[Environment]::SetEnvironmentVariable('Path',(($items+$root)-join ';'),$scope); Write-Output ('Added to user PATH: '+$root)} else {Write-Output ('Already on user PATH: '+$root)}"
if errorlevel 1 (
    echo.
    echo ERROR: Could not update the user environment.
    exit /b 1
)

echo.
echo Installed:
echo   VAULTFORGE_ROOT=%ROOT%
echo   PATH includes %ROOT%
echo.
echo Open a new terminal, then run:
echo   VAULTFORGE where
exit /b 0

:run_image_gen
if not exist "%BAT_FILE%" (
    echo ERROR: Batch route not found:
    echo %BAT_FILE%
    exit /b 1
)

if exist "%WATCH_BAT%" (
    start "VaultForge Image Watcher" cmd /k ""%WATCH_BAT%""
) else (
    echo WARNING: Watch BAT not found:
    echo %WATCH_BAT%
)

call "%BAT_FILE%" %FORWARD_ARGS%
set "RUN_EXIT=%ERRORLEVEL%"

set /p "ASK=Open output dir? [y/N]: "
if /I "%ASK%"=="y" (
    echo Opening output dir...
    explorer "%OUTPUT_DIR%"
)

exit /b %RUN_EXIT%

:run_batch
if not exist "%BAT_FILE%" (
    echo ERROR: Batch route not found:
    echo %BAT_FILE%
    exit /b 1
)
if defined WORKDIR (
    if not exist "%WORKDIR%" (
        echo ERROR: Working directory not found:
        echo %WORKDIR%
        exit /b 1
    )
    pushd "%WORKDIR%"
)
call "%BAT_FILE%" %FORWARD_ARGS%
set "RUN_EXIT=%ERRORLEVEL%"
if defined WORKDIR popd
exit /b %RUN_EXIT%


:run_python_module
if not exist "%WORKDIR%" (
    echo ERROR: Working directory not found:
    echo %WORKDIR%
    exit /b 1
)
set "PYTHON_EXE=%WORKDIR%\.venv\Scripts\python.exe"
if not exist "%PYTHON_EXE%" set "PYTHON_EXE=python"
if /I "%PYTHON_EXE%"=="python" (
    where python >nul 2>nul
    if errorlevel 1 (
        echo ERROR: Python was not found on PATH.
        exit /b 1
    )
)
if defined PYTHONPATH (
    set "PYTHONPATH=%WORKDIR%\src;%PYTHONPATH%"
) else (
    set "PYTHONPATH=%WORKDIR%\src"
)
pushd "%WORKDIR%"
"%PYTHON_EXE%" -m "%PY_MODULE%" %FORWARD_ARGS%
set "RUN_EXIT=%ERRORLEVEL%"
popd
exit /b %RUN_EXIT%


:run_python_file
if not exist "%WORKDIR%" (
    echo ERROR: Working directory not found:
    echo %WORKDIR%
    exit /b 1
)
if not exist "%PY_FILE%" (
    echo ERROR: Python script not found:
    echo %PY_FILE%
    exit /b 1
)
set "PYTHON_EXE=%WORKDIR%\.venv\Scripts\python.exe"
if not exist "%PYTHON_EXE%" set "PYTHON_EXE=python"
if /I "%PYTHON_EXE%"=="python" (
    where python >nul 2>nul
    if errorlevel 1 (
        echo ERROR: Python was not found on PATH.
        exit /b 1
    )
)
pushd "%WORKDIR%"
"%PYTHON_EXE%" "%PY_FILE%" %FORWARD_ARGS%
set "RUN_EXIT=%ERRORLEVEL%"
popd
exit /b %RUN_EXIT%


:help
echo Usage:
echo.
echo   VAULTFORGE ^<lane^> [args]
echo.
echo Global setup:
echo.
echo   VAULTFORGE install-global
echo   VAULTFORGE where
echo.
echo Core lanes:
echo.
echo   VAULTFORGE workflow-b [args]
echo   VAULTFORGE workflow-b-watch [args]
echo   VAULTFORGE engine [args]
echo   VAULTFORGE business "PROMPT" [CLIENT] [ASSET_TYPE] [JOB] [TAG]
echo   VAULTFORGE business-bank [args]
echo   VAULTFORGE business-md [args]
echo   VAULTFORGE business-pack [args]
echo   VAULTFORGE xp4l [args]
echo   VAULTFORGE coding [args]
echo.
echo Art and icon lanes:
echo.
echo   VAULTFORGE image-gen "PROMPT" [args]
echo   VAULTFORGE icons [all^|quests^|achievements^|titles^|rewards] [args]
echo   VAULTFORGE svg [args]
echo   VAULTFORGE loop-rewards [args]
echo.
echo Diagnostics:
echo.
echo   VAULTFORGE test [args]
echo.
exit /b 0
