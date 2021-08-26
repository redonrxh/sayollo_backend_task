FROM python:3.9.6

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

ADD . /app
WORKDIR /app

RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt
