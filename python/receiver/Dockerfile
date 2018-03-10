FROM python:3
MAINTAINER Eduard Asriyan <ed-asriyan@protonmail.com>

WORKDIR /application

ADD requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

ADD app ./app
ADD app.py app.py
ADD configuration ./configuration

ARG CONFIG=config.yml
ADD $CONFIG config.yml

CMD ./app.py
