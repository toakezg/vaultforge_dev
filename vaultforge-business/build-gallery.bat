@echo off
setlocal

powershell -ExecutionPolicy Bypass -File "%~dp0build-gallery.ps1" %*
