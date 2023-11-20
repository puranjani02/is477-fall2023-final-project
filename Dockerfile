FROM python:3.10-bullseye
WORKDIR /is477
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt