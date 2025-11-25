from src.cleaning_data import PreProcessStrategy
import logging
from fastapi import FastAPI
import mlflow
from pydantic import BaseModel
app=FastAPI()
cleaning_strategies= PreProcessStrategy()

# http://e-mail-spam-mlops--mlflow-server-1:5050' e-mail-spam-mlops-- is my local docker container name instaed use below service name
mlflow.set_tracking_uri("http://host.docker.internal:5050")#make sure that app is running locally
mlflow.set_experiment('email_spam_detection')
model_gradient_boosting=mlflow.pyfunc.load_model('models:/Production_Gradient_Boost_Model/1')


class TextInput(BaseModel):
    text:str

@app.post('/predict_ada_model')
def predict_ada_model(input_text: TextInput):
   try:
       txt=cleaning_strategies.clense_production_data(input_text.text)
       prediction=model_gradient_boosting.predict(txt)
       logging.info('Prediction Done')
       return{"prediction": prediction.tolist()}
   except Exception as e:
       logging.error(F'Error predicting gb_model:{e}')
       raise e

@app.post('/predict_gb_model')
def predict_gb_model(input_text: TextInput):
    try:
       txt=cleaning_strategies.clense_production_data(input_text.text)
       prediction=model_gradient_boosting.predict(txt)
       logging.info('Prediction Done')
       return{"prediction": prediction.tolist()}
    except Exception as e:
       logging.error(F'Error predicting gb_model:{e}')
       raise e



