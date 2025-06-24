Make sure to have .env file
sftp_host=''
sftp_port=''
sftp_username=''
sftp_password=''
sftp_remote_folder='/'

to explore how to use, run the command: python main.py -h
usage: main.py [-h] [--order] [--pa] [--debug] [--environment {uat,prod}]

Alert Email for DG items in Order

options:
  -h, --help            show this help message and exit
  --order               Build ORDER
  --pa                  Build PA
  --debug               Run in debug mode
  --environment, -e {uat,prod}
                        Environment to run in: uat or prod (default: uat)


build order files (ODH, ODL) in PROD, run the command: python main.py --order -e prod
build order files (PAH, PAL) in PROD, run the command: python main.py --order -e prod

.bat file
@echo off
set pwd=%userprofile%\Projects\rwsif
call "%pwd%\venv\Scripts\activate.bat"
python main.py --order
PAUSE

Notes: Make sure to input correct values to IF_Input.xlsx file
Make sure to have backup_prod or backup_uat