FROM python:3.9

LABEL maintainer ShantanuFadnis

ENV APP_HOME /app

WORKDIR ${APP_HOME}

RUN apt-get update && \
    apt-get clean && \
    apt-get install -y openjdk-11-jre-headless && \
    pip install --upgrade pip;

RUN pip install tox

COPY requirements.txt /tmp/requirements.txt

RUN \
    echo "Installing requirements" && \
    pip install -r /tmp/requirements.txt

COPY . /app
