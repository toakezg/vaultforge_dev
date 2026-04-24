@echo off
setlocal

powershell -ExecutionPolicy Bypass -File "%~dp0run_business.ps1" ^
  "A clean, readable brand mark for a local service business called Smoke Test Studio." ^
  -Client "smoke-test" ^
  -AssetType "logo" ^
  -Job "smoke" ^
  -Tag "local, trustworthy, clear" ^
  -Preset "business-logo" ^
  -Style "clean-corporate" ^
  -Mod "small-size-readable" ^
  -TransparentSafe ^
  -DryRun
