EXTRADEP := $(if $(EXTRADEP),$(EXTRADEP),$(realpath ./depends))
PIDFILE := $(if $(PIDFILE),$(PIDFILE),"$(PIDDIR)/stats.pid")
LOGFILE := $(if $(LOGFILE),$(LOGFILE),"$(LOGDIR)/stats.log")

PYTHONPATH=PYTHONPATH:$(EXTRADEP)
CONTAINERNAME=stats
IMAGENAME=stats

start:
	( \
		. venv/bin/activate; \
		nohup python3 stats/app.py > $(LOGFILE) 2>&1 & echo $$!> $(PIDFILE); \
	)

start_4_docker:
	PYTHONPATH=$(PYTHONPATH) python3 stats/app.py

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

docker_build: \
	version_file_increment \
	docker_build_curr

docker_build_curr:
	o=`cut -f1 VERSION`; \
	docker build -t $(IMAGENAME):$$o . ;

docker_run: \
	docker_stop \
	docker_container_remove \
	docker_run_container

kubernetes_service:
	kubectl apply -f kuber/stats-service.yaml

kubernetes_deployment:
	kubectl apply -f kuber/stats-deployment.yaml
	
kubernetes_deployment_remove:
	kubectl delete deployment -l app=stats

kubernetes_service_remove:
	kubectl delete service -l name=stats


version_file_increment:
	o=`cut -f1 VERSION`; \
	n=`expr $$o + 1`; \
	echo $$n > VERSION; \

kubernetes_buildnload: \
	docker_build \
	kubernetes_update_image

kubernetes_update_image:
	o=`cut -f1 VERSION`; \
	echo "image version is ", $$o; \
	kubectl set image deployment/stats-deployment $(IMAGENAME)=$(IMAGENAME):$$o