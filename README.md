# Retail Sales Data Engineering Pipeline

The vast amount of data captured in retail sales transactions holds immense potential for uncovering valuable business insights. However, manually analyzing this data is cumbersome and inefficient.

This project aims to unlock the power of retail sales data by building an automated data engineering pipeline. This pipeline will prepare the data for analysis, allowing us to explore critical questions and gain a deeper understanding of our business.

## Key areas for analysis:

- Sales Trends: Identify patterns and trends in sales over time (e.g., seasonal fluctuations, product category performance, impact of promotions).
- Customer Behavior: Analyze customer purchasing habits (e.g., frequency, average order value, product preferences, customer segmentation).
- Product Performance: Evaluate the performance of individual products and product categories (e.g., identify best-sellers, analyze profitability, optimize pricing strategies).
- Marketing Effectiveness: Assess the impact of marketing campaigns on sales performance (e.g., track sales uplift after promotions, identify target audiences).
- Inventory Management: Optimize inventory levels based on sales data to minimize stockouts and overstocking.

## Project Details
This project proposes a data engineering pipeline that automates the data processing workflow utilizing the following tech stacks:
- `Mage AI` for orchestration
- `Google Cloud Platform (GCP)` services for storage
- `Spark` for big data loading and transformation
- `DBT` for data transformation 
- `Terraform` for cloud resources provision

The pipeline will:

- Extract retail sales data from Kaggle dataset.
- Validate the data against pre-defined schemas to ensure consistency and quality.
- Load the processed data into a BigQuery table.
- Transform the data to prepare it for analysis with DBT.
- Visualization

This automated pipeline will improve data accessibility, reliability, and ultimately facilitate better decision-making based on accurate and timely insights.

## Running the Project

This project utilizes a `Makefile` to automate various tasks. Here's how to use the Makefile to run the pipeline:

**1. Cloud resources provision:**
```script
make terraform
```
* Use the `make terraform` command to initialize Terraform in the terraform` directory. This make command will trigger a series of Terraform command to initialize Terraform in the Terraform directory, format Terraform code to ensure it adheres to a consistent style, preview the changes Terraform will make to your GCP resources based on your configuration and finally create or modify GCP resources as defined in your Terraform configuration.

**Remember:**

* Update the `terraform` directory with your GCP project ID and desired resource configurations before running these commands.

**2. Destroying Terraform resources:**
```script
make terraform_destroy
```
* Use `make terraform_destroy` to remove all resources provisioned by Terraform. This is useful for cleaning up your environment.

**3. Launching the Data Pipeline:**
```script
make docker
```
* Run `make docker` to start the data processing container defined in `docker-compose.yml`. This container executes the data pipeline steps using Mage AI.

**4. Stopping the Data Pipeline:**
```script
make docker_down
```
* Use `make docker_down` to stop the running data processing container.

**5. Getting Help:**
```script
Available rules:

docker              Launch data pipeline container
docker_down         Destroy data pipeline container
terraform           Create cloud resources via Terraform
terraform_destroy   Destroy cloud resources via Terraform
```
* Type `make` to display a list of available commands and their brief descriptions.

By utilizing these commands, you can manage your infrastructure provisioning and data processing workflow effectively.

## Resources

- [Data Engineering Zoomcamp by DataTalks.Club](https://github.com/DataTalksClub/data-engineering-zoomcamp)
