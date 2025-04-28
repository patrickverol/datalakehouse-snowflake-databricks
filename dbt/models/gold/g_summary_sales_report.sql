{{ 
    config(
        materialized='incremental',
        unique_key='sk_product || sale_year',
        schema='03_GOLD',
        alias='g_summary_sales_report'
    ) 
}}

SELECT 
    sk_product,
    product_name,
    sale_year,
    SUM(sales_value) AS total_sales,
    SUM(quantity) AS total_quantity
FROM 
    {{ ref('s_fact_sales') }}
{% if is_incremental() %}
WHERE 
    (sk_product, sale_year) NOT IN (SELECT sk_product, sale_year FROM {{ this }})
{% endif %}
GROUP BY 
    sk_product, product_name, sale_year
ORDER BY 
    sale_year, product_name