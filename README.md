# E-mail-Spam-MLOPS
This is my 3rd MLOPs project. I am taking ref from my 2nd one (https://github.com/ris2002/Sentiment-Analysis-MLOPS.git). In the second one I have done the mlops using zenml,traning has been done using Logistic Regression and deployment has been done using Fast api.
What improvements and what learning I am going to do over the 2nd one in this current project-< br / >
* Usage of Airflow
* Using kubernetes
* Zenml had inbuilt mlflow so I am going to use mlflow seperately
* Learning and using 4 boosting classification models-< br / >
1]AdaBoost< br / >
2]Gradient Boosting< br / >
3]XGB< br / >
4]Cat Boosting< br / >
And this will be the another revison of how mlops works
## Errors encountered while setting and runing up AirFlow
1]Module not found error-Had a hard time figuring out how to import a function from another folder to thhe dags folder< br / >< br / >

A] While creating airflow we need to follow the following steps< br / >
* curl -LfO 'https://airflow.apache.org/docs/apache-airflow/stable/docker-compose.yaml'< br / >
The above command creates a docker-compose yaml file
* mkdir -p ./dags ./logs ./plugins'< br / >
The above folder creates the our wantd main files
* docker compose up airflow-init< br / >
This initiates the airflow db

* docker compose up< br / >
This command runs airflow in the docker 

< br / >

It is convinet to create all the required folders in 'mkdir -p ./dags ./logs ./plugins' as the python paths and thhe mounting of those folders would be already be automatically be done in docker-compose yaml file. If you need to use a script from an unmounted folder, first go to docker-compose yaml file, go to volumes path and place the 
< br / >  <ins>__cmd(- ${AIRFLOW_PROJ_DIR:-.}/'folder_name':/opt/airflow/'folder_name':z )__</ins> < br / >
then go to environments path and place cmd < br / >  <ins>__cmd(PYTHONPATH: /opt/airflow/'folder_name')__</ins> < br / >
This has to be done so that the docker can identify the path of the unmounted folder.< br / >

< br / >  <ins>__(It is important to note that since we have mounted the folders the root folder for all python scripts remain the same irrespective of which folders they are present locally so if you want to import a func directly write 'from script_name import function' instead of directly writig the local path of it )__</ins> < br / >



---------
## Data Cleaning


---------
## Project Structure (Need To Complete)







