.PHONY: test
.PHONY: run

SERVICE_NAME=hello-world-printer

deps: 
	pip install -r requirements.txt; \
	pip install -r test_requirements.txt

lint:
	flake8 hello_world test

test:
	PYTHONPATH=. py.test

run:
	PYTHONPATH=. FLASK_APP=hello_world flask run

docker_build:
	docker build -t $(SERVICE_NAME) .

docker_run: docker_build
	docker run \
	--name $(SERVICE_NAME)-dev \
	-p 5000:5000 \
	-d $(SERVICE_NAME)

docker_stop: 
	docker stop $(SERVICE_NAME)-dev

USERNAME=agmarstudio
TAG=$(USERNAME)/$(SERVICE_NAME)

docker_push: docker_build
	@docker login --username $(USERNAME) --password $${DOCKER_PASSWORD}; \
	docker tag $(SERVICE_NAME) $(TAG); \
	docker push $(TAG); \
	docker logout;
