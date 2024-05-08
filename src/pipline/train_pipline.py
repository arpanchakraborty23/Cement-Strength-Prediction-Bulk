import os,sys
from src.logging.logger import logging
from src.exception.exception import CustomException
from src.components.data_ingestion import DataIngestion

class TrainPipline:
    def __init__(self) -> None:
        pass
    def pipline():
        obj=DataIngestion()
        train_data,test_data=obj.initate_data_ingestion()

if __name__=='__main__':
    try:
        STAGE_NAME='Data Ingestion'
        logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = TrainPipline
        obj.pipline()
        logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logging.info('error' ,str(e))
        raise CustomException(sys,e) 
        