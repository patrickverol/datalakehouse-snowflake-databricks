{{
    config(
        materialized='incremental',
        unique_key='sk_customer',
        schema='01_BRONZE',
        alias='b_dim_customer'
    )
}}

select 
    id_customer,
    sk_customer,
    name,
    type,
    city,
    state,
    country,
    insertion_timestamp
from {{ source('lakehouse', 'stg_dim_customer') }}

{% if is_incremental() %}
    where insertion_timestamp > (select max(insertion_timestamp) from {{ this }})
{% endif %} 