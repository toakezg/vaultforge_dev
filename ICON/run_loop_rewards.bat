@echo off
setlocal
call "%~dp0run-icons-part-a.bat" rewards --limit 11 --rerun weapon --rerun gear --rerun keys --style pixel
exit /b %ERRORLEVEL%
