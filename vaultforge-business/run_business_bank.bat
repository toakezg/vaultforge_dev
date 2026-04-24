@echo off
setlocal

echo Running the starter logo pack through VaultForge Business.
echo.
call "%~dp0run-client-pack.bat" "%~1" "%~2" "%~3" "%~4" "%~dp0logo-pack.txt" "%~5"
