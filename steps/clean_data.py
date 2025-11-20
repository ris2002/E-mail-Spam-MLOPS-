import logging
from typing import Tuple
from cleaning_data import PreProcessStrategy
from typing_extensions import Annotated
import numpy as np
import pandas as pd
from airflow.decorators import dag, task
import pickle

@task
def vectorized_and_split_data(df:pd.DataFrame)->Tuple[
        Annotated[np.ndarray,"X_Train"],
        Annotated[np.ndarray,"X_Test"],
        Annotated[pd.DataFrame,"Y_Train"],
        Annotated[pd.DataFrame,"Y_Test"]
        ]:
    try:
        x=PreProcessStrategy()
        preprocess_data=x.clean_data(df)
        X_Train,X_Test,Y_Train,Y_Test=x.vectorize_train_and_split(preprocess_data)
        logging.info('Successfully vectorized and split tthe data')
        logging.info(f'X_Train{X_Train.shape},Y_Train{Y_Train.shape},X_Test{X_Test.shape},Y_Test{Y_Test.shape}')
        with open('/opt/airflow/config/x_train.pkl','wb') as f:
            pickle.dump(X_Train,f)
        with open('/opt/airflow/config/y_train.pkl','wb') as f:
            pickle.dump(Y_Train,f)
        with open('/opt/airflow/config/x_test.pkl','wb') as f:
            pickle.dump(X_Test,f)
        with open('/opt/airflow/config/y_test.pkl','wb') as f:
            pickle.dump(Y_Test,f)

    except Exception as e:
        logging.error(f'Error while vectorizing and splitting the data')
        raise e