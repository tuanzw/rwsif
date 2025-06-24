@echo off
set pwd=%userprofile%\Projects\rwsif
call %pwd%\venv\Scripts\activate.bat
python main.py --order
PAUSE