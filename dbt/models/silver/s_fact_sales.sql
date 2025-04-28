{{
    config(
        materialized='incremental',
        unique_key='sk_product || sk_customer || sk_channel || sk_date',
        schema='02_SILVER',
        alias='s_fact_sales'
    )
}}

select 
    f.sk_product,
    f.sk_customer,
    f.sk_channel,
    f.sk_date,
    f.quantity,
    f.sales_value,
    p.name as product_name,
    p.category as product_category,
    c.name as customer_name,
    c.type as customer_type,
    c.city as customer_city,
    c.state as customer_state,
    c.country as customer_country,
    ch.name as channel_name,
    ch.region as channel_region,
    d.full_date as sale_date,
    d.day as sale_day,
    d.month as sale_month,
    d.year as sale_year,
    f.insertion_timestamp
from {{ ref('b_fact_sales') }} f
left join {{ ref('b_dim_product') }} p on f.sk_product = p.sk_product
left join {{ ref('b_dim_customer') }} c on f.sk_customer = c.sk_customer
left join {{ ref('b_dim_channel') }} ch on f.sk_channel = ch.sk_channel
left join {{ source('lakehouse', 'stg_dim_date') }} d on f.sk_date = d.sk_date

{% if is_incremental() %}
    where f.insertion_timestamp > (select max(insertion_timestamp) from {{ this }})
{% endif %} 