from ingest_data import ingest_data
from clean_data import vectorized_and_split_data
from airflow.decorators import dag, task
from train_model import model_training
from evaluate_model import evaluate_model

import logging

@dag(dag_id='dag_train_pipeline', schedule='@once')
def run_train_pipeline():
    csv_path = "/opt/airflow/dataset/emails.csv"
    
    task_ingest=ingest_data(csv_path)
    task_vectorize_and_split=vectorized_and_split_data(task_ingest)
    logging.info('Successful Splitting of data')
    task_model_train= model_training()
    logging.info('Successful training of models')
    task_model_evaluate=evaluate_model()
    logging.info('Successful evaluation of models')
    task_ingest>>task_vectorize_and_split>>task_model_train>>task_model_evaluate




pipeline = run_train_pipeline()
