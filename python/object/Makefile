EXTRADEP := $(if $(EXTRADEP),$(EXTRADEP),$(realpath ./depends))
PIDFILE := $(if $(PIDFILE),$(PIDFILE),"$(PIDDIR)/object.pid")
LOGFILE := $(if $(LOGFILE),$(LOGFILE),"$(LOGDIR)/object.log")

PYTHONPATH=PYTHONPATH:$(EXTRADEP)
CONTAINERNAME=object
IMAGENAME=object

start:
	( \
		. venv/bin/activate; \
		nohup python3 object/app.py --config ./etc/config_s.json > $(LOGFILE) 2>&1 & echo $$!> $(PIDFILE); \
	)

start_4_docker:
	PYTHONPATH=$(PYTHONPATH) python3 object/app.py --config ./etc/config.json

stop:
	cat $(PIDFILE) | xargs kill

build:
	cp -r ../../depends/python/* depends

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
	kubectl apply -f kuber/object-service.yaml

kubernetes_deployment:
	kubectl apply -f kuber/object-deployment.yaml
	
kubernetes_deployment_remove:
	kubectl delete deployment -l app=object

kubernetes_service_remove:
	kubectl delete service -l name=object


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
	kubectl set image deployment/object-deployment $(IMAGENAME)=$(IMAGENAME):$$o

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


# как накатывать базу postgres
# 1. создём под
# kubectl run --namespace default postgresql-client --restart=Never --rm --tty -i --image postgres    --env "PGPASSWORD=$PGPASSWORD"    --command -- psql -U user -h postgresql postgres
# 2. накатываем
# kubectl exec -it postgresql-client -- psql -U user -h postgresql | cat object/schema/schema.sql