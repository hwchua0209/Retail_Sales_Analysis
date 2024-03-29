import os
from typing import List
from google.cloud import bigquery
from google.cloud.exceptions import NotFound
from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigKey, ConfigFileLoader


def get_gcp_creds() -> None:
    """
    Retrieves the Google Cloud Platform (GCP) credentials from a configuration file
    and sets the GOOGLE_APPLICATION_CREDENTIALS environment variable to the path of the GCP key file.
    """
    # Construct the path to the configuration file
    config_path = os.path.join(get_repo_path(), "io_config.yaml")
    config_profile = "default"

    # Create a ConfigFileLoader object using the configuration file path and a profile name "default"
    config = ConfigFileLoader(config_path, config_profile)

    # Retrieve the GCP key file path from the configuration
    gcp_key = config[ConfigKey.GOOGLE_SERVICE_ACC_KEY_FILEPATH]

    # Set the GOOGLE_APPLICATION_CREDENTIALS environment variable to the GCP key file path
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = gcp_key


def delete_gbq_table(table_id: str) -> None:
    """
    Deletes a table in Google BigQuery.

    Args:
        table_id (str): The ID of the table to be deleted.

    Returns:
        None
    """
    # Retrieve the GCP credentials and set the GOOGLE_APPLICATION_CREDENTIALS environment variable
    get_gcp_creds()

    client = bigquery.Client()

    # Delete the specified table
    client.delete_table(table_id, not_found_ok=True)  # Make an API request

    # Print a message indicating the table has been deleted
    print(f"Deleted table '{table_id}'.")


def check_table_exist(table_id: str) -> bool:
    """
    Checks if a table exists in Google BigQuery.

    Args:
        table_id (str): The ID of the table to check.

    Returns:
        None:
    """
    # Retrieve the GCP credentials and set the GOOGLE_APPLICATION_CREDENTIALS environment variable
    get_gcp_creds()

    client = bigquery.Client()

    try:
        client.get_table(table_id)  # Make an API request.
        print(f"Table {table_id} already exists.")
        return True
    except NotFound:
        print(f"Table {table_id} is not found.")
        return False


def create_partitioned_table(table_id: str, schema: List[bigquery.SchemaField]) -> None:
    """
    Create a partitioned table in Google BigQuery.

    Args:
        table_id (str): The ID of the table to be created.
        schema (List[bigquery.SchemaField]): The schema of the table.

    Returns:
        None
    """
    # Retrieve the GCP credentials and set the GOOGLE_APPLICATION_CREDENTIALS environment variable
    get_gcp_creds()

    client = bigquery.Client()
    table = bigquery.Table(table_id, schema=schema)

    table.time_partitioning = bigquery.TimePartitioning(
        type_=bigquery.TimePartitioningType.YEAR,
        field="date",  # name of column to use for partitioning
    )

    table = client.create_table(table)

    print(
        f"Created table {table.project}.{table.dataset_id}.{table.table_id}, "
        f"partitioned on column {table.time_partitioning.field}."
    )


def load_data_to_partitioned_table(
    table_id: str, schema: List[bigquery.SchemaField], uri: List[str]
) -> None:
    """
    Loads data from a URI into a partitioned table in BigQuery.

    Args:
        table_id (str): The ID of the table to load the data into.
        schema (List[bigquery.SchemaField]): The schema of the data being loaded.
        uri (str): The URI of the data to load.

    Returns:
        None

    Raises:
        google.api_core.exceptions.GoogleAPIError: If an error occurs while loading the data.
    """
    client = bigquery.Client()

    job_config = bigquery.LoadJobConfig(
        schema=schema,
        time_partitioning=bigquery.TimePartitioning(
            type_=bigquery.TimePartitioningType.YEAR,
            field="date",  # Name of the column to use for partitioning.
        ),
        source_format="PARQUET",
    )

    load_job = client.load_table_from_uri(
        uri, table_id, job_config=job_config
    )  # Make an API request.

    load_job.result()  # Wait for the job to complete.

    table = client.get_table(table_id)
    print(f"Loaded {table.num_rows} rows to table {table_id}")
