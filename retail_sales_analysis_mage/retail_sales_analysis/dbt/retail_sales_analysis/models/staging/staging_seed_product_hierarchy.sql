{{
  config(
    materialized = 'view',
    )
}}

with source as (
      select * from {{ source('staging', 'seed_product_hierarchy') }}
),
bq_sales_product as (
    select
        product_id,
        product_length,
        product_depth,
        product_width,
        product_length * product_depth * product_width as product_volume,
        cluster_id,

    from source
)
select * from bq_sales_product
  