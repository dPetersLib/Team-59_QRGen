# pull official base image
FROM python:3.8-slim-buster

# set working directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# add app
COPY . .

# install python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
