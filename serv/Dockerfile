FROM python:3.8-alpine

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN python3 -m pip install --upgrade pip && pip install pipenv

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

RUN apk add libffi-dev

COPY . /app/

RUN pipenv install --system --deploy
