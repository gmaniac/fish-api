# prefix the repository name with qb/ as a namespace
REPO_NAME := pets-on-pets/api

# All of these variables are defaulted and do not need to be changed
TOKEN?=need_to_pass_gem_token

develop:
	@docker build --no-cache --build-arg TOKEN=${TOKEN} -f ./Dockerfile.develop -t ${REPO_NAME}:develop .