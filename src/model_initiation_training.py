import logging
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier

from abc import ABC,abstractmethod
import numpy as np
import pandas as pd
@abstractmethod
class ModelTraining(ABC):
    def fitting_the_model(self,X_train:np.ndarray,Y_train:pd.DataFrame):
        pass


class Gradient_Boosting(ModelTraining):
    def fitting_the_model(self,X_train:np.ndarray,Y_train:pd.DataFrame):
        try:
            pass
        except Exception as e:
            logging.error(f'Error Fitting Gradient Boosting Model{e}')
            raise e
                                                                                
class ADA_Boosting(ModelTraining):
    def fitting_the_model(self,X_train:np.ndarray,Y_train:pd.DataFrame):
        try:
            pass
        except Exception as e:
            logging.error(f'Error Fitting ADA_Boosting Model{e}')
            raise e

class XGB_Boosting(ModelTraining):
    def fitting_the_model(self,X_train:np.ndarray,Y_train:pd.DataFrame):
        try:
            pass
        except Exception as e:
            logging.error(f'Error Fitting XGB_Boosting Model{e}')
            raise e


