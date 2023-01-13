#!/bin/bash

# Docker build
app="flask_cicd"
docker build -t ${app} .
docker run --name ${app} -p 5000:5000 ${app}
