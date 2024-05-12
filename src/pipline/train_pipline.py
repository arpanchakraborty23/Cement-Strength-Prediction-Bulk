import os,sys
from src.logging.logger import logging
from src.exception.exception import CustomException
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_train import ModelTrain

class TrainPipeline:
    def __init__(self) -> None:
         pass
    def pipline(self):
         try:
              logging.info('**************** TrainPipline *****************')
              data_ingestion=DataIngestion()
              data_ingestion.initate_data_ingestion()

              data_transformation=DataTransformation()
              data_transformation.initate_data_transformation()

              model_train=ModelTrain()
              model_train.initate_model_train()

              logging.info('**************** TrainPipline Completed *****************')
         except Exception as e:
              logging.info(f' Errror occured {str(e)}')
              raise CustomException(sys,e)
         
if __name__=='__main__':
     obj=TrainPipeline()
     obj.pipline()