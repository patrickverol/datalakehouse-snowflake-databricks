<h1 align="center">
    Datalakehouse for Snowflake or Databricks with Airbyte and DBT
</h1>

<br>
    <div align="center">
        <a><img src="https://github.com/user-attachments/assets/46a5f8b1-f047-4c6b-b8da-e3cc9a57bb7e"></a> 
    </div>
</br>

<div align="center">
    <a href = "https://www.python.org/" target="_blank"><img src="https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white" target="_blank"></a>
    <a href = "https://www.postgresql.org/docs/"><img src="https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white" target="_blank"></a>
    <a href = "https://docs.airbyte.com/"><img src="https://img.shields.io/badge/Airbyte-615EFF.svg?style=for-the-badge&logo=Airbyte&logoColor=white" target="_blank"></a>
    <a href = "https://docs.getdbt.com/docs/build/documentation"><img src="https://img.shields.io/badge/dbt-FF694B?style=for-the-badge&logo=dbt&logoColor=white" target="_blank"></a>
    <a href = "https://docs.docker.com/"><img src="https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white" target="_blank"></a>
    <a href = "https://docs.databricks.com/aws/en/"><img src="https://img.shields.io/badge/Databricks-FF3621?style=for-the-badge&logo=Databricks&logoColor=white" target="_blank"></a>
    <a href = "https://docs.snowflake.com/"><img src="https://img.shields.io/badge/Snowflake-29B5E8.svg?style=for-the-badge&logo=Snowflake&logoColor=white" target="_blank"></a>
</div> 

## About the project

In this project, I develop a data lakehouse on the Snowflake and Databricks platforms, performing data transformations with DBT and using Airbyte for data loading.

The entire environment is managed with Docker, ensuring environment isolation and version control.

Airbyte is one of the most widely used open-source tools for data movement. In this project, the data is moved from a Postgres database to Snowflake or Databricks, but several data sources can be connected through the Airbyte UI.

Likewise, DBT is one of the most widely used open-source tools for data transformation. In this project, DBT is used to build the bronze, silver, and gold layers in Snowflake or Databricks.

With this approach, the benefits of the best open-source data tools are taken advantage of, as well as the benefits of the best data platforms.

In addition, this project addresses the main step in building a data lakehouse: data modeling. A fictitious company and a business problem to be solved are defined. From this business problem, data modeling is performed to solve the problem, where the conceptual, dimensional, logical and physical models are defined to build the data lakehouse and solve the proposed problem based on data.

If you want to understand the modeling part, go to the modeling folder, where the entire resolution of the business problem is developed.

## Databricks Lakehouse Schema

<br>
    <div align="center">
        <a><img src="https://github.com/user-attachments/assets/535e22a6-21b6-4cab-a7c7-95d3b369e2ed"></a> 
    </div>
</br>

## Databricks Lineage

<br>
    <div align="center">
        <a><img src="https://github.com/user-attachments/assets/94ac959d-fa2f-4f39-906e-48c335616ad8"></a> 
    </div>
</br>

## Snowflake Lakehouse Schema

<br>
    <div align="center">
        <a><img src="https://github.com/user-attachments/assets/5fd109e1-974e-4df0-97f5-69e7c34e19a0"></a> 
    </div>
</br>

## Snowflake Lineage

<br>
    <div align="center">
        <a><img src="https://github.com/user-attachments/assets/5077fe58-bd4f-4c81-b469-4c8b7aee6a29"></a> 
    </div>
</br>

---

## Installation and configuration

- **Airbyte:** data extraction - http://localhost:56174/
- **Dbt:** data transformation
- **Airflow:** task orchestration - http://localhost:8085/
- **PostgreSQL:** data storage - http://localhost:5780/

--- 

## Requirements
- Docker Desktop
- Python 3.6 or higher
- Recommended 8GB RAM or higher only for docker containers.

---

## Credentials

### Airflow
- **username:** `airflow`
- **password:** `airflow`

### Postgres
- **Name:** `db_source`
- **Host name/adress:** `localhost`
- **Port:** `5780`
- **Maintenance database:** `dbSource`
- **Username:** `useradmin`
- **password:** `password`
*Credentials to connect using pgAdmin*

### Airbyte
Enter a valid email when trying to log in.
- For other configurations:
 - **internal_host:** `host.docker.internal`
 - **internal_host_and_port:** `http://host.docker.internal:8000`
 - **user:** `airbyte`
 - **password:** `password`

---

## Setup Instructions
1. Open your terminal.
2. Navigate to the root of the `data-stack` repository
3. Run `docker compose up --build` to initialize the containers. If you want to run it in the background, add `-d` argument.
4. Make shure you have the accounts created in Databricks or Snowflake (you will need the tokens, account and password to configure Airbyte and Airflow).
5. Perform Airflow configurations (*Section below*)
6. Go to Airflow UI and run the 3 firsts DAGs to populate the data source in Postgres.
5. Perform Airbyte configurations (*Section below*)
6. Go to the airflow-worker container terminal and inicialize the dbt project (*Section below*)
8. Run all the Airflow DAGs exactly in the configured order.
9. Go to Snowflake or Databricks and see the schemas created.

---

## First Airflow Configurations
1. Open Airflow
2. Go to connections
3. Create the Postgres connection with the below configuration:
    - **Connection Id:** `postgres_connection_id`
    - **Connection Type:** `Postgres`
    - **Host:** `db_source`
    - **Schemas:** `dbSource`
    - **Login:** `useradmin`
    - **Password:** `password`
    - **Port:** `5432`
4. Create the Airbyte connection with the below configuration:
    - **Connection Id:** `airbyte_connection_id`
    - **Connection Type:** `Airbyte`
    - **Host:** `airbyte-server`
    - **Port:** `8001`

---

## Airbyte Configurations
1. Open Airbyte, enter an email and select `Get started`
2. Select sources (*left sidebar*) , in the search bar write `Postgres` and select it 
3. Create the Postgres connection for source data
    - **Source_name:** `Postgres`
    - **Host:** `host.docker.internal`
    - **Port:** `5780`
    - **Database Name:** `dbSource`
    - **Schemas:** `dw`
    - **Username:** `useradmin`
    - **Password:** `password`
    - ***Scroll until the end and select `set up source`***
4. Select Destinations (*left sidebar*), search for Snowflake and select it.
5. Create the Snowflake connection as destination (*you can find your credentials in the email that you received after create your account*)
    - **Destination_name:** `Snowflake`
    - **Host:** `<account_name>.snowflakecomputing.com`
    - **Role:** `ACCOUNTADMIN`
    - **Warehouse:** `COMPUTE_WH`
    - **Database**: `LAKEHOUSE_DB`
    - **Default Schema:** `LAKEHOUSE_SCHEMA`
    - **Username:** `<your_username>`
    - **Password:** `<your_password>`
    - ***Scroll until the end and select `set up destination`***
6. Select Destinations (*left sidebar*), search for Databricks Lakehouse and select it.
7. Create the Databricks connection as destination (*you can find your credentials in SQL Warehouses -> Connection details*)
    - **Destination_name:** `Databricks Lakehouse`
    - **Server Hostname:** `<your_server_hostname>`
    - **HTTP Path:** `<your_http_path>`
    - **Port:** `443`
    - **Access Token:** `<your_acess_token>`
    - **Databricks catalog:** `datalakehouse`
    - **Default Schema:** `LAKEHOUSE_SCHEMA`
    - ***Scroll until the end and select `set up destination`***
8. Select Connections (*left sidebar*)
9. Create the Postgres -> Snowflake connection
    - Select the `Postgres` source
    - Select `Use existing destination`
    - In the destination tab select **Snowflake** and select `Use existing destination`
    - In the new screen view, change the `Replication frequency` to `Manual`
    - Define the `Destination Stream Prefix` to `stg_`
    - Sync mode should be `Full refresh overwrite`
    - Select `set up connection`
10. Select Connections (*left sidebar*)
11. Create the Postgres -> Databricks connection
    - Select the `Postgres` source
    - Select `Use existing destination`
    - In the destination tab select **Databricks** and select `Use existing destination`
    - In the new screen view, change the `Replication frequency` to `Manual`
    - Define the `Destination Stream Prefix` to `stg_`
    - Sync mode should be `Full refresh overwrite`
    - Select `set up connection`
12. After setting up the connections, you can click on `Sync now` to move data from source to destination, but if you want Airflow to orquestrate the next loads of data, you will need to get connection id and replace into the code of the DAGs.
    - Select Connections (*left sidebar*), click on the connection you want (*Snowflake or Databricks*), get the link on http bar, it would be something like this: `http://localhost:56174/workspaces/0f607d97-c473-4bd0-8033-e10b047540e9/connections/90a7a5cd-e87a-425c-bd22-5c9da230e795/transformation`
    - Select the entire code between **connection** and **transformation**, in this example above is: `90a7a5cd-e87a-425c-bd22-5c9da230e795`
    - Paste the code in the variables that will be created in Airflow, next step.
   
---

## Second Airflow Configurations
1. Open Airflow
2. Go to variables
3. Create the airbyte_postgres_to_snowflake_connection_id with the below configuration:
    - **Key:** `airbyte_postgres_to_snowflake_connection_id`
    - **Val:** `<your_connection_id_created_in_airbyte>`
    - **Description:** `Connection_id from Postgres to Snowflake`
4. Create the airbyte_postgres_to_databricks_connection_id with the below configuration:
    - **Key:** `airbyte_postgres_to_databricks_connection_id`
    - **Val:** `<your_connection_id_created_in_airbyte>`
    - **Description:** `Connection_id from Postgres to Databricks`

---

## DBT Configurations
1. Open the terminal
2. Go to the path of your projet: `cd data-stack`
3. Go to the airflow-worker terminal: `docker compose exec airflow-worker bash`
5. If do you want to inicialize the project in Snowflake:
    - Enter a name for your project: `dbt init snowflake_datalakehouse`
    - Which database would you like to use: `snowflake`
    - Account: `<your_account>` *(You can see that in the email you recieved after created your account)*
    - Username: `<your_username>` *(You can see that in the email you recieved after created your account)*
    - Password: `<your_password>`
    - Role: `ACCOUNTADMIN`
    - Warehouse: `COMPUTE_WH`
    - Database: `LAKEHOUSE_DB`
    - Default Schema: `LAKEHOUSE_SCHEMA`
    - threads: `10` *(Change that will not make difference)*
    - Remove examples from models: `rm -r snowflake_datalakehouse/models/*`
    - Move your own models to the folder models: `cp -r models_snowflake/* snowflake_datalakehouse/models`
    - Go to the Airflow UI and run the `05_dbt_snowflake_dag`
6. If do you want to inicialize the project in Databricks:
    - Enter a name for your project: `dbt init databricks_datalakehouse`
    - Which database would you like to use: `databricks`
    - http_path: `<your_http_path>` *(You can create one in Settings -> Developer -> Manage tokens)*
    - Token: `<your_token>` *(You can create one in Settings -> Developer -> Manage tokens)*
    - Desired unity catalog option: `use Unity Catalog`
    - Catalog: `datalakehouse`
    - Schema: `lakehouse_schema`
    - threads: `10` *(Change that will not make difference)*
    - Remove examples from models: `rm -r databricks_datalakehouse/models/*`
    - Move your own models to the folder models: `cp -r models_databricks/* databricks_datalakehouse/models`
    - Go to the Airflow UI and run the `07_dbt_databricks_dag`
