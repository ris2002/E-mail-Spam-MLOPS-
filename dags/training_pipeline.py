'''from airflow.decorators import dag, task
import logging
from steps.ingest_data import ingest_data
@dag(dag_id='ml_pipeline',
         schedule_interval='@once')
def training_pipeline():
    csv_path = "/Users/rishilboddula/Desktop/MLOPS/E-mail-Spam-MLOPS-/dataset/emails.csv"
    df=ingest_data(csv_path)
    return df
pipeline=training_pipeline()'''

from airflow.decorators import dag, task
from steps.ingest_data import ingest_data  # your existing function
import pandas as pd
import logging

@dag(dag_id='ml_pipeline', schedule='@once')
def training_pipeline():

    

    csv_path = "/opt/airflow/dataset/emails.csv"
    df = ingest_data(csv_path) 


pipeline = training_pipeline()#running the pipeline
