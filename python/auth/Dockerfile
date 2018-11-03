FROM python:3
MAINTAINER Eduard Asriyan <ed-asriyan@protonmail.com>

WORKDIR /application

ADD requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

ADD auth auth
ADD Makefile Makefile

ARG CONFIG=config.yml
ADD config.yml.example config.yml

EXPOSE 5000

ENTRYPOINT [ "make" ]
CMD [ "start_4_docker" ]
