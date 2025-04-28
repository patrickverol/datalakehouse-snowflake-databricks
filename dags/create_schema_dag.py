from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from datetime import datetime

# Define the default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
}

# Create the DAG
with DAG(
    '01_create_schema_dag',
    default_args=default_args,
    description='A simple DAG to create PostgreSQL schema',
    schedule_interval='@once',  # Run once
) as dag:

    # Task to create the schema
    create_schema = PostgresOperator(
        task_id='create_schema',
        postgres_conn_id='postgres_connection_id',  # Use the connection ID you set up in Airflow
        sql='scripts/create_schema.sql',  # Path to your SQL file in the container
    )

    create_schema