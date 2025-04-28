from airflow import DAG
from airflow.providers.airbyte.operators.airbyte import AirbyteTriggerSyncOperator
from airflow.providers.airbyte.sensors.airbyte import AirbyteJobSensor
from datetime import datetime
from airflow.models import Variable

# Get the Airbyte connection ID from Airflow variables
airbyte_postgres_to_databricks_connection_id = Variable.get("airbyte_postgres_to_databricks_connection_id")

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
}

with DAG('06_airbyte_source_to_databricks_dag',
         default_args=default_args,
         schedule_interval='@daily',
         catchup=False) as dag:

    # Task to trigger the Airbyte sync
    trigger_airbyte_sync = AirbyteTriggerSyncOperator(
        task_id='airbyte_trigger_sync',
        airbyte_conn_id='airbyte_connection_id',  # Your Airbyte connection ID in Airflow
        connection_id=airbyte_postgres_to_databricks_connection_id,
        asynchronous=True
    )

    # Task to wait for the sync to complete
    wait_for_sync_completion = AirbyteJobSensor(
        task_id='airbyte_check_sync',
        airbyte_conn_id='airbyte_connection_id',  # Your Airbyte connection ID in Airflow
        airbyte_job_id=trigger_airbyte_sync.output  # Use the output from the trigger task
    )

    # Set task dependencies
    trigger_airbyte_sync >> wait_for_sync_completion  # Ensure the sync is triggered before checking its completion