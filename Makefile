SHELL=/bin/bash
# === USER PARAMETERS
ifdef OS
   export PYTHON_COMMAND=python
   export UV_INSTALL_CMD=pip install uv==0.2.26
   export VENV_BIN=.venv/Scripts
else
   export PYTHON_COMMAND=python3.12
   export UV_INSTALL_CMD=pip install uv==0.2.26
   export VENV_BIN=.venv/bin
endif

export SRC_DIR=portfolio
ifndef BRANCH_NAME
	export BRANCH_NAME=$(shell git rev-parse --abbrev-ref HEAD)
endif
DEPLOY_ENVIRONMENT=$(shell if [ $(findstring main, $(BRANCH_NAME)) ]; then \
			echo 'prod'; \
		elif [ $(findstring pre, $(BRANCH_NAME)) ]; then \
			echo 'pre'; \
		else \
		 	echo 'dev'; \
		fi)
# If use deploy_environment in the tag system
# `y` => yes
# `n` => no
USE_DEPLOY_ENVIRONMENT=y

# == SETUP REPOSITORY AND DEPENDENCIES
create-env:
	# create environment
	uv venv -p $(PYTHON_COMMAND)

install-uv:
	# install uv package manager
	$(UV_INSTALL_CMD)

set-hooks:
	cp .hooks/pre-commit .git/hooks/pre-commit && chmod +x .git/hooks/pre-commit
	cp .hooks/pre-push .git/hooks/pre-push && chmod +x .git/hooks/pre-push
	cp .hooks/post-merge .git/hooks/post-merge && chmod +x .git/hooks/post-merge

compile:
	# install extra dev group
	uv pip compile pyproject.toml --extra dev -o requirements.txt --cache-dir .uv_cache

install:
	uv pip sync requirements.txt --cache-dir .uv_cache

setup: install-uv set-hooks compile install

# === CODE VALIDATION
format:
	. $(VENV_BIN)/activate && ruff format $(SRC_DIR)

lint:
	. $(VENV_BIN)/activate && ruff check $(SRC_DIR) --fix
	. $(VENV_BIN)/activate && mypy --ignore-missing-imports --install-types --non-interactive --package $(SRC_DIR)

test:
	. $(VENV_BIN)/activate && pytest --verbose --color=yes --cov=$(SRC_DIR) -n auto

all-validation: format lint test

# === DEPLOYMENT
docker-build:
	docker build -t portfolio .

docker-run:
	docker run -p 8000:8000 portfolio

docker-tag:
	docker tag portfolio:latest portfolio:$(BRANCH_NAME)

docker-push:
	docker push portfolio:$(BRANCH_NAME)

docker-setup: docker-build docker-tag docker-run 