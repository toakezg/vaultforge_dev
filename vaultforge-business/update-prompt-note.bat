@echo off
setlocal

powershell -ExecutionPolicy Bypass -File "%~dp0update-prompt-note.ps1" %*
