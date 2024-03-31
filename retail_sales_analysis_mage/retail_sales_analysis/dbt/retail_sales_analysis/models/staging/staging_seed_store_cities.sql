{{
  config(
    materialized = 'view',
    )
}}

with source as (
      select * from {{ source('staging', 'seed_store_cities') }}
),
bq_cities as (
    select
        {{ adapter.quote("store_id") }},
        {{ adapter.quote("storetype_id") }},
        {{ adapter.quote("store_size") }},
        {{ adapter.quote("city_id") }}

    from source
)
select * from bq_cities
  