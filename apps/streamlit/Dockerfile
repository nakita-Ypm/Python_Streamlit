FROM python:slim

WORKDIR /apps

COPY . .

RUN pip3 install -r requirements.txt


CMD ["tail", "-f", "/dev/null"]

# CMD ["python3", "./src/main.py"]