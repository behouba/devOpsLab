# syntax=docker/dockerfile:1

FROM python:3.9-alpine

# Create non root user
RUN adduser --home /app --shell /bin/sh --uid 1000 --disabled-password dockeruser
USER dockeruser

# expose port
EXPOSE 5000

# Set env variables for Flask
ENV FLASK_ENV=development FLASK_APP=main.py

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt --no-cache-dir

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]