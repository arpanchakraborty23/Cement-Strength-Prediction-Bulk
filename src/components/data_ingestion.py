import os,sys
import pandas as pd
from dataclasses import dataclass
from pathlib import Path
from sklearn.model_selection import train_test_split

from src.constant.ymal_path import *
from src.logging.logger import logging
from src.exception.exception import CustomException
from src.utils.utils import read_yaml,create_dir


@dataclass
class DataIngestionConfig:
   dir:Path
   raw:Path
   train_data:Path
   test_data: Path

class DataIngestion:
   def __init__(self,config=config_file_path):
      self.config=read_yaml(config)

      create_dir([self.config.artifacts_root])

      config=self.config.data_ingestion

      self.config_manager=DataIngestionConfig(
         dir=config.dir,
         raw=config.raw,
         test_data=config.test_data,
         train_data=config.train_data
      )
      return self.config_manager
   
   def initate_data_ingestion(self):

    try:
        logging.info('data_ingestion has started')
        df=pd.read_csv('NoteBook\data.csv')
        print(df.head())
        
        df.to_csv(self.config_manager.raw)

        train_data,test_data=train_test_split(df,test_size=0.3,random_state=42)

        train_data.to_csv(self.config_manager.train_data)

        test_data=test_data.to_csv(self.config_manager.test_data)

        return (
           self.config_manager.train_data,
           self.config_manager.test_data
        )


    except Exception as e:
        logging.info('Error',str(e))
        raise CustomException(sys,e)
    
if __name__=='__main__':
   obj=DataIngestion()
   train_data,test_data=obj.initate_data_ingestion()
      
