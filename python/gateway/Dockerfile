FROM grpc/python:1.4-onbuild
COPY depends depends
COPY gateway gateway
COPY Makefile Makefile
COPY requirements.txt requirements.txt
COPY etc etc
COPY run_test.py run_test.py
RUN apt-get update && apt-get install make
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn
EXPOSE 5000
# ENTRYPOINT ["python3"]
ENTRYPOINT ["make"]
CMD [ "start_4_docker_prod" ]