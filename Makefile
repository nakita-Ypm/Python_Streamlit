include .env

rm:
	docker rm `docker ps -aq`

rmi:
	docker rmi `docker images -q`

crm:
	docker container rm `docker container ls  -aq`

up:
	docker compose up -d

down:
	docker compose down

ens:
	docker compose exec -it streamlit /bin/bash

exe:
	docker compose exec streamlit python3 ./src/main.py


# python3 ./src/handler/ping_handler.py

# python3 ./src/adapter/adapter.py

# python3 ./src/main.py

# streamlit run ./src/main.py