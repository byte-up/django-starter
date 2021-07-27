# pull official base image
FROM python:3.8.3-alpine

ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/
RUN apk update \
    && apk add postgresql-dev gcc python3-dev zlib-dev jpeg-dev musl-dev libffi-dev \
    freetype-dev libjpeg freetype-dev libjpeg-turbo-dev libjpeg-turbo openssl-dev cargo rust
RUN pip install -r requirements.txt
COPY . /app/
