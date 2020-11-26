FROM python:3.9-slim-buster

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
RUN pip install -U pip setuptools && pip install -r /app/requirements.txt

WORKDIR /app/
COPY ./app.py /app
COPY ./service.py /app

CMD gunicorn service:app --bind=0.0.0.0:$PORT -w 4 -k uvicorn.workers.UvicornH11Worker