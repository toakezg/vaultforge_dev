@echo off
set count=0

:loop
if %count%==10 goto end

powershell -ExecutionPolicy Bypass -File .\run_business_md_bank.ps1 -Path ".\my-prompts-bank\Gallable\gallable-app-icon.md"

set /a count+=1
goto loop

:end
echo Done.
pause