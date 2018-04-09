EXTRADEP := $(if $(EXTRADEP),$(EXTRADEP),$(realpath ./depends))
PIDFILE := $(if $(PIDFILE),$(PIDFILE),"$(PIDDIR)/reciever.pid")
LOGFILE := $(if $(LOGFILE),$(LOGFILE),"$(LOGDIR)/reciever.log")

PYTHONPATH=PYTHONPATH:$(EXTRADEP)
CONTAINERNAME=reciever
IMAGENAME=reciever
CONFIG=config.yml.example

start:
	( \
		. venv/bin/activate; \
		nohup python3 reciever/app.py > $(LOGFILE) 2>&1 & echo $$!> $(PIDFILE); \
	)

start_4_docker:
	PYTHONPATH=$(PYTHONPATH) python3 reciever/app.py

stop:
	cat $(PIDFILE) | xargs kill

build:
	cp -r ../../depends/python depends

docker_stop:
	-docker container stop $(CONTAINERNAME)

docker_container_remove:
	-docker container rm $(CONTAINERNAME)

docker_run_container:
	docker run -p 5000:5000 -d --name $(CONTAINERNAME) $(IMAGENAME)

docker_build:
	docker build -t $(IMAGENAME) .

docker_run: \
	docker_stop \
	docker_container_remove \
	docker_run_container