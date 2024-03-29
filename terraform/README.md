# Resource Provisioning with Terraform

This directory contains Terraform configurations for provisioning resources in GCP.

## Getting Started

### Prerequisites:
- **Ensure Terraform is installed.** You may follow this [instruction](https://developer.hashicorp.com/Terraform/tutorials/gcp-get-started/install-cli) for Terraform installation 

### Using this directory:

- Review the Terraform configuration files (*.tf). These files define the resources you want to provision, such as virtual machines, storage, database etc.

- Update variables in the `variables.tf` file to match your specific needs (e.g., region, instance type, credentials etc.).

### Run Terraform commands
A Makefile was created to defines seperate targets for different tasks

Run the following for complete Terraform process from `Terraform init` -> `Terraform format` -> `Terraform plan` -> `Terraform apply`

```Makefile
make terraform
```
To destroy the provisioned resources, run the followng make command
```Makefile
make terraform_destroy
```

For finer control over each process, you could also run the Terraform command

- Terraform init: Initializes the Terraform workspace and downloads required provider plugins.
- Terraform plan: Shows the changes Terraform will make to your infrastructure based on the current configuration.
- Terraform apply: Applies the planned changes and provisions resources in your cloud platform.
- Terraform destroy: Destroys provisioned resources (use with caution!).


