import shutil
import os,sys
import pickle
import pandas as pd

from src.logging.logger import logging
from src.exception.exception import CustomException
from flask import request
from src.utils.utils import load_obj

from dataclasses import dataclass

@dataclass
class PradictionPiplineConfig:
    prediction_output_dirname: str = "predictions"
    prediction_file_name:str =  "predicted_file.csv"
    model_file_path: str = os.path.join("model/model.pkl" )
    preprocessor_path: str = os.path.join("preprocess\preprocess.pkl")
    prediction_file_path:str = os.path.join(prediction_output_dirname,prediction_file_name)

class PredictionPipeline:
    def __init__(self,):
        
        logging.info('bulk_ prediction config')
        self.pradiction_pipline_config=PradictionPiplineConfig()

    def save_input_file(self)->str:
        try:
            #creating the file
            pred_file_input_dir = "prediction_artifacts"
            os.makedirs(pred_file_input_dir, exist_ok=True)

            input_csv_file = request.files['file']
            pred_file_path = os.path.join(pred_file_input_dir, input_csv_file.filename)
            
            input_csv_file.save(pred_file_path)

          

            return pred_file_path


        except Exception as e:
            logging.info(f'Error in input file {str(e)}')
            raise CustomException (sys,e)


    def predict(self,features):
        try:
            model=load_obj('artifacts\model.pkl')
            preprocesser=load_obj('preprocess\preprocess.pkl')
          
            scale=preprocesser.transform(features)
            pred=model.predict(scale)

            return pred

        except Exception as e:
            logging.info(f'Error in prediction {str(e)}')
            raise CustomException (sys,e)    


    def get_predicted_dataframe(self, input_dataframe_path:pd.DataFrame):
        try:
            
            input_dataframe=pd.read_csv(input_dataframe_path)
            
            Target_column='concrete_compressive_strength'
          

            input_dataframe = input_dataframe.drop(columns=[Target_column ],axis=1) 
            prediction=self.predict(input_dataframe)
            input_dataframe[Target_column]=[pred for pred in prediction]




            # saving pradiction col as csv
            os.makedirs(self.pradiction_pipline_config.prediction_output_dirname,exist_ok=True)

            input_dataframe.to_csv(self.pradiction_pipline_config.prediction_file_path,index=False)

            
            logging.info("predictions completed. ")

        except Exception as e:
            logging.info(f" error {str(e)}")
            raise CustomException(e, sys) from e


    def run_pipline(self):
        try:
            input_csv_path=self.save_input_file()
            self.get_predicted_dataframe(input_dataframe_path=input_csv_path)

            return self.pradiction_pipline_config

        except Exception as e:
            logging.info(f" error {str(e)}")
            raise CustomException(e, sys) from e
        



            
