{{
    config(
        materialized='incremental',
        unique_key='sk_product || sk_customer || sk_channel || sk_date',
        schema='01_BRONZE',
        alias='b_fact_sales'
    )
}}

select 
    sk_product,
    sk_customer,
    sk_channel,
    sk_date,
    quantity,
    sales_value,
    insertion_timestamp
from {{ source('lakehouse', 'stg_fact_sales') }}

{% if is_incremental() %}
    where insertion_timestamp > (select max(insertion_timestamp) from {{ this }})
{% endif %} 