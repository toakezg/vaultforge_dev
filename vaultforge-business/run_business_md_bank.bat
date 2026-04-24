@echo off
setlocal

powershell -ExecutionPolicy Bypass -File "%~dp0run_business_md_bank.ps1" %*
