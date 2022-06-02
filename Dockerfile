FROM python:3.8

WORKDIR /cicd_demo
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . /cicd_demo
