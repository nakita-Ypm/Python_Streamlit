FROM python:slim

WORKDIR /apps

COPY . .

RUN pip3 install -r requirements.txt

CMD ["tail", "-f", "/dev/null"]

# CMD ["streamlit", "run", "./src/main.py"]

 