terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.6.0"
    }
  }
}

provider "google" {
  credentials = file(var.credentials)
  project     = var.project
  region      = var.region
}

resource "google_storage_bucket" "sales-project-bucket" {
  name          = var.gcs_bucket_name
  location      = var.location
  force_destroy = true


  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}

resource "google_bigquery_dataset" "sales_analysis_dataset" {
  dataset_id = var.bq_name
  location   = var.location
}

# resource "google_bigquery_dataset" "sales_dataset" {
#   dataset_id = var.bq_sales_name
#   location   = var.location
# }

# resource "google_bigquery_dataset" "store_dataset" {
#   dataset_id = var.bq_store_name
#   location   = var.location
# }