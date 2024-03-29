from google.cloud import bigquery

from retail_sales_analysis.utils.gcp_helper import (
    check_table_exist,
    delete_gbq_table,
    create_partitioned_table,
    load_data_to_partitioned_table,
)

if "custom" not in globals():
    from mage_ai.data_preparation.decorators import custom


@custom
def load_sales_parquet_to_gbq(*args, **kwargs) -> None:
    """
    args: The output from any upstream parent blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """

    project_id = "plucky-spirit-412403"
    dataset_id = "sales_analysis"
    table_name = "sales"

    table_id = f"{project_id}.{dataset_id}.{table_name}"

    table_schema = [
        bigquery.SchemaField("product_id", "STRING"),
        bigquery.SchemaField("store_id", "STRING"),
        bigquery.SchemaField("date", "DATE"),
        bigquery.SchemaField("sales", "INTEGER"),
        bigquery.SchemaField("revenue", "FLOAT"),
        bigquery.SchemaField("stock", "INTEGER"),
        bigquery.SchemaField("price", "FLOAT"),
        bigquery.SchemaField("year", "INTEGER"),
        bigquery.SchemaField("month", "INTEGER"),
        bigquery.SchemaField("day", "INTEGER"),
    ]
    source_uris = ["gs://plucky-spirit-412403-sales-bucket/processed/sales/*.parquet"]
    table_exist = check_table_exist(table_id)

    if table_exist:
        delete_gbq_table(table_id)
        create_partitioned_table(table_id=table_id, schema=table_schema)
        load_data_to_partitioned_table(
            table_id=table_id, schema=table_schema, uri=source_uris
        )
    else:
        create_partitioned_table(table_id=table_id, schema=table_schema)
        load_data_to_partitioned_table(
            table_id=table_id, schema=table_schema, uri=source_uris
        )
