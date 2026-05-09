@echo off
setlocal EnableExtensions

set "ROOT=%~dp0"
if "%ROOT:~-1%"=="\" set "ROOT=%ROOT:~0,-1%"

if not exist "%ROOT%\run_workflow_b.bat" (
    echo ERROR: Workflow B launcher not found:
    echo %ROOT%\run_workflow_b.bat
    exit /b 1
)

set "WATCH_CMD=%TEMP%\vaultforge_workflow_b_watch_%RANDOM%_%RANDOM%.cmd"

> "%WATCH_CMD%" echo @echo off
>> "%WATCH_CMD%" echo title VaultForge Workflow B Watch
>> "%WATCH_CMD%" echo cd /d "%ROOT%"
>> "%WATCH_CMD%" echo echo ========================================
>> "%WATCH_CMD%" echo echo VaultForge Workflow B watch window
>> "%WATCH_CMD%" echo echo Root: %ROOT%
>> "%WATCH_CMD%" echo echo Started: %%DATE%% %%TIME%%
>> "%WATCH_CMD%" echo echo ========================================
>> "%WATCH_CMD%" echo echo.
>> "%WATCH_CMD%" echo call "%ROOT%\run_workflow_b.bat" --terminal-detail verbose %*
>> "%WATCH_CMD%" echo set "WF_EXIT=%%ERRORLEVEL%%"
>> "%WATCH_CMD%" echo echo.
>> "%WATCH_CMD%" echo echo ========================================
>> "%WATCH_CMD%" echo echo Workflow B finished with exit code %%WF_EXIT%%
>> "%WATCH_CMD%" echo echo.
>> "%WATCH_CMD%" echo echo Exit code guide:
>> "%WATCH_CMD%" echo echo   0   normal finish, budget/timebox stop, or dry-run finish
>> "%WATCH_CMD%" echo echo   3   hard gate stop from an agent signal
>> "%WATCH_CMD%" echo echo   130 operator cancelled with Ctrl+C; check workflow-b-cancel-handoff.md
>> "%WATCH_CMD%" echo echo   127 Codex CLI launch failure or missing executable
>> "%WATCH_CMD%" echo echo   other Codex CLI or agent process return code
>> "%WATCH_CMD%" echo echo.
>> "%WATCH_CMD%" echo echo Latest run packets:
>> "%WATCH_CMD%" echo powershell -NoProfile -ExecutionPolicy Bypass -Command "Get-ChildItem -LiteralPath '%ROOT%\runs\workflow-b' -Directory -ErrorAction SilentlyContinue ^| Sort-Object LastWriteTime -Descending ^| Select-Object -First 3 Name,LastWriteTime ^| Format-Table -AutoSize"
>> "%WATCH_CMD%" echo echo.
>> "%WATCH_CMD%" echo echo Check workflow-b-live-status.md, checkpoints.jsonl, status.jsonl, workflow-b-cancel-handoff.md, and workflow-b-error-guide.md if present.
>> "%WATCH_CMD%" echo echo ========================================
>> "%WATCH_CMD%" echo pause
>> "%WATCH_CMD%" echo exit /b %%WF_EXIT%%

start "VaultForge Workflow B Watch" cmd.exe /k "%WATCH_CMD%"
exit /b 0
