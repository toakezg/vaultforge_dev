@echo off
setlocal

powershell -ExecutionPolicy Bypass -File "%~dp0build-contact-sheets.ps1" %*
