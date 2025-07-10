@echo off
set pwd=%userprofile%\Projects\rwsif
call %pwd%\venv\Scripts\activate.bat
start "" "pythonw.exe" "%pwd%\main.ui.py"
exit
