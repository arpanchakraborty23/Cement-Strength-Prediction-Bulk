import os,sys
from src.logging.logger import logging
from src.exception.exception import CustomException
from src.components.data_ingestion import DataIngestion

obj=DataIngestion()
train_data,test_data=obj.initate_data_ingestion()

