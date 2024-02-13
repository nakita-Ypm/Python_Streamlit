include .env

rm:
	docker rm `docker ps -aq`

rmi:
	docker rmi `docker images -q`

crm:
	docker container rm `docker container ls  -aq`

up:
	cp .env.example .env
	docker compose up -d

down:
	docker compose down

ens:
	docker compose exec -it streamlit /bin/bash

exe:
	docker compose exec streamlit python3 ./src/main.py

fmt:
	docker-compose exec streamlit black ./

enf:
	docker compose exec -it flask /bin/bash

sr:
	docker-compose exec streamlit streamlit run ./src/home.py
