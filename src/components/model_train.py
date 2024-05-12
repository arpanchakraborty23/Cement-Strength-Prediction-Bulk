import os,sys
import pandas as pd
import numpy as np
from dataclasses import dataclass
from pathlib import Path
from sklearn.linear_model import LinearRegression,ElasticNet
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor,BaggingRegressor,GradientBoostingRegressor
from sklearn.neighbors import KDTree
from sklearn.svm import SVR

from src.logging.logger import logging
from src.exception.exception import CustomException
from src.utils.utils import save_obj,model_evaluate

@dataclass
class ModelTrainConfig:
    model:Path=os.path.join('model/model.pkl')

class ModelTrain:
    def __init__(self) -> None:
        self.config=ModelTrainConfig()

    def initate_model_train(self):
        try:
            logging.info('===================== Model Train =====================')
            train_array=np.load('artifacts/train_arr.npy')
            test_array=np.load('artifacts/test_arr.npy')

            print(train_array)
        
            x_train, y_train, x_test, y_test = (
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )
          
           
            logging.info('Data loded')

            models={
               
                'BaggingRegressor':BaggingRegressor(),
                'SVR':SVR(),
                'GradientBoosting': GradientBoostingRegressor(),
                'Linear Regression': LinearRegression(),
                'ElasticNet':ElasticNet(),
                'DecisionTreeRegressor':DecisionTreeRegressor(), 
                'RandomForest': RandomForestRegressor()
            }        

            params={
                'BaggingRegressor':{
                     'n_estimators': [10, 100, 50],
                     'bootstrap':[True,False],
                     'oob_score':[True,False],
                },
                'SVR': {
                    'C': [0.1, 1, 10],
                    'kernel': ['linear', 'rbf', 'poly'],
                    'gamma': ['scale', 'auto']
                },
                'GradientBoosting': {
                    'learning_rate': [0.01, 0.1, 0.2],
                    'n_estimators': [50, 100, 200],
                    'max_depth': [3, 4, 5],
                    'subsample': [0.8, 1.0]
                },
                'Linear Regression':  {
                    'fit_intercept': [True, False]
                },
                'ElasticNet': {
                     'alpha': [0.6, 0.5, 0.4],            
                     'l1_ratio': [0.4, 0.5, 0.14],        
                     'selection': ['cyclic', 'random']
                },
                'DecisionTreeRegressor':{
                     'max_depth': [None, 5, 10, 15], 
                    'min_samples_split': [2, 5, 10],   
                    'min_samples_leaf': [1, 2, 4] 

                },
                'RandomForest':  {
                    'n_estimators': [50, 100, 200],
                    'max_depth': [None, 10, 20, 30],
                    'min_samples_split': [2, 5, 10],
                    'min_samples_leaf': [1, 2, 4]
                }
            }

            model_report:dict=model_evaluate(x_train=x_train,y_train=y_train,x_test=x_test,y_test=y_test,models=models,params=params)   
            print(model_report)

            logging.info(f' model report {model_report}')

            best_model_score=max(sorted(model_report.values()))

            best_model_name=list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            best_model=models[best_model_name]

            print(f'Best Model Found , Model Name : {best_model_name} , Score : {best_model_score}')
            print('\n====================================================================================\n')
            logging.info(f'Best Model Found , Model Name : {best_model_name} , Score : {best_model_score}')

            save_obj(
                file_path=self.config.model,
                obj=best_model
            )
            logging.info('===================== Model Train Completed =====================')
        except Exception as e:
            logging.info('Error ',str(e))
            raise CustomException(sys,e)
