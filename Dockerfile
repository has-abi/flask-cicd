FROM python:3.10-slim-buster

# set working directory
WORKDIR /usr/src/app

# Install pipenv and compilation dependencies
RUN pip install pipenv

# COPY python dependencies
COPY ./Pipfile /usr/src/app/Pipfile
COPY ./Pipfile.lock /usr/src/app/Pipfile.lock

# Install python dependencies
RUN pipenv install --system --deploy --ignore-pipfile

# Install python dependencies
RUN pipenv install --system --deploy --ignore-pipfile

# Add app
COPY . /usr/src/app

# Run
CMD gunicorn --bind 0.0.0.0:5000 manage:app