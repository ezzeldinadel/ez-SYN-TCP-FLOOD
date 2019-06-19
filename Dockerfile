FROM jfloff/alpine-python:3.6

USER root

RUN apk add screen

COPY src /root/flooder

WORKDIR /root/flooder

RUN pip install -r requirements.txt

RUN mkdir out


