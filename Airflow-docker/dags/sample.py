from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator

from utils import weather_api_extract

default_args = {
    'owner': 'victor_project',
    'retries': 2
}

new = DAG(
    dag_id="full_job",
    description="Fetching the data from the weather API",
    schedule="@daily",
    start_date=datetime(2025, 6, 12),
    catchup=False,
    default_args=default_args
)

task1 = PythonOperator(
    dag=new,
    python_callable=weather_api_extract,
    task_id="task1"
)

task1
