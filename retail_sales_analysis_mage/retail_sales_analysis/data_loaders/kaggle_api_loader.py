import os
from retail_sales_analysis.utils.data_config import SAVE_DIR

if "data_loader" not in globals():
    from mage_ai.data_preparation.decorators import data_loader


@data_loader
def load_kaggle_data(*args, **kwargs) -> None:
    """
    Load data from Kaggle with Kaggle API to local filesystem

    Returns:
        None
    """
    # Specify your data loading logic here
    os.system(
        f"kaggle datasets download -d berkayalan/retail-sales-data"
        f" -p {SAVE_DIR} --unzip"
    )
    print(f"All file loaded to {SAVE_DIR}...")
