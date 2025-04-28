from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
}

with DAG('02_insert_dim_date_dag',
         default_args=default_args,
         schedule_interval='@once',
         catchup=False) as dag:

    install_requirements = BashOperator(
        task_id='install_requirements',
        bash_command='python -m pip install --upgrade pip && pip install -r /opt/airflow/dags/scripts/requirements.txt',  # Path to requirements.txt
    )

    insert_dim_date = BashOperator(
        task_id='insert_dim_date',
        bash_command='python /opt/airflow/dags/scripts/insert_dim_date.py',  # Path to your script
    )

    install_requirements >> insert_dim_date  # Ensure requirements are installed before running the script