@echo off
setlocal EnableDelayedExpansion

set "VAULT_ROOT=%~dp0"
if "%VAULT_ROOT:~-1%"=="\" set "VAULT_ROOT=%VAULT_ROOT:~0,-1%"

set "TARGET=%~1"

if "%TARGET%"=="" (
    set "TARGET=all"
) else if "%TARGET:~0,1%"=="-" (
    set "TARGET=all"
) else (
    shift
)

if /I "%TARGET%"=="help" goto :usage
if /I "%TARGET%"=="--help" goto :usage

set "FORWARD_ARGS="

:collect_args
if "%~1"=="" goto :args_ready
set "FORWARD_ARGS=!FORWARD_ARGS! %1"
shift
goto :collect_args

:args_ready
set "ART_ROOT=E:\tools\image_generation\vaultforge-art"
set "ART_PYTHON=%ART_ROOT%\.venv\Scripts\python.exe"
set "ART_SCRIPT=%ART_ROOT%\generate_art.py"

if not exist "%ART_PYTHON%" (
    echo Required Python executable not found:
    echo %ART_PYTHON%
    echo.
    echo Set up the sibling art project first.
    exit /b 1
)

if not exist "%ART_SCRIPT%" (
    echo Required generator script not found:
    echo %ART_SCRIPT%
    exit /b 1
)

if /I "%TARGET%"=="all" goto :run_all
if /I "%TARGET%"=="quests" goto :run_quests
if /I "%TARGET%"=="achievements" goto :run_achievements
if /I "%TARGET%"=="titles" goto :run_titles
if /I "%TARGET%"=="rewards" goto :run_rewards

echo Unknown target: %TARGET%
echo.
goto :usage

:run_all
call :ensure_output quests
echo.
echo Running XP4Life Icons Part A: quests
"%ART_PYTHON%" "%ART_SCRIPT%" --batch "%VAULT_ROOT%\ICON\XP4Life\part-a\prompts\quests" --output-dir "%VAULT_ROOT%\ICON\XP4Life\part-a\generated\quests" --preset icon --style fine-line --style geometric !FORWARD_ARGS!
if errorlevel 1 exit /b %ERRORLEVEL%

call :ensure_output achievements
echo.
echo Running XP4Life Icons Part A: achievements
"%ART_PYTHON%" "%ART_SCRIPT%" --batch "%VAULT_ROOT%\ICON\XP4Life\part-a\prompts\achievements" --output-dir "%VAULT_ROOT%\ICON\XP4Life\part-a\generated\achievements" --preset icon --style fine-line --style geometric !FORWARD_ARGS!
if errorlevel 1 exit /b %ERRORLEVEL%

call :ensure_output titles
echo.
echo Running XP4Life Icons Part A: titles
"%ART_PYTHON%" "%ART_SCRIPT%" --batch "%VAULT_ROOT%\ICON\XP4Life\part-a\prompts\titles" --output-dir "%VAULT_ROOT%\ICON\XP4Life\part-a\generated\titles" --preset icon --style fine-line --style geometric --style mystica !FORWARD_ARGS!
if errorlevel 1 exit /b %ERRORLEVEL%

call :ensure_output rewards
echo.
echo Running XP4Life Icons Part A: rewards
"%ART_PYTHON%" "%ART_SCRIPT%" --batch "%VAULT_ROOT%\ICON\XP4Life\part-a\prompts\rewards" --output-dir "%VAULT_ROOT%\ICON\XP4Life\part-a\generated\rewards" --preset icon --style fine-line --style geometric --style mystica !FORWARD_ARGS!
exit /b %ERRORLEVEL%

:run_quests
call :ensure_output quests
echo Running XP4Life Icons Part A: quests
"%ART_PYTHON%" "%ART_SCRIPT%" --batch "%VAULT_ROOT%\ICON\XP4Life\part-a\prompts\quests" --output-dir "%VAULT_ROOT%\ICON\XP4Life\part-a\generated\quests" --preset icon --style fine-line --style geometric !FORWARD_ARGS!
exit /b %ERRORLEVEL%

:run_achievements
call :ensure_output achievements
echo Running XP4Life Icons Part A: achievements
"%ART_PYTHON%" "%ART_SCRIPT%" --batch "%VAULT_ROOT%\ICON\XP4Life\part-a\prompts\achievements" --output-dir "%VAULT_ROOT%\ICON\XP4Life\part-a\generated\achievements" --preset icon --style fine-line --style geometric !FORWARD_ARGS!
exit /b %ERRORLEVEL%

:run_titles
call :ensure_output titles
echo Running XP4Life Icons Part A: titles
"%ART_PYTHON%" "%ART_SCRIPT%" --batch "%VAULT_ROOT%\ICON\XP4Life\part-a\prompts\titles" --output-dir "%VAULT_ROOT%\ICON\XP4Life\part-a\generated\titles" --preset icon --style fine-line --style geometric --style mystica !FORWARD_ARGS!
exit /b %ERRORLEVEL%

:run_rewards
call :ensure_output rewards
echo Running XP4Life Icons Part A: rewards
"%ART_PYTHON%" "%ART_SCRIPT%" --batch "%VAULT_ROOT%\ICON\XP4Life\part-a\prompts\rewards" --output-dir "%VAULT_ROOT%\ICON\XP4Life\part-a\generated\rewards" --preset icon --style fine-line --style geometric --style mystica !FORWARD_ARGS!
exit /b %ERRORLEVEL%

:ensure_output
if not exist "%VAULT_ROOT%\ICON\XP4Life\part-a\generated\%~1" mkdir "%VAULT_ROOT%\ICON\XP4Life\part-a\generated\%~1"
exit /b 0

:usage
echo Usage:
echo   run-icons-part-a.bat [all^|quests^|achievements^|titles^|rewards] [extra generator args]
echo.
echo Examples:
echo   run-icons-part-a.bat --dry-run
echo   run-icons-part-a.bat quests
echo   run-icons-part-a.bat titles --rerun rune-sigil
exit /b 1
