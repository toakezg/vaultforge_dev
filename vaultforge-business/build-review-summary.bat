@echo off
setlocal
powershell -ExecutionPolicy Bypass -File "%~dp0build-review-summary.ps1" %*
