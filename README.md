# E-mail-Spam-MLOPS
This is my 3rd MLOPs project. I am taking ref from my 2nd one (https://github.com/ris2002/Sentiment-Analysis-MLOPS.git). In the second one I have done the mlops using zenml,traning has been done using Logistic Regression and deployment has been done using Fast api.
What improvements and what learning I am going to do over the 2nd one in this current project-␣␣
* Usage of Airflow
* Using kubernetes
* Zenml had inbuilt mlflow so I am going to use mlflow seperately
* Learning and using 4 boosting classification models-␣␣
1]AdaBoost␣␣
2]Gradient Boosting␣␣
3]XGB␣␣
4]Cat Boosting␣␣
* I am going to run more tha one models in same pipeline

And this will be the another revison of how mlops works
## Errors encountered while setting and runing up AirFlow
1]Module not found error-Had a hard time figuring out how to import a function from another folder to thhe dags folder␣␣

A] While creating airflow we need to follow the following steps␣␣
* curl -LfO 'https://airflow.apache.org/docs/apache-airflow/stable/docker-compose.yaml'< br / >
The above command creates a docker-compose yaml file
* mkdir -p ./dags ./logs ./plugins'␣␣
The above folder creates the our wantd main files
* docker compose up airflow-init␣␣
This initiates the airflow db

* docker compose up␣␣
This command runs airflow in the docker 

␣␣
␣␣

It is convinet to create all the required folders in 'mkdir -p ./dags ./logs ./plugins' as the python paths and thhe mounting of those folders would be already be automatically be done in docker-compose yaml file. If you need to use a script from an unmounted folder, first go to docker-compose yaml file, go to volumes path and place the ␣␣<ins>__cmd(- ${AIRFLOW_PROJ_DIR:-.}/'folder_name':/opt/airflow/'folder_name':z )__</ins> ␣␣
then go to environments path and place cmd 
␣␣  <ins>__cmd(PYTHONPATH: /opt/airflow/'folder_name')__</ins> ␣␣

This has to be done so that the docker can identify the path of the unmounted folder.␣␣

< br / >  <ins>__(It is important to note that since we have mounted the folders the root folder for all python scripts remain the same irrespective of which folders they are present locally so if you want to import a func directly write 'from script_name import function' instead of directly writig the local path of it )__</ins> < br / >




---------

## Some more errors encoutered while using Airflow
* Unpacking XComArgs outside tasks
Scenario:
df = ingest_data(csv_path)                  # returns XComArg
X_Train, X_Test, Y_Train, Y_Test = vectorized_and_split_data(df)  # ❌

Error:
TypeError: 'XComArg' object is not iterable

Cause:

@task decorated functions return XComArg references, not the actual data.

You cannot unpack or iterate over an XComArg in the DAG definition.

Fix:

Wrap multiple outputs in a dict or tuple inside the task.

Access via split["X_Train"] or split[0] in downstream tasks.

* Returning objects not serializable by XCom
Scenario:
@task
def vectorized_and_split_data(df):
    X_Train, X_Test, Y_Train, Y_Test = processor.vectorize_train_and_split(df)
    return X_Train, X_Test, Y_Train, Y_Test

X_Train and X_Test are scipy sparse matrices.
Error:
TypeError: cannot serialize object of type <class 'scipy.sparse._csr.csr_matrix'>
Cause:
Airflow tries to push the returned object to XCom.
XCom cannot serialize large objects like sparse matrices, big DataFrames, or ML models.
Fix:
Do not return large objects via XCom.
Save them to disk or cloud storage and return only file paths in XCom.
* I have used a task in my dag which contains other tasks
what happened is I am not able to track the other tasks within that task
* Var when given in dag fuction gets converted to Xcom
Better to import the dataset inside the dag funnc instead of giving the dataset instead of declaring  it as a var in dag func.

* It is important to note that I was able to run the dag with installing requirements.txt from docker as basic modules like sklearn,pandas and numpy are already pre installed in the airflow so when I ran dag previously I didnot need to installl them . However I faced error whhen I started using mlflow. So the safe thing I thought was use thee docker to innstall all requirements.txt ffile.
there are also some changes sto be done in thhe docker compose file, in x-airflow-common: section I need to comment out the image and un comment out the 'build: .'  after that build thee docker-compose file and restar it



----------
## Data Cleaning


---------
## Project Structure (Need To Complete)







