# dbt_models_dag.py
from airflow import DAG
from datetime import datetime
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
}

with DAG('07_dbt_databricks_dag', 
         default_args=default_args, 
         schedule_interval='@daily',
         catchup=False) as dag:

    start = EmptyOperator(task_id='start')
    end = EmptyOperator(task_id='end')

    # Task to run DBT models in the Airflow container
    run_dbt_databricks = BashOperator(
        task_id='run_dbt_databricks',
        bash_command='cd /opt/airflow/dbt/databricks_datalakehouse && dbt run'
    )

    start >> run_dbt_databricks >> end
    