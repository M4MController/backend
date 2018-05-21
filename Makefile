LOGDIR = $(realpath ./logs/)
PIDDIR = $(realpath ./pids/)
IMPORTDIR = $(realpath ./depends)
DNSREPLICAS = 1
PYTHONIMP = $(IMPORTDIR)/python

PYTHONPATH = PYTHONPATH:$(PYTHONIMP)

export

run_test:
	$(MAKE) -C  python/gateway run_test

start_data:
	$(MAKE) -C  python/data start

start_gateway:
	$(MAKE) -C  python/gateway start

start_stats:
	$(MAKE) -C  python/stats start

start_receiver:
	$(MAKE) -C  python/receiver start

stop_data:
	-$(MAKE) -C  python/data stop

stop_gateway:
	-$(MAKE) -C  python/gateway stop

stop_stats:
	-$(MAKE) -C  python/stats stop


start_all: \
	start_data \
	start_stats \
	start_gateway \

stop_all: \
	stop_data \
	stop_stats \
	stop_gateway \

build_data:
	$(MAKE) -C  python/data build

build_gateway:
	$(MAKE) -C  python/gateway build

build_stats:
	$(MAKE) -C  python/stats build

build_all: \
	rebuild_protobuf \
	build_data \
	build_stats \
	build_gateway \

# не работает, надо лапками вводить команду у себя для работы
use_kubernetes_docker: 
	@eval $$(minikube docker-env)

# выкатываем с тегом
docker_image_build_gateway_minikube:
	@eval $$(minikube docker-env);\
	$(MAKE) -C  python/gateway docker_build

docker_image_build_data_minikube:
	@eval $$(minikube docker-env);\
	$(MAKE) -C  python/data docker_build

docker_image_build_stats_minikube:
	@eval $$(minikube docker-env);\
	$(MAKE) -C  python/stats docker_build

docker_image_build_receiver_minikube:
	@eval $$(minikube docker-env);\
	$(MAKE) -C  python/receiver docker_build

docker_images_minikube_build: \
	docker_image_build_gateway_minikube \
	docker_image_build_data_minikube \
	docker_image_build_stats_minikube \
	docker_image_build_receiver_minikube

#выкатываем без перетеггирования 
docker_image_build_gateway_minikube_curr:
	@eval $$(minikube docker-env);\
	$(MAKE) -C  python/gateway docker_build_curr

docker_image_build_data_minikube_curr:
	@eval $$(minikube docker-env);\
	$(MAKE) -C  python/data docker_build_curr

docker_image_build_stats_minikube_curr:
	@eval $$(minikube docker-env);\
	$(MAKE) -C  python/stats docker_build_curr

docker_image_build_receiver_minikube_curr:
	@eval $$(minikube docker-env);\
	$(MAKE) -C  python/receiver docker_build_curr


docker_images_minikube_build_curr: \
	docker_image_build_gateway_minikube_curr \
	docker_image_build_data_minikube_curr \
	docker_image_build_stats_minikube_curr \
	docker_image_build_receiver_minikube_curr

# просто выкатываем образы
docker_image_build_gateway:
	$(MAKE) -C  python/gateway docker_build

docker_image_build_data:
	$(MAKE) -C  python/data docker_build

docker_image_build_stats:
	$(MAKE) -C  python/stats docker_build

docker_image_build_receiver:
	$(MAKE) -C  python/receiver docker_build

docker_images_build: \
	docker_image_build_gateway \
	docker_image_build_data \
	docker_image_build_stats \
	docker_image_build_receiver

kubernetes_docker_images_build: \
	use_kubernetes_docker \
	docker_images_build

rebuild_protobuf: 
	python3 -m grpc_tools.protoc -I./protobuf/ ./protobuf/proto/*.proto --python_out=./depends/python/ --grpc_python_out=./depends/python/

# data kubernetes
kubernetes_data_service:
	$(MAKE) -C  python/data kubernetes_service

kubernetes_data_deployment:
	$(MAKE) -C  python/data kubernetes_deployment
	
kubernetes_data_deployment_remove:
	$(MAKE) -C  python/data kubernetes_deployment_remove

kubernetes_data_service_remove:
	$(MAKE) -C  python/data kubernetes_service_remove


#Собираем новый образ и запускаем
kubernetes_data_buildnload:
	@eval $$(minikube docker-env); \
	$(MAKE) -C  python/data kubernetes_buildnload

# stats kubernetes
kubernetes_stats_service:
	$(MAKE) -C  python/stats kubernetes_service

kubernetes_stats_deployment:
	$(MAKE) -C  python/stats kubernetes_deployment
	
kubernetes_stats_deployment_remove:
	$(MAKE) -C  python/stats kubernetes_deployment_remove

kubernetes_stats_service_remove:
	$(MAKE) -C  python/stats kubernetes_service_remove

kubernetes_stats_buildnload:
	@eval $$(minikube docker-env); \
	$(MAKE) -C  python/stats kubernetes_buildnload


# gateway kubernetes
kubernetes_gateway_service:
	$(MAKE) -C  python/gateway kubernetes_service

kubernetes_gateway_deployment:
	$(MAKE) -C  python/gateway kubernetes_deployment
	
kubernetes_gateway_deployment_remove:
	$(MAKE) -C  python/gateway kubernetes_deployment_remove

kubernetes_gateway_service_remove:
	$(MAKE) -C  python/gateway kubernetes_service_remove

kubernetes_gateway_buildnload:
	@eval $$(minikube docker-env); \
	$(MAKE) -C  python/gateway kubernetes_buildnload


# reciever kubernetes
kubernetes_reciever_service:
	$(MAKE) -C  python/receiver kubernetes_service

kubernetes_reciever_deployment:
	$(MAKE) -C  python/receiver kubernetes_deployment
	
kubernetes_reciever_deployment_remove:
	$(MAKE) -C  python/receiver kubernetes_deployment_remove

kubernetes_reciever_service_remove:
	$(MAKE) -C  python/receiver kubernetes_service_remove

kubernetes_receiver_buildnload:
	@eval $$(minikube docker-env); \
	$(MAKE) -C  python/receiver kubernetes_buildnload


# устанавливаем dns
kubernetes_install_dns:
	kubectl --namespace=kube-system scale deployment kube-dns --replicas=$(DNSREPLICAS)

# устанавливаем mongo replica set:
helm_install_mongo:
	helm install --name mongodb --set replicas=1 stable/mongodb-replicaset 

# устанавливаем rabbitmq 
helm_install_rabbitmq:
	helm install --name rabbitmq --set rabbitmq.username=user,rabbitmq.password=user,persistence.enabled=false,rbacEnabled=true stable/rabbitmq 