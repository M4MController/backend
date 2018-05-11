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

use_kubernetes_docker: 
	eval $(minikube docker-env)

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
	kubectl apply -f kuber/data-service.yaml

kubernetes_data_deployment:
	kubectl apply -f kuber/data-deployment.yaml
	
kubernetes_data_deployment_remove:
	kubectl delete deployment -l app=data

kubernetes_data_service_remove:
	kubectl delete service -l name=data

# stats kubernetes
kubernetes_stats_service:
	kubectl apply -f kuber/stats-service.yaml

kubernetes_stats_deployment:
	kubectl apply -f kuber/stats-deployment.yaml
	
kubernetes_stats_deployment_remove:
	kubectl delete deployment -l app=stats

kubernetes_stats_service_remove:
	kubectl delete service -l name=stats

# gateway kubernetes
kubernetes_gateway_service:
	kubectl apply -f kuber/gateway-service.yaml

kubernetes_gateway_deployment:
	kubectl apply -f kuber/gateway-deployment.yaml
	
kubernetes_gateway_deployment_remove:
	kubectl delete deployment -l app=gateway

kubernetes_gateway_service_remove:
	kubectl delete service -l name=gateway

# reciever kubernetes
kubernetes_reciever_service:
	kubectl apply -f kuber/reciever-service.yaml

kubernetes_reciever_deployment:
	kubectl apply -f kuber/reciever-deployment.yaml
	
kubernetes_reciever_deployment_remove:
	kubectl delete deployment -l app=reciever

kubernetes_reciever_service_remove:
	kubectl delete service -l name=reciever

# # rabbitmq
# kubernetes_rabbitmq_service:
# 	kubectl apply -f kuber/rabbitmq-service.yaml

# kubernetes_rabbitmq_controller:
# 	kubectl apply -f kuber/rabbitmq-controller.yaml
	
# kubernetes_rabbitmq_controller_remove:
# 	kubectl delete pod -l component=rabbitmq

# kubernetes_rabbitmq_service_remove:
# 	kubectl delete service -l name=rabbitmq

# устанавливаем dns
kubernetes_install_dns:
	kubectl --namespace=kube-system scale deployment kube-dns --replicas=$(DNSREPLICAS)

# устанавливаем mongo replica set:
helm_install_mongo:
	helm install stable/mongodb-replicaset

# устанавливаем rabbitmq 
helm_install_rabbitmq:
	helm install --set rabbitmq.username=user,rabbitmq.password=user stable/rabbitmq 