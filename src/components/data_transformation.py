import os,sys
import pandas as pd
import numpy as np
from sklearn.preprocessing import RobustScaler,StandardScaler
from sklearn.pipeline import Pipeline
from dataclasses import dataclass

from src.logging.logger import logging
from src.exception.exception import CustomException
from src.utils.utils import save_obj

@dataclass
class DataTransformationConfig:
    preprocess_obj=os.path.join('preprocess/preprocess.pkl')
    train_data=os.path.join('artifacts/train.csv')
    test_data=os.path.join('artifacts/test.csv')
    train_arr=os.path.join('artifacts/train_arr.npy')
    test_arr=os.path.join('artifacts/test_arr.npy')



class DataTransformation:
    def __init__(self) -> None:
        self.data_transformation_config=DataTransformationConfig()

    def get_transformation_obj(self):
        preprocess_obj=Pipeline(
            steps=[
                ('Scaler',StandardScaler())
            ]
        )
        return preprocess_obj

    def initate_data_transformation(self):
        try:
            logging.info('============== Data Transformation ============== ')

            train_data=pd.read_csv(self.data_transformation_config.train_data)
            test_data=pd.read_csv(self.data_transformation_config.test_data)

            Traget_col='concrete_compressive_strength'

            input_feature_train_data=train_data.drop(columns=Traget_col,axis=1)
            target_feature_train_data=train_data[Traget_col]

            input_feature_test_data=test_data.drop(columns=Traget_col,axis=1)
            target_feature_test_data=test_data[Traget_col]

            scaler=self.get_transformation_obj()
            logging.info('preprocesser loded')

            transform_input_feature_train_data=scaler.fit_transform(input_feature_train_data)

            transform_input_feature_test_data=scaler.transform(input_feature_test_data)

            train_arr=np.c_[transform_input_feature_train_data,np.array(target_feature_train_data)]

            test_arr=np.c_[transform_input_feature_test_data,np.array(target_feature_test_data)]

            np.save(self.data_transformation_config.train_arr,train_arr)
            np.save(self.data_transformation_config.test_arr,test_arr)

            save_obj(
                file_path=self.data_transformation_config.preprocess_obj,
                obj=scaler
            )

            logging.info('============== Data Transformation Completed ============== ')
            return(
                train_arr,
                test_arr
            )

            

        except Exception as e:
            logging.info(f'Error occured {str(e)}')
            raise CustomException(sys,e)