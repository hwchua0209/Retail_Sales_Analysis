from pyspark.sql import SparkSession

if "data_loader" not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if "test" not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data(*args, **kwargs) -> SparkSession:
    """
    Create Spark Session in Mage

    Returns:
       Spark Session
    """
    # Specify your data loading logic here
    spark = SparkSession.builder.getOrCreate()
    kwargs["context"]["spark"] = spark
