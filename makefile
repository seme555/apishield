install:
	pipenv install

build:
	docker-compose build

run:
	docker-compose up 

brun:
	docker-compose up --build

stop:
	docker-compose stop 

destroy:
	docker-compose down 

