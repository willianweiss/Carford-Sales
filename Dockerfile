FROM python:3.9.7

WORKDIR /api

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .
