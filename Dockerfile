FROM python:3.7-slim

RUN mkdir /main
WORKDIR /main

COPY ./main/requirements.txt /main
RUN pip install -r requirements.txt

COPY ./main /main