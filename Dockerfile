FROM python:3.12

WORKDIR /api_cardiotech

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt
