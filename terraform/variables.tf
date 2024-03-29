variable "credentials" {
  description = "GCP Credentials"
  default     = "../secrets/gcp_creds.json"
}


variable "project" {
  description = "Project"
  default     = "plucky-spirit-412403"
}

variable "region" {
  description = "Region"
  default     = "us"
}

variable "location" {
  description = "Project Location"
  default     = "us"
}

variable "bq_name" {
  description = "Sales Dataset"
  default     = "sales_analysis"
}

# variable "bq_product_name" {
#   description = "Product Dataset"
#   default     = "product_dataset"
# }

# variable "bq_store_name" {
#   description = "Store Dataset"
#   default     = "store_dataset"
# }

variable "gcs_bucket_name" {
  description = "Project Bucket Name"
  default     = "plucky-spirit-412403-sales-bucket"
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}

