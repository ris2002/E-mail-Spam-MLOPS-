import logging
import numpy as np
import pandas as pd
from model_initiation_training import   Gradient_Boosting_Class,ADA_Boosting_Class
from airflow.decorators import dag, task
import mlflow
import pickle
from sklearn.base import ClassifierMixin
from typing_extensions import Annotated
from typing import Tuple
import mlflow.sklearn #important to import this
import json
@task
def model_training():
    #client = mlflow.tracking.MlflowClient()
   # experiment = client.get_experiment_by_name(experiment_name)
   # if experiment is None:
    #    client.create_experiment(experiment_name)

    config_path='/opt/airflow/config/config.json'
    with open(config_path,'r') as f:
        config=json.load(f)
    mlflow.set_tracking_uri('http://e-mail-spam-mlops--mlflow-server-1:5050')
    mlflow.set_experiment("email_spam_detection")
    try:
        with open('/opt/airflow/config/x_train.pkl','rb') as f:
            x_train=pickle.load(f)
            logging.info('Loaded x_train valuses')
        with open('/opt/airflow/config/y_train.pkl','rb') as f:
            y_train=pickle.load(f)
            logging.info('Loaded y_train valuses')
        ada_boost_model=ADA_Boosting_Class()
        gb_boost_model=Gradient_Boosting_Class()
        trained_ada_boost_model=ada_boost_model.fitting_the_model(x_train,y_train,**config['ada_boost'])
        trained_gb_model=gb_boost_model.fitting_the_model(x_train,y_train,**config['gradient_boost'])
        with open('/opt/airflow/config/ada_boost_trained_model.pkl','wb') as f:
            pickle.dump(trained_ada_boost_model,f)
        with open('/opt/airflow/config/gb_boost_trained_model.pkl','wb') as f:
            pickle.dump(trained_gb_model,f)
    
        
        with mlflow.start_run(run_name='ada_boosting_model') as run:
            mlflow.sklearn.log_model(sk_model=trained_ada_boost_model,artifact_path='ada_boost')
            run_id=run.info.run_id
            mlflow.register_model(
            model_uri=f'runs:/{run_id}/ada_boost',
            name='ada_boost_model' )
        

        with mlflow.start_run(run_name='gb_boosting_model') as run:
            mlflow.sklearn.log_model(sk_model= trained_gb_model,artifact_path='gb_boost')
            run_id=run.info.run_id
            mlflow.register_model(
            model_uri=f'runs:/{run_id}/gb_boost',
            name='GB_boost_model')

        logging.info('SUCCCESSFULLY TRAINED AND REGISTERED THE MODEL')


        

            
    

        

    except Exception as e:
        logging.error(f'Error training the model:::{e}')
        raise e