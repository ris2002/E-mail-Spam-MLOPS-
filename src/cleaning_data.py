import pandas as pd
import numpy as np
import logging
import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from typing import Tuple
from typing_extensions import Annotated
import pickle

class PreProcessStrategy:
    def clean_data(self,df:pd.DataFrame)->pd.DataFrame:
        try:
            def indepth_preprocess(text):
                text=text.lower()
                text=re.sub(r'(?i)^subject:\s*','',text)#case insensittive aand only removes the header line
                return text
            df['text']=df['text'].apply(indepth_preprocess)
            dataframe=df
            return dataframe
        except Exception as e:
            logging.error(f'Errinng in cleaning the data from DataFrame {e}')
            raise e
        
    def vectorize_train_and_split(self,dataframe:pd.DataFrame)->Tuple[
        Annotated[np.ndarray,"X_Train"],
        Annotated[np.ndarray,"X_Test"],
        Annotated[pd.DataFrame,"Y_Train"],
        Annotated[pd.DataFrame,"Y_Test"]
        ]:
        try:
            X=dataframe['text']
            Y=dataframe['spam']
            X_Train_df,X_Test_df,Y_Train,Y_Test=train_test_split(X,Y,test_size=0.2,random_state=2)
            tfid=TfidfVectorizer(max_features=5000,ngram_range=(1,2))
            X_Train=tfid.fit_transform(X_Train_df)
            X_Test=tfid.transform(X_Test_df)
            with open('/opt/airflow/config/tfidvectorizer.pkl','wb') as f:
                pickle.dump(tfid,f)
                print('dumped the data successfully in config folder')
            return X_Train,X_Test,Y_Train,Y_Test
        except Exception as e:
            logging.error(f'Errinng in cleaning the data from DataFrame {e}')
            raise e
    
    def clense_production_data(self,text:str):
        lower_text=text.lower()
        cleaned_text=re.sub(r'(?i)^subject:\s*','',lower_text)
        with open('config/tfidvectorizer.pkl','rb') as f:## docker location
            tfid=pickle.load(f)
        transformed_question=tfid.transform([cleaned_text])
        return transformed_question