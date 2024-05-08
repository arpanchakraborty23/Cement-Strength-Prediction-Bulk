import os,sys
import yaml
import pandas as pd 
import pickle
from src.logging.logger import logging
from src.exception.exception import CustomException

def save_obj(file_path,obj):
        dir=os.path.dirname(file_path)
        os.makedirs(dir,exist_ok= True)

        with open(file_path,'wb') as f:
            pickle.dump(obj,f)
            logging.info(f"Saved object in {file_path}")