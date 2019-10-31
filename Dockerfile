FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /example
WORKDIR /example
COPY requirements.txt /example/
RUN pip install -r requirements.txt
COPY . /example/