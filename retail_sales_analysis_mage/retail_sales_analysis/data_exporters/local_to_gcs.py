import os
from typing import Dict

from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.google_cloud_storage import GoogleCloudStorage

from retail_sales_analysis.utils.data_config import GCS_BUCKET_NAME, SAVE_DIR

if "data_exporter" not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_google_cloud_storage(**kwargs) -> None:
    """
    Template for exporting data to a Google Cloud Storage bucket.
    Specify your configuration settings in 'io_config.yaml'.

    Docs: https://docs.mage.ai/design/data-loading#googlecloudstorage
    """

    # Retrieve the file paths of all CSV files in the SAVE_DIR directory
    all_csv_files: Dict[str, str] = {}
    for root, _, files in os.walk(SAVE_DIR):
        for csv in files:
            filename = csv.split(".")[0]
            csv_path = os.path.join(root, csv)
            all_csv_files[filename] = csv_path

    config_path = os.path.join(get_repo_path(), "io_config.yaml")
    config_profile = "default"

    bucket_name = GCS_BUCKET_NAME

    # Export each CSV file to the specified Google Cloud Storage bucket
    for csv_name, csv_path in all_csv_files.items():
        object_key = f"raw/{csv_name}"

        GoogleCloudStorage.with_config(
            ConfigFileLoader(config_path, config_profile)
        ).export(
            csv_path,
            bucket_name,
            object_key,
        )
