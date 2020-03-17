FROM python:3.7.7-slim-buster
MAINTAINER Atila Aloise de Almeida

COPY /src/api /api

RUN pip3 install -r /api/requirements.txt

EXPOSE 5000
# start
CMD python3 /api/api.py