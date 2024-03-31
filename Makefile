PROJECT_NAME=retail_sales_analysis_mage-magic
#################################################################################
# Terraform Commands          		                                            #
#################################################################################
terraform_init:
	@echo "Initializing terraform"
	@cd terraform;\
	terraform init

terraform_format: terraform_init
	@echo "Formatting terraform file"
	@cd terraform;\
	terraform fmt -recursive

terraform_plan: terraform_format
	@echo "Plan terraform"
	@cd terraform;\
	terraform plan

terraform_apply: terraform_plan
	@echo "Apply terraform"
	@cd terraform;\
	terraform apply

## Destroy cloud resources via Terraform
terraform_destroy:
	@echo "Destroy all terraform setup"
	@cd terraform;\
	terraform destroy

## Create cloud resources via Terraform
terraform: terraform_apply

#################################################################################
# Docker Compose Commands                                                       #
#################################################################################

## Launch data pipeline container
start:
	@echo "Launching data pipeline container"
	@cd retail_sales_analysis_mage;\
	docker compose down;\
	docker compose build;\
	docker compose up

## Clean up data pipeline container
clean:
	@echo "Destroy data pipeline container"
	@cd retail_sales_analysis_mage;\
	docker compose down;\
	docker ps -a | awk '/$(PROJECT_NAME)/ { print $$1 }' | xargs docker rm -f;\
  	docker images -a | awk '/$(PROJECT_NAME)/ { print $$3 }' | xargs docker rmi -f

#################################################################################
# Self Documenting Commands                                                     #
#################################################################################

.DEFAULT_GOAL := help

.PHONY: help
help:
	@echo "$$(tput bold)Available rules:$$(tput sgr0)"
	@echo
	@sed -n -e "/^## / { \
		h; \
		s/.*//; \
		:doc" \
		-e "H; \
		n; \
		s/^## //; \
		t doc" \
		-e "s/:.*//; \
		G; \
		s/\\n## /---/; \
		s/\\n/ /g; \
		p; \
	}" ${MAKEFILE_LIST} \
	| LC_ALL='C' sort --ignore-case \
	| awk -F '---' \
		-v ncol=$$(tput cols) \
		-v indent=19 \
		-v col_on="$$(tput setaf 5)" \
		-v col_off="$$(tput sgr0)" \
	'{ \
		printf "%s%*s%s ", col_on, -indent, $$1, col_off; \
		n = split($$2, words, " "); \
		line_length = ncol - indent; \
		for (i = 1; i <= n; i++) { \
			line_length -= length(words[i]) + 1; \
			if (line_length <= 0) { \
				line_length = ncol - indent - length(words[i]) - 1; \
				printf "\n%*s ", -indent, " "; \
			} \
			printf "%s ", words[i]; \
		} \
		printf "\n"; \
	}' \
	| more $(shell test $(shell uname) = Darwin && echo '--no-init --raw-control-chars')