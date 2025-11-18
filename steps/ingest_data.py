import logging
from airflow.decorators import task
import pandas as pd

@task
def ingest_data(csv_path)->pd.DataFrame:
    try:
        df=pd.read_csv(csv_path)
        return df
    except Exception as e:
        logging.error(f'Error when coverrting scv file to dataframe{e}')
        raise e

