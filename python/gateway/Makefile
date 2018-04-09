EXTRADEP := $(if $(EXTRADEP),$(EXTRADEP),$(realpath ./depends))
PIDFILE := $(if $(PIDFILE),$(PIDFILE),"$(PIDDIR)/gateway.pid")
LOGFILE := $(if $(LOGFILE),$(LOGFILE),"$(LOGDIR)/gateway.log")

PYTHONPATH=PYTHONPATH:$(EXTRADEP)
CONTAINERNAME=gateway
IMAGENAME=gateway

start:
	( \
		if [ -d venv ]; then \
			. venv/bin/activate; \
		fi; \
		PYTHONPATH=$(PYTHONPATH) FLASK_APP=gateway/app.py nohup python3 -m flask run --host=0.0.0.0  > $(LOGFILE) 2>&1 & echo $$!> $(PIDFILE); \
	)

start_4_docker:
	PYTHONPATH=$(PYTHONPATH) FLASK_APP=gateway/app.py python3 -m flask run --host=0.0.0.0

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

run_test:
	( \
		if [ -d venv ]; then \
			. venv/bin/activate; \
		fi; \
		PYTHONPATH=$(PYTHONPATH) python3 run_test.py; \
	)

stop:
	cat $(PIDFILE) | xargs kill

build:
	cp -r ../../depends/python depends
