FROM python:alpine3.6

COPY requirements.txt /requirements.txt
COPY main.py /src/main.py
RUN pip install -r /requirements.txt
RUN python
