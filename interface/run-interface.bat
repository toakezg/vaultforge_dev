@echo off
setlocal
cd /d "%~dp0"

if "%~1"=="" (
  set "VF_INTERFACE_PORT=4173"
) else (
  set "VF_INTERFACE_PORT=%~1"
)

if exist "%ProgramFiles%\nodejs\node.exe" (
  "%ProgramFiles%\nodejs\node.exe" scripts\launch-interface.mjs %VF_INTERFACE_PORT%
) else (
  node scripts\launch-interface.mjs %VF_INTERFACE_PORT%
)
