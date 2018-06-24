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
	cp -r ../../depends/python/* depends

kubernetes_service:
	kubectl apply -f kuber/reciever-service.yaml

kubernetes_deployment:
	kubectl apply -f kuber/reciever-deployment.yaml
	
kubernetes_deployment_remove:
	kubectl delete deployment -l app=gateway

kubernetes_service_remove:
	kubectl delete service -l name=gateway

docker_build: \
	version_file_increment \
	docker_build_curr

docker_build_curr:
	o=`cut -f1 VERSION`; \
	docker build -t $(IMAGENAME):$$o . ;

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
	kubectl set image deployment/gateway-deployment $(IMAGENAME)=$(IMAGENAME):$$o


docker_images_cleanup: 
	o=`cut -f1 VERSION`; \
	echo "cleanup ", $$o; \
	r=`docker images | awk '/ / { print $$1" version="$$2" "$$3}'| grep $(IMAGENAME) | grep -v version=$$o | awk '/ / { print $$3 }'`; \
	echo $$r; \
	docker rmi $$r

# docker rmi $(docker images | awk '/ / { print $1" version="$2" "$3}'| grep "gateway" | grep -v version=1 | awk '/ / { print $3 }')
# docker images | awk '/ / { print $1" version="$2" "$3}'

docker_cleanup: \
	docker_images_cleanup
