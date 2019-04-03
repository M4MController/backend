FROM grpc/python:1.4-onbuild
COPY depends depends
COPY receiver receiver
COPY requirements.txt requirements.txt
COPY Makefile Makefile
COPY etc etc
RUN apt-get update && apt-get install make
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
ENTRYPOINT [ "make" ]
CMD [ "start_4_docker" ]