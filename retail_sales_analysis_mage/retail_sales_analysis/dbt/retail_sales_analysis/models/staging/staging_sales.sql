{{
  config(
    materialized = 'view',
    )
}}

with bq_sales as (
    select 
        product_id,
        store_id,
        date,
        coalesce(sales, 0) as sales,
        coalesce(revenue, 0) as revenue,
        coalesce(stock, 0) as stock,
        coalesce(price, 0) as price,
        year,
        month,
        day

    from {{ source('staging', 'raw_sales')}}
)

select * from bq_sales
  