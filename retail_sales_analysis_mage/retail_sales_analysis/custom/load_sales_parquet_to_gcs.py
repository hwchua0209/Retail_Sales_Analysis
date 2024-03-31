from pyspark.sql import types
import pyspark.sql.functions as F

from retail_sales_analysis.utils.data_config import GCS_BUCKET_NAME, SALES_COL
from retail_sales_analysis.utils.gcp_helper import (
    get_gcp_creds,
)

if "custom" not in globals():
    from mage_ai.data_preparation.decorators import custom
if "test" not in globals():
    from mage_ai.data_preparation.decorators import test


@custom
def load_sales_parquet_to_gcs(*args, **kwargs) -> None:
    """
    args: The output from any upstream parent blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    get_gcp_creds()

    bucket_name = GCS_BUCKET_NAME
    object_key_raw = "raw/sales/"
    object_key_processed = "processed/sales/"

    gcs_raw = f"gs://{bucket_name}/{object_key_raw}"
    gcs_processed = f"gs://{bucket_name}/{object_key_processed}"

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
        .load(gcs_raw)
    )

    df = df.select(*SALES_COL)
    df = df.withColumn("year", F.year("date"))
    df = df.withColumn("month", F.month("date"))
    df = df.withColumn("day", F.day("date"))

    df.write.parquet(gcs_processed, mode="overwrite")

    print("Sales dataframe written to GCS")
