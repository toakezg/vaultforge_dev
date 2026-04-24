

## run_loop_forever.bat
### .py
```
:loop
python generate_art.py
goto loop
```
[[vaultforge-business/Loopers/run_loop_forever.bat]]
[[run_10_loops.bat]]
### .ps1
```
:loop
powershell -ExecutionPolicy Bypass -File .\run_business_md_bank.ps1 -Path ".\my-prompts-bank\vaultforge\cover-01.md"
goto loop
```
##### with delay
```
@echo off

:loop
echo Running business pipeline...

powershell -ExecutionPolicy Bypass -File "%~dp0run_business_md_bank.ps1" -Path "%~dp0my-prompts-bank\vaultforge\cover-01.md"

timeout /t 2 >nul
goto loop
```

## Controlled Loop
### .py
```
@echo off
set count=0

:loop
if %count%==10 goto end

python generate_art.py

set /a count+=1
goto loop

:end
echo Done.
```
`set count=0`
`:loop`
`if %count%==10 goto end`
`running.py`
`set /a count+=1`
`goto loop`
`:end`

### .ps1
```
@echo off
set count=0

:loop
if %count%==10 goto end

powershell -ExecutionPolicy Bypass -File .\run_business_md_bank.ps1 -Path ".\my-prompts-bank\vaultforge\cover-01.md"

set /a count+=1
goto loop

:end
echo Done.
pause
```
## Add Delay to Loop under running.py
```
:loop
python generate_art.py
timeout /t 5 >nul
goto loop
```
👉 Adds a **5 second pause**

- good for API usage
- avoids hammering requests
- feels more “engine-like”
## run_batch_50.bat



## run_until_stop.bat
