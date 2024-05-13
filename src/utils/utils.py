import os,sys
import yaml
import pandas as pd 
import numpy as np
import pickle
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error
from sklearn.metrics import r2_score
from sklearn.model_selection import RandomizedSearchCV,GridSearchCV

from src.logging.logger import logging
from src.exception.exception import CustomException

def save_obj(file_path,obj):
        dir=os.path.dirname(file_path)
        os.makedirs(dir,exist_ok= True)

        with open(file_path,'wb') as f:
            pickle.dump(obj,f)
            logging.info(f"Saved object in {file_path}")

def load_obj(file_path):
    try:
        with open(file_path,'rb') as file_obj:
            return pickle.load(file_obj)

       
    except Exception as e:
            raise CustomException(e,sys) from e

def model_evaluate(x_train, y_train, x_test, y_test, models,params):
    try:
        report = {}

        
        for i in range(len(models)):
            model = list(models.values())[i]
            para=params[list(models.keys())[i]]
            gs=GridSearchCV(model,param_grid=para,cv=5,verbose=3,refit=True,scoring='neg_mean_squared_error',n_jobs=-1)

            
            gs.fit(x_train,y_train)
            y_pred=gs.predict(x_test)

            # model.fit(x_train,y_train)
            # y_pred=model.predict(x_test)
            
            accuracy=r2_score(y_test,y_pred)
            # Calculate mean absolute error
            mae = mean_absolute_error(y_test, y_pred)
       

            # Calculate mean squared error
            mse = mean_squared_error(y_test, y_pred)
          
            report[list(models.keys())[i]] =[
                f'Accuracy: {accuracy:.2f}%  MAE: {mae:.2f}%  MSE: {mse:.2f}%'   
            ]
            sns.regplot(x=y_test,y=y_pred,ci=None,color='indianred')
           
            plt.title([list(models.keys())[i]] )
            plt.show()
        return report
    except Exception as e:
            logging.info('Error ',str(e))
            raise CustomException(sys,e)
