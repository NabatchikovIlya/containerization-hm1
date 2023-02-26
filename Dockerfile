FROM python:3.10

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /usr/src/app
COPY api/ /usr/src/app


RUN pip install --upgrade pip
RUN pip install --upgrade -r requirements.txt