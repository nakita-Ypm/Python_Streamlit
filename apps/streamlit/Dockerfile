FROM python:slim

WORKDIR /apps

COPY . .

RUN pip3 install -r requirements.txt

CMD ["streamlit", "run", "./src/home.py"]

 