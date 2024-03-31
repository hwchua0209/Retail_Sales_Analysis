{{
  config(
    materialized = 'table',
    )
}}

with 
sales_data as (
    select *, 
    from {{ ref('staging_sales') }}
), 

product_data as (
    select *, 
    from {{ ref('staging_seed_product_hierarchy') }}
), 

city_data as (
    select *, 
    from {{ ref('staging_seed_store_cities') }}
)

select 
    s.product_id,
    s.store_id,
    date as sales_date,
    year as sales_year,
    month as sales_month,
    day as sales_day,
    sales as sales_quantity,
    revenue as daily_revenue,
    stock,
    price as product_price,
    product_volume,
    cluster_id,
    storetype_id,
    store_size,
    city_id

from sales_data s
inner join product_data p
on s.product_id = p.product_id
inner join city_data c 
on s.store_id = c.store_id