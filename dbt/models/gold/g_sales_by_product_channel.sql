{{ 
    config(
        materialized='incremental',
        unique_key='sk_product || sk_channel',
        schema='03_GOLD',
        alias='g_sales_by_product_channel'
    ) 
}}

SELECT 
    sk_product,
    sk_channel,
    product_name,
    channel_name,
    SUM(sales_value) AS total_sales,
    SUM(quantity) AS total_quantity
FROM 
    {{ ref('s_fact_sales') }}
    
{% if is_incremental() %}
WHERE 
    (sk_product, sk_channel) NOT IN (SELECT sk_product, sk_channel FROM {{ this }})
{% endif %}
GROUP BY 
    sk_product, sk_channel, product_name, channel_name