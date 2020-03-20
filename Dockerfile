FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/
RUN apt-get update && apt-get install -y gettext libgettextpo-dev
RUN pip install -r requirements.txt
COPY . /app/
