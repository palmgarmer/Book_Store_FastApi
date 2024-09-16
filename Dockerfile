# FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9
FROM python:3.9-slim-bullseye

# set working directory
WORKDIR ./app

# copy dependencies
COPY requirements.txt .

# install FreeTDS and dependencies
RUN apt-get update \
 && apt-get install --reinstall build-essential -y

# install pyodbc (and, optionally, sqlalchemy)
RUN python -m pip install --upgrade pip
RUN pip install --upgrade setuptools

# psycopg2 for connection postgres
RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2==2.9.3

# install dependencies
RUN pip install -r requirements.txt

# copy project
COPY . /app/
