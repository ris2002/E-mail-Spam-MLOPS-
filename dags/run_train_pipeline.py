from ingest_data import ingest_data
from clean_data import vectorized_and_split_data
from airflow.decorators import dag, task

import logging

@dag(dag_id='ml_train_pipeline', schedule='@once')
def run_train_pipeline():
    csv_path = "/opt/airflow/dataset/emails.csv"
    
    df=ingest_data(csv_path)
    vectorized_and_split_data(df)
    logging.info('Successful Training')


pipeline = run_train_pipeline()
