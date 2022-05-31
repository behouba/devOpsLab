#!/bin/bash
app="behouba/devops-labs:lab2"

# Build the image
docker build -t ${app} .

# Scan the image
docker scan ${app}

