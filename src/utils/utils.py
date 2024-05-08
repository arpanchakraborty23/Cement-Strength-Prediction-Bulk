import os,sys
import yaml
import pandas as pd 
import pymysql
from dotenv import load_dotenv
load_dotenv()
host=os.getenv("host")
user=os.getenv("user")
pasword=os.getenv("pasword")
db=os.getenv('db')

from src.logging.logger import logging
from src.exception.exception import CustomException

def read_yaml(file_path):
    try:
        with open(file_path) as f:
            file=yaml.safe_load(f)
            logging.info(f'{file} has loded')

        return file

    except Exception as e:
        logging.info('Error',str(e))
        raise CustomException(sys,e)
    
def create_dir(dir):
    try:
        os.makedirs(dir,exist_ok=True)
        logging.info(f' {dir} has created')
    except Exception as e:
        logging.info('Error',str(e))
        raise CustomException(sys,e)