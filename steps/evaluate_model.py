from airflow.decorators import dag, task
import mlflow
import mlflow.sklearn
import logging
import pickle
from model_data_evaluation import Evaluation_Techniques


@task
def evaluate_model():
    #/opt/airflow/config/ada_trained_model.pkl
    #/opt/airflow/config/gb_trained_model.pkl
    #client = mlflow.tracking.MlflowClient()
   # experiment = client.get_experiment_by_name(experiment_name)
   # if experiment is None:
   #     client.create_experiment(experiment_name)

    mlflow.set_tracking_uri('http://e-mail-spam-mlops--mlflow-server-1:5050')
    mlflow.set_experiment("email_spam_detection")
    try:
        with open('/opt/airflow/config/ada_trained_model.pkl','rb') as f:
            ada_model=pickle.load(f)
        with open('/opt/airflow/config/gb_trained_model.pkl','rb') as f:
            gb_model=pickle.load(f)
        with open('/opt/airflow/config/x_test.pkl','rb') as f:
            x_test=pickle.load(f)
        with open('/opt/airflow/config/y_test.pkl','rb') as f:
            y_test=pickle.load(f)

        ada_y_pred_model=ada_model.predict(x_test)
        gb_y_pred_model=gb_model.predict(x_test)

        Evaluation=Evaluation_Techniques()
        acc_score_ada_model=Evaluation.accuracy_score_function(ada_y_pred_model,y_test)
        acc_score_gb_model=Evaluation.accuracy_score_function(gb_y_pred_model,y_test)
        ada_TN,ada_TP,ada_FN,ada_FP=Evaluation.confusion_matrix_function(ada_y_pred_model,y_test)
        gb_TN,gb_TP,gb_FN,gb_FP=Evaluation.confusion_matrix_function(gb_y_pred_model,y_test)





        with mlflow.start_run(run_name='gb_boosting_model') as run:
            mlflow.log_metric('accuracy_score:',acc_score_gb_model)
            mlflow.log_metric('True Negative',gb_TN)
            mlflow.log_metric('True Positive',gb_TP)
            mlflow.log_metric('False Negative',gb_FN)
            mlflow.log_metric('False Positive',gb_FP)
        
        with mlflow.start_run(run_name='ada_boosting_model') as run:
            mlflow.log_metric('accuracy_score:',acc_score_ada_model)
            mlflow.log_metric('True Negative',ada_TN)
            mlflow.log_metric('True Positive',ada_TP)
            mlflow.log_metric('False Negative',ada_FN)
            mlflow.log_metric('False Positive',ada_FP)




        pass
    except Exception as e:
        logging.error(f'Error logging the predicted model {e}')
        raise e