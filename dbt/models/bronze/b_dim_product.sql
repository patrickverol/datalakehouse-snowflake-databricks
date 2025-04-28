{{
    config(
        materialized='incremental',
        unique_key='sk_product',
        schema='01_BRONZE',
        alias='b_dim_product'
    )
}}

select 
    id_product,
    sk_product,
    name,
    category,
    insertion_timestamp
from {{ source('lakehouse', 'stg_dim_product') }}

{% if is_incremental() %}
    where insertion_timestamp > (select max(insertion_timestamp) from {{ this }})
{% endif %} 