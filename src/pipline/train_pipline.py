import os,sys
from src.logging.logger import logging
from src.exception.exception import CustomException
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_train import ModelTrain

obj=DataIngestion()
train_data,test_data=obj.initate_data_ingestion()

obj=DataTransformation()
train_arr,test_arr=obj.initate_data_transformation(train_data=train_data,test_data=test_data)

obj=ModelTrain()
print(obj.initate_model_train(train_arr,test_arr))