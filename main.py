import pandas as pd
import csv
import argparse
from datetime import datetime
import os
import shutil
import glob

from pydantic import BaseModel, ValidationError
from typing import Optional, Type, Union, Annotated, get_origin, get_args
import paramiko
from dotenv import dotenv_values

from models.odh import ODH
from models.odl import ODL
from models.pah import PAH
from models.pal import PAL
from models.sku import SKU

from logger import logger

def get_fields_by_type(model_class: Type[BaseModel], target_type: Type) -> dict[str, Type]:
    matching_fields = {}
    def matches_type(ann) -> bool:
        if ann is target_type:
            return True
        origin = get_origin(ann)
        if origin is Annotated:
            base_type = get_args(ann)[0]
            return matches_type(base_type)
        if origin in (Optional, Union):
            args = get_args(ann)
            return any(matches_type(arg) for arg in args if arg is not type(None))
        return False
    for field_name, field_info in model_class.model_fields.items():
        annotation = field_info.annotation
        if matches_type(annotation):
            matching_fields[field_name] = target_type
    return matching_fields

def build_order_header(input_file, suffix):
    df = pd.read_excel(input_file, sheet_name='odh', converters=get_fields_by_type(ODH, str), na_filter=False)
    df = df.replace('', None)
    data = df.to_dict(orient="records")
    if len(data) > 0:
        rows = [ODH(**item).model_dump() for item in data]
        with open(f'IF_ODH_{suffix}.txt', 'w', newline='', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=ODH.model_fields.keys())
            writer.writerows(rows)
            logger.info(f'IF_ODH_{suffix}.txt')

def build_order_line(input_file, suffix):
    df = pd.read_excel(input_file, sheet_name='odl', converters=get_fields_by_type(ODL, str), na_filter=False)
    df = df.replace('', None)
    data = df.to_dict(orient="records")
    if len(data) > 0:
        rows = [ODL(**item).model_dump() for item in data]
        with open(f'IF_ODL_{suffix}.txt', 'w', newline='', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=ODL.model_fields.keys())
            writer.writerows(rows)
            logger.info(f'IF_ODL_{suffix}.txt')

def build_pa_header(input_file, suffix):
    df = pd.read_excel(input_file, sheet_name='pah', converters=get_fields_by_type(PAH, str), na_filter=False)
    df = df.replace('', None)
    data = df.to_dict(orient="records")
    if len(data) > 0:
        rows = [PAH(**item).model_dump() for item in data]
        with open(f'IF_PAH_{suffix}.txt', 'w', newline='', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=PAH.model_fields.keys())
            writer.writerows(rows)
            logger.info(f'IF_PAH_{suffix}.txt')

def build_pa_line(input_file, suffix):
    df = pd.read_excel(input_file, sheet_name='pal', converters=get_fields_by_type(PAL, str), na_filter=False)
    df = df.replace('', None)
    data = df.to_dict(orient="records")
    if len(data) > 0:
        rows = [PAL(**item).model_dump() for item in data]
        with open(f'IF_PAL_{suffix}.txt', 'w', newline='', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=PAL.model_fields.keys())
            writer.writerows(rows)
            logger.info(f'IF_PAL_{suffix}.txt')



def build_sku(input_file, suffix):
    # Step 1: Read and normalize input
    df = pd.read_excel(input_file, sheet_name='sku', converters=get_fields_by_type(SKU, str), na_filter=False)
    df.replace('', None, inplace=True)

    if not df.empty:
        # Step 2: Validate and normalize using Pydantic model
        df = df.apply(lambda row: pd.Series(SKU(**row).model_dump()), axis=1)

        # Step 3: Prepare for CSV output — convert to string
        def prepare_for_export(row):
            return {
                k: (
                    '@' if row['Merge_Action'] == 'U' and pd.isna(v)
                    else '' if pd.isna(v)
                    else v
                )
                for k, v in row.items()
            }

        export_rows = df.apply(prepare_for_export, axis=1).tolist()

        # Step 4: Write to CSV
        with open(f'IF_SKU_{suffix}.txt', 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=SKU.model_fields.keys())
            writer.writeheader()
            writer.writerows(export_rows)

        logger.info(f'IF_SKU_{suffix}.txt')

def sftp_upload(host, port, username, password, filenames, remote_folder, backup, debug_mode=False):
    if debug_mode != True:
        with paramiko.SSHClient() as ssh:
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname=host, port=port, username=username, password=password, look_for_keys=False)
            sftp = ssh.open_sftp()
            sftp.chdir(remote_folder)
            for filename in filenames:
                sftp.put(localpath=os.path.join(os.getcwd(), filename), remotepath=filename)
                shutil.move(src=os.path.join(os.getcwd(), filename), dst=os.path.join(os.getcwd(), backup, filename))
            logger.info(f'Uploaded {filenames}')
    else:
        logger.info('Running in --debug mode, no sftp upload!')

def main():
    try:
        parser = argparse.ArgumentParser(description='Alert Email for DG items in Order')
        parser.add_argument('--order', action="store_true", help="Build ORDER", required = False)
        parser.add_argument('--pa', action="store_true", help="Build PA", required = False)
        parser.add_argument('--sku', action="store_true", help="Build SKU", required = False)
        parser.add_argument('--debug', action="store_true", help="Run in debug mode", required = False)
        parser.add_argument('--environment', '-e', help='Environment to run in: uat or prod (default: uat)', type=str, choices=['uat', 'prod'], required=False, default='uat')
        parser.add_argument('--name', '-m', help='Output filename suffix', type=str, required=False)
        args = parser.parse_args()

        if not os.path.isfile(f'.env.{args.environment}'):
            logger.error(f'.env.{args.environment} not existed')
        else:
            logger.info(f'Environment to run in: {str.upper(args.environment)}')
            env = dotenv_values(f'.env.{args.environment}')
            name_prefix = getattr(args, 'name', '') or ''
            sufffix_with_ymdhms = f'{name_prefix}_{datetime.now().strftime('%y%m%d%H%M%S')}'

            input_file = 'IF_Input.xlsx'
            if args.order == True:
                build_order_header(input_file, sufffix_with_ymdhms)
                build_order_line(input_file, sufffix_with_ymdhms)  
            elif args.pa == True:
                build_pa_header(input_file,sufffix_with_ymdhms) 
                build_pa_line(input_file, sufffix_with_ymdhms)
            elif args.sku == True:
                build_sku(input_file, sufffix_with_ymdhms)

            sftp_upload(host=env.get('sftp_host'), port=env.get('sftp_port'),
                    username=env.get('sftp_username'), password=env.get('sftp_password'),
                    remote_folder=env.get('sftp_remote_folder'), filenames=glob.glob('IF*.txt'),
                    backup=f'backup_{args.environment}',
                    debug_mode=args.debug)
            
    except ValidationError as e:
        logger.error(e.errors())
    except IOError as e:
        logger.error(e)
    except Exception as e:
        logger.exception(e)
    finally:
        pass

if __name__ == '__main__':
    main()