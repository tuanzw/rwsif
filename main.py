
import argparse
from datetime import datetime
import os
import glob
from dotenv import dotenv_values
from pydantic import ValidationError

from logger import logger
from app import *

def main():
    try:
        parser = argparse.ArgumentParser(description='Alert Email for DG items in Order')
        parser.add_argument('--order', action="store_true", help="Build ORDER", required = False)
        parser.add_argument('--pa', action="store_true", help="Build PA", required = False)
        parser.add_argument('--sku', action="store_true", help="Build SKU", required = False)
        parser.add_argument('--skc', action="store_true", help="Build SKC", required = False)
        parser.add_argument('--ssc', action="store_true", help="Build SSC", required = False)
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
            suffix_with_ymdhms = f'{name_prefix}_{datetime.now().strftime('%y%m%d%H%M%S')}'

            input_file = 'IF_Input.xlsx'
            if args.order:
                build_order_header(input_file, suffix_with_ymdhms)
                build_order_line(input_file, suffix_with_ymdhms)  
            elif args.pa:
                build_pa_header(input_file,suffix_with_ymdhms) 
                build_pa_line(input_file, suffix_with_ymdhms)
            elif args.sku:
                build_sku(input_file, suffix_with_ymdhms)
            elif args.skc:
                build_skc(input_file, suffix_with_ymdhms)
            elif args.ssc:
                build_ssc(input_file, suffix_with_ymdhms)
            elif args.rcv:
                build_rcv(input_file, suffix_with_ymdhms)

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