FROM jfloff/alpine-python:3.6

RUN apk update
RUN apk add tcpdump
RUN apk add screen

COPY src /root/flooder

WORKDIR /root/flooder

RUN pip install -r requirements.txt

RUN mkdir out

USER root

