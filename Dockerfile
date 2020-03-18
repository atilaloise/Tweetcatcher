FROM python:3.7.7-slim-buster
MAINTAINER Atila Aloise de Almeida

COPY /src/api /api

RUN pip3 install -r /api/requirements.txt

EXPOSE 8000
# start
CMD cd /api && gunicorn --bind 0.0.0.0 api:app --log-config config/gunicorn-logs.conf