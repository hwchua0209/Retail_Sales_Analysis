import os

# Kaggle Config

SAVE_DIR = os.path.join(os.getcwd(), "datasets")

# GCS Config
GCS_BUCKET_NAME = "plucky-spirit-412403-sales-bucket"

# Sales Config
SALES_COL = [
    'product_id',
    'store_id',
    'date',
    'sales',
    'revenue',
    'stock',
    'price',
]

# Product Hierachy Config
PRODUCT_HIERACHY_COL = [
    'product_id',
    'product_length',
    'product_depth',
    'product_width',
    'cluster_id',
]
