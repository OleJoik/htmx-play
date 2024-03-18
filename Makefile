.PHONY: help

# Run "make" to get help with how to use the makefile
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help

reload: ## Run app in uvicorn with reload flag
	poetry run uvicorn main:app --host 0.0.0.0 --port 3000 --reload
