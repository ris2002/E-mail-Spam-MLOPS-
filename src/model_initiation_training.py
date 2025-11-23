import logging
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier

from abc import ABC,abstractmethod
import numpy as np
import pandas as pd

class ModelTraining(ABC):
    @abstractmethod
    def fitting_the_model(self,X_train:np.ndarray,Y_train:pd.DataFrame,**kwargs):

        pass


class Gradient_Boosting_Class(ModelTraining):
    def fitting_the_model(self,X_train:np.ndarray,Y_train:pd.DataFrame,**kwargs):
        try:
            model=GradientBoostingClassifier(**kwargs)
            fit_model=model.fit(X_train,Y_train)
            return fit_model
        except Exception as e:
            logging.error(f'Error Fitting Gradient Boosting Model{e}')
            raise e
                                                                                
class ADA_Boosting_Class(ModelTraining):
    def fitting_the_model(self,X_train:np.ndarray,Y_train:pd.DataFrame,**kwargs):
        try:
            model=AdaBoostClassifier(**kwargs)
            fit_model=model.fit(X_train,Y_train)
            return fit_model
        except Exception as e:
            logging.error(f'Error Fitting ADA_Boosting Model{e}')
            raise e

class XGB_Boosting_Class(ModelTraining):
    def fitting_the_model(self,X_train:np.ndarray,Y_train:pd.DataFrame,**kwargs):
        try:
            pass
        except Exception as e:
            logging.error(f'Error Fitting XGB_Boosting Model{e}')
            raise e


