FROM python:3.12-alpine3.20

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt /temp/requirements.txt

COPY service /app

EXPOSE 8000

RUN apk add postgresql-client postgresql-dev build-base

RUN pip install -r /temp/requirements.txt