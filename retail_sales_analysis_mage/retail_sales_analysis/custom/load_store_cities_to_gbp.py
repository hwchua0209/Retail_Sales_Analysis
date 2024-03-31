from google.cloud import bigquery

from retail_sales_analysis.utils.gcp_helper import (
    check_table_exist,
    delete_gbq_table,
    create_unpartitioned_table,
    load_data_to_unpartitioned_table,
)

if "custom" not in globals():
    from mage_ai.data_preparation.decorators import custom


@custom
def load_store_cities_to_gbq(*args, **kwargs) -> None:
    """
    args: The output from any upstream parent blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """

    project_id = "plucky-spirit-412403"
    dataset_id = "sales_analysis"
    table_name = "seed_store_cities"

    table_id = f"{project_id}.{dataset_id}.{table_name}"

    table_schema = [
        bigquery.SchemaField("int64_field_0", "INTEGER"),
        # Added to address issue describe here
        # https://medium.com/@sylvia.sc/gcp-bigquery-csv-table-encountered-too-many-errors-giving-up-33cbba3ea670
        bigquery.SchemaField("store_id", "STRING"),
        bigquery.SchemaField("storetype_id", "STRING"),
        bigquery.SchemaField("store_size", "INTEGER"),
        bigquery.SchemaField("city_id", "STRING"),
    ]
    source_uris = ["gs://plucky-spirit-412403-sales-bucket/processed/store_cities"]
    table_exist = check_table_exist(table_id)

    if table_exist:
        delete_gbq_table(table_id)
        create_unpartitioned_table(
            table_id=table_id, schema=table_schema, uri=source_uris
        )
        load_data_to_unpartitioned_table(
            table_id=table_id, schema=table_schema, uri=source_uris
        )
    else:
        create_unpartitioned_table(
            table_id=table_id, schema=table_schema, uri=source_uris
        )
        load_data_to_unpartitioned_table(
            table_id=table_id, schema=table_schema, uri=source_uris
        )
