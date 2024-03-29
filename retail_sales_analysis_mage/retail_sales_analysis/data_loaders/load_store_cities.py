import pandas as pd
from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.google_cloud_storage import GoogleCloudStorage
from os import path

from retail_sales_analysis.utils.data_config import GCS_BUCKET_NAME

if "data_loader" not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if "test" not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_from_google_cloud_storage(*args, **kwargs) -> pd.DataFrame:
    """
    Template for loading data from a Google Cloud Storage bucket.
    Specify your configuration settings in 'io_config.yaml'.

    Docs: https://docs.mage.ai/design/data-loading#googlecloudstorage
    """
    config_path = path.join(get_repo_path(), "io_config.yaml")
    config_profile = "default"

    bucket_name = GCS_BUCKET_NAME
    object_key = "raw/store_cities"

    # Set schema
    dtype = {
        "store_id": str,
        "storetype_id": str,
        "store_size": int,
        "city_id": str,
    }

    df = GoogleCloudStorage.with_config(
        ConfigFileLoader(config_path, config_profile)
    ).load(bucket_name, object_key, format="csv", dtype=dtype)

    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, "The output is undefined"
