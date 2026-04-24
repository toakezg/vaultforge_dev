@echo off

:loop
echo Running business pipeline...

powershell -ExecutionPolicy Bypass -File "%~dp0run_business_md_bank.ps1" -Path "%~dp0my-prompts-bank\vaultforge\cover-01.md"

timeout /t 2 >nul
goto loop