FROM python:3
MAINTAINER Eduard Asriyan <ed-asriyan@protonmail.com>

WORKDIR /application

ADD requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

ADD app ./app
ADD app.py app.py
ADD configuration ./configuration
ADD Makefile Makefile

ARG CONFIG=config.yml
ADD config.yml config.yml
COPY etc etc

EXPOSE 5000

ENTRYPOINT [ "make" ]
CMD [ "start_4_docker" ]
