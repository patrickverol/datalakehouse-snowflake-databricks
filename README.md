<h1 align="center">
    Datalakehouse for Snowflake or Databricks with Airbyte and DBT
</h1>

<br>
    <div align="center">
        <a><img src="https://github.com/user-attachments/assets/33da8c2b-0a73-444e-83aa-0624f3cb819a"></a> 
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

## Installation and configuration

- **Airbyte:** data extraction - http://localhost:56174/
- **Dbt:** data transformation
- **Airflow:** task orchestration - http://localhost:8085/
- **PostgreSQL:** data storage - http://localhost:5780/

## Use Case Explanation
We will be working with transactional data referred to loan transactions and customers from GeekBankPE (a famous bank around the world).

You have two requirements from different areas of the bank.

- The Marketing area needs to have updated customer data to be able to contact them and make offers.
- The Finance area requires to have daily loan transactions complemented with customer drivers to be able to analyze them and improve the revenue.

To fulfill with the request, we are going to perform incremental loads and also using techniques like upsert.

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
    12.1. Select Connections (*left sidebar*), click on the connection you want (*Snowflake or Databricks*), get the link on http bar, it would be something like this: `http://localhost:56174/workspaces/0f607d97-c473-4bd0-8033-e10b047540e9/connections/90a7a5cd-e87a-425c-bd22-5c9da230e795/transformation`
    12.2. Select the entire code between **connection** and **transformation**, in this example above is: `90a7a5cd-e87a-425c-bd22-5c9da230e795`
    12.3. Paste the code in the variables that will be created in Airflow, next step.
   
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
    5.1. Enter a name for your project: `dbt init snowflake_datalakehouse`
    5.2. Which database would you like to use: `snowflake`
    5.3. Account: `<your_account>` *(You can see that in the email you recieved after created your account)*
    5.4. Username: `<your_username>` *(You can see that in the email you recieved after created your account)*
    5.5. Password: `<your_password>`
    5.6. Role: `ACCOUNTADMIN`
    5.7. Warehouse: `COMPUTE_WH`
    5.8. Database: `LAKEHOUSE_DB`
    5.9. Default Schema: `LAKEHOUSE_SCHEMA`
    5.10. threads: `10` *(Change that will not make difference)*
    5.11. Remove examples from models: `rm -r snowflake_datalakehouse/models/*`
    5.12. Move your own models to the folder models: `cp -r models_snowflake/* snowflake_datalakehouse/models`
    5.13. Go to the Airflow UI and run the `05_dbt_snowflake_dag`
6. If do you want to inicialize the project in Databricks:
    6.1. Enter a name for your project: `dbt init databricks_datalakehouse`
    6.2. Which database would you like to use: `databricks`
    6.3. http_path: `<your_http_path>` *(You can create one in Settings -> Developer -> Manage tokens)*
    6.4. Token: `<your_token>` *(You can create one in Settings -> Developer -> Manage tokens)*
    6.5. Desired unity catalog option: `use Unity Catalog`
    6.6. Catalog: `datalakehouse`
    6.7. Schema: `lakehouse_schema`
    6.8. threads: `10` *(Change that will not make difference)*
    6.9. Remove examples from models: `rm -r databricks_datalakehouse/models/*`
    6.10. Move your own models to the folder models: `cp -r models_databricks/* databricks_datalakehouse/models`
    6.11. Go to the Airflow UI and run the `07_dbt_databricks_dag`
