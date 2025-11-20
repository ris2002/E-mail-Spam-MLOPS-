import logging
from typing import Tuple
from cleaning_data import PreProcessStrategy
from typing_extensions import Annotated
import numpy as np
import pandas as pd
def vectorized_and_split_data(df:pd.DataFrame)->Tuple[
        Annotated[np.ndarray,"X_Train"],
        Annotated[np.ndarray,"X_Test"],
        Annotated[pd.DataFrame,"Y_Train"],
        Annotated[pd.DataFrame,"Y_Test"]
        ]:
    try:
        x=PreProcessStrategy()
        preprocess_data=x.clean_data(df)
        X_Train_df,X_Test_df,Y_Train,Y_Test=x.vectorize_train_and_split(preprocess_data)
        logging.info('Successfully vectorized and split tthe data')
        return X_Train_df,X_Test_df,Y_Train,Y_Test
    except Exception as e:
        logging.error(f'Error while vectorizing and splitting the data')
        raise e