@echo off
setlocal
call "%~dp0run-icons-part-a.bat" rewards --limit 10 --style pixel
exit /b %ERRORLEVEL%
