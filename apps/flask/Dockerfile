uuuuFROM python:slim

WORKDIR /apps

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 3001

CMD ["tail", "-f", "/dev/null"]

# CMD ["python3", "./src/main.py"]