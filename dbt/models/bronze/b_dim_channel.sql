{{
    config(
        materialized='incremental',
        unique_key='sk_channel',
        schema='01_BRONZE',
        alias='b_dim_channel'
    )
}}

select 
    id_channel,
    sk_channel,
    name,
    region,
    insertion_timestamp
from {{ source('lakehouse', 'stg_dim_channel') }}

{% if is_incremental() %}
    where insertion_timestamp > (select max(insertion_timestamp) from {{ this }})
{% endif %} 