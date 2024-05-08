import os,sys
import pandas as pd
from dataclasses import dataclass
from pathlib import Path
from sklearn.model_selection import train_test_split


from src.logging.logger import logging
from src.exception.exception import CustomException



@dataclass
class DataIngestionConfig:
  
   raw_data:Path=os.path.join('artifacts/raw.csv')
   train_data:Path=os.path.join('artifacts/train.csv')
   test_data: Path=os.path.join('artifacts/test.csv')

class DataIngestion:
   def __init__(self) -> None:
        self.data_ingestion_config=DataIngestionConfig()

   def initate_data_ingestion(self):
      try:
         logging.info('=================== Data ingestion =================')

         df=pd.read_csv('NoteBook/data.csv')

         # os.makedirs(
         #         os.path.dirname(self.data_ingestion_config.raw_data), exist_ok=True
         #    )

         # df.to_csv(self.data_ingestion_config.raw_data)

         train_data,test_data=train_test_split(df,test_size=0.29,random_state=40)

         train_data.to_csv(self.data_ingestion_config.train_data,header=True,index=False)
         test_data.to_csv(self.data_ingestion_config.test_data,header=True,index=False)

         print(train_data.head())

         logging.info('================Data Ingestion competed================')
         return(
            self.data_ingestion_config.train_data,
            self.data_ingestion_config.test_data
         )

      except Exception as e:
         logging.info(f'Error occured {str(e)}')
         CustomException(sys,e)
    

      
