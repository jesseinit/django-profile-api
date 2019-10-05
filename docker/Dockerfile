# Set base image
FROM python:3.6-buster

# Maintainer
LABEL maintainer="Jesse Egbosionu <j3bsie@gmail.com>"

# Default user
USER root

# Set working directory in the container
WORKDIR /app

# Update base os packages and base app dependencies

RUN apt-get update -u && apt-get install -y supervisor libpq-dev python3-dev python3-pip && python3 -m pip install pipenv

# Start process manager
RUN supervisord

# Copy app process config file to container
# COPY ./docker/profile_api.conf /etc/supervisor/conf.d/profile_api.conf

# Copy files and folder to container
COPY . /app

RUN pipenv install

RUN ls -ah


