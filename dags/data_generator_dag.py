from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
}

with DAG('03_data_generator_dag',
         default_args=default_args,
         schedule_interval='@daily',
         catchup=False) as dag:

    data_generator = BashOperator(
        task_id='data_generator',
        bash_command='python /opt/airflow/dags/scripts/data_generator.py',  # Path to your script
    )

    data_generator