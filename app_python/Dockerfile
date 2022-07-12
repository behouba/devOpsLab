# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

# expose port
EXPOSE 5000

# Set env variables for Flask
ENV FLASK_ENV=development FLASK_APP=main.py

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt --no-cache-dir

# Create non root user
RUN adduser --disabled-password appuser && chown -R appuser /app
USER appuser


COPY requirements.txt requirements.txt



ENTRYPOINT [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]