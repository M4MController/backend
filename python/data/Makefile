EXTRADEP := $(if $(EXTRADEP),$(EXTRADEP),$(realpath ./depends))
PIDFILE := $(if $(PIDFILE),$(PIDFILE),"$(PIDDIR)/data.pid")
LOGFILE := $(if $(LOGFILE),$(LOGFILE),"$(LOGDIR)/data.log")

PYTHONPATH=PYTHONPATH:$(EXTRADEP)
CONTAINERNAME=data
IMAGENAME=data

start:
	( \
		. venv/bin/activate; \
		nohup python3 data/app.py --config ./etc/config_s.json > $(LOGFILE) 2>&1 & echo $$!> $(PIDFILE); \
	)

start_4_docker:
	PYTHONPATH=$(PYTHONPATH) python3 data/app.py --config ./etc/config.json

stop:
	cat $(PIDFILE) | xargs kill

build:
	cp -r ../../depends/python/* depends

docker_stop:
	-docker container stop $(CONTAINERNAME)

docker_container_remove:
	-docker container rm $(CONTAINERNAME)

docker_run_container:
	docker run -p 5000:5000  -d --name $(CONTAINERNAME) $(IMAGENAME)

docker_run: \
	docker_stop \
	docker_container_remove \
	docker_run_container

docker_build: \
	version_file_increment \
	docker_build_curr

docker_build_curr:
	o=`cut -f1 VERSION`; \
	docker build -t $(IMAGENAME):$$o . ;

kubernetes_service:
	kubectl apply -f kuber/data-service.yaml

kubernetes_deployment:
	kubectl apply -f kuber/data-deployment.yaml
	
kubernetes_deployment_remove:
	kubectl delete deployment -l app=data

kubernetes_service_remove:
	kubectl delete service -l name=data

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
	kubectl set image deployment/data-deployment $(IMAGENAME)=$(IMAGENAME):$$o

# docker rmi $(docker images | awk '/ / { print $1" version="$2" "$3}'| grep "gateway" | grep -v version=1 | awk '/ / { print $3 }')
# docker images | awk '/ / { print $1" version="$2" "$3}'

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
	
fill_data:
	( \
		. venv/bin/activate; \
		PYTHONPATH=$(PYTHONPATH) python3 utils/fill_data.py;\
	)

fixture: 
	( \
		. venv/bin/activate; \
		PYTHONPATH=$(PYTHONPATH):depends python3 utils/fill_data.py localhost:27017 1;\
	)
