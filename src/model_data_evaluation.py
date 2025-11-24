import logging
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
import pandas as pd
import numpy as np
from typing import Tuple
from typing_extensions import Annotated

from sklearn.base import ClassifierMixin

class Evaluation_Techniques():
    
    def accuracy_score_function(self,predicted_model:np.ndarray,y_test:pd.DataFrame):

        try:
            acc_score=accuracy_score(y_test,predicted_model)
            logging.info(f'Successfully calculated the accuracy score:{acc_score}')
            return acc_score
            
            

        except Exception as e:
            logging.error(f'Error calculating the accuracy score :{e}')
            raise e

    def confusion_matrix_function(self,predicted_model:np.ndarray,y_test:pd.DataFrame)->Tuple[Annotated[int,'true_negatives'],Annotated[int,'true_positives'],Annotated[int,'false_negatives'],Annotated[int,'false_positives']]:

        try:
            cm=confusion_matrix(y_test,predicted_model)
            
            
            true_negatives=int(cm[0][0])
            true_positive=int(cm[1][1])
            false_negatives=int(cm[1][0])
            false_positive=int(cm[0][1])
            logging.info(f'Successfully calculated the classification_report score:{cm}')
            return true_negatives,true_positive,false_negatives,false_positive
      
        except Exception as e:
            logging.error(f'Error calculating the classification_report :{e}')
            raise e

    def classification_report_function(self,predicted_model:np.ndarray,y_test:pd.DataFrame)->str:

        try:
            reports=classification_report(y_test,predicted_model)
            logging.info(f'Successfully calculated the confusion_matrix score:{reports}')
            return reports
           
        except Exception as e:
            logging.error(f'Error calculating the confusion_matrix :{e}')
            raise e
