FROM python:3.10-slim-buster

# set working directory
WORKDIR /usr/src/app

# Install pipenv and compilation dependencies
RUN pip install pipenv

# COPY dependencies
COPY ./Pipfile /usr/src/app/Pipfile
COPY ./Pipfile.lock /usr/src/app/Pipfile.lock

# Install dependencies
RUN pipenv install --system --deploy --ignore-pipfile

# Add app
COPY . /usr/src/app
