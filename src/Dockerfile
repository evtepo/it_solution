FROM python:3.11-slim

WORKDIR /src

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY docker/launch.sh launch.sh

COPY requirements.txt requirements.txt

RUN apt-get update \
    && apt-get -y install postgresql-client \
    && apt-get -y install netcat-traditional \
    && pip install --upgrade pip --no-cache-dir \
    && pip install -r requirements.txt --no-cache-dir

COPY . .

ENTRYPOINT ["sh", "launch.sh"]
