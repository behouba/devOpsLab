#!/bin/bash
app="behouba/devops-labs:latest"

# Build the image
docker build -t ${app} .

# Scan the image
docker scan ${app}

