---
tags:
  - nath
  - note
  - setup
---

___
When you want to randomly generate  a new something, say a new icon for a dir or file, the method used for it was:

go to 
```r
/my-prompts-bank/
```
and create a folder for what it is, in this case Gallable
like this:
```r
/my-prompts-bank/Gallable
```

then head to:
```r
vaultforge-business/my-prompts-bank/_template
```
create a copy of any one or more of the templates in there:
```r
brand-board-template
client-pack-template
cover-template
icon-template
logo-template
```
move the copied template into the folder you made
```r
/my-prompts-bank/Gallable
```
adjust the properties in the template and type in your prompt.

when ready to run, edit .bat file found in business root dir:
(edit showing green here "file-path' & if `count==10` to `x` )
```r
@echo off
set count=0

:loop
if %count%==10 goto end

powershell -ExecutionPolicy Bypass -File .\run_business_md_bank.ps1 -Path ".\my-prompts-bank\Gallable\gallable-app-icon.md"

set /a count+=1
goto loop

:end
echo Done.
pause
```
and then run the bat from here or file explorer
[[run_loop_10.bat]]

this .bat is wrapped around `[[run_business_md_bank.ps1]]`
[[run_business_md_bank.ps1]]

if its failing most likely pathing issue. with 'cannot find'
right click the prompt file and copy vault path for any case error. make sure `.\` is meaning from where the .bat file is to `my-prompt-bank` and make sure all lines are `\` `backslash`

should work if not go to READMEs and any prompt templates to refer to. 

if succesful generated images will head too `.\generated\same-as-created-folder-name\then-follow-down`
in this case:
```r
vaultforge-business/generated/gallable/icon/business-icon/mono-mark/2026-04-24/job-icon-pack-01
```


