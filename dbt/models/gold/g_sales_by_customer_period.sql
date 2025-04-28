{{ 
    config(
        materialized='incremental',
        unique_key='sk_customer || sale_year || sale_month',
        schema='03_GOLD',
        alias='g_sales_by_customer_period'
    ) 
}}

SELECT 
    sk_customer,
    customer_name,
    sale_year,
    sale_month,
    SUM(sales_value) AS total_sales,
    SUM(quantity) AS total_quantity
FROM 
    {{ ref('s_fact_sales') }}
{% if is_incremental() %}
WHERE 
    (sk_customer, sale_year, sale_month) NOT IN (SELECT sk_customer, sale_year, sale_month FROM {{ this }})
{% endif %}
GROUP BY 
    sk_customer, customer_name, sale_year, sale_month