from pyspark.sql import DataFrame, types

from retail_sales_analysis.utils.data_config import GCS_BUCKET_NAME
from retail_sales_analysis.utils.gcp_helper import get_gcp_creds

if "data_loader" not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if "test" not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_from_google_cloud_storage() -> DataFrame:
    """
    Template for loading data from a Google Cloud Storage bucket.
    Specify your configuration settings in 'io_config.yaml'.

    Docs: https://docs.mage.ai/design/data-loading#googlecloudstorage
    """
    get_gcp_creds()

    bucket_name = GCS_BUCKET_NAME
    object_key = "raw/sales"

    gcs = f"gs://{bucket_name}/{object_key}"

    # Set Schema
    schema = types.StructType(
        [
            types.StructField("product_id", types.StringType(), True),
            types.StructField("store_id", types.StringType(), True),
            types.StructField("date", types.DateType(), True),
            types.StructField("sales", types.IntegerType(), True),
            types.StructField("revenue", types.FloatType(), True),
            types.StructField("stock", types.IntegerType(), True),
            types.StructField("price", types.FloatType(), True),
            types.StructField("promo_type_1", types.StringType(), True),
            types.StructField("promo_bin_1", types.StringType(), True),
            types.StructField("promo_type_2", types.StringType(), True),
            types.StructField("promo_bin_2", types.StringType(), True),
            types.StructField("promo_discount_2", types.FloatType(), True),
            types.StructField("promo_discount_type_2", types.StringType(), True),
        ]
    )
    df = (
        kwargs["spark"]
        .read.format("csv")
        .option("header", "true")
        .option("delimiter", ",")
        .schema(schema)
        .load(gcs)
    )

    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, "The output is undefined"
