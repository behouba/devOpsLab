# syntax=docker/dockerfile:1

FROM python:3.9-alpine


# expose port
EXPOSE 5000

# Set env variables for Flask
ENV FLASK_ENV=development FLASK_APP=main.py

WORKDIR /app

# Create non root user
RUN adduser --disabled-password dockeruser && chown -R dockeruser /app
USER dockeruser


COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt --no-cache-dir

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]