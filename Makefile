LOGDIR = $(realpath ./logs/)
PIDDIR = $(realpath ./pids/)
IMPORTDIR = $(realpath ./depends)
DNSREPLICAS = 1
PYTHONIMP = $(IMPORTDIR)/python

PYTHONPATH = PYTHONPATH:$(PYTHONIMP)

export

include python/*/Export.mk

run_test:
	$(MAKE) -C python/gateway run_test

start_all: \
	start_data \
	start_stats \
	start_users \
	start_object \
	start_gateway \
	start_auth \
	start_companies \
	start_tariffs \

stop_all: \
	stop_data \
	stop_stats \
	stop_users \
	stop_object \
	stop_gateway \
	stop_auth \
	stop_companies \
	stop_tariffs \

build_all: \
	rebuild_protobuf \
	build_data \
	build_stats \
	build_users \
	build_object \
	build_gateway \
	build_auth \
	build_companies \
	build_tariffs \

docker_clean_all: \
	docker_clean_data \
	docker_clean_stats \
	docker_clean_users \
	docker_clean_object \
	docker_clean_gateway \
	docker_clean_auth \
	#docker_clean_companies \
	#docker_clean_tariffs \


# для работы с докером необходимо переключить контекст на minikube
# сделать это из makefile для родительского терминала без костылей 
# (я не уверен) нельзя, ткчт для работы с докером minikube надо ввести
# eval $(minikube docker-env)
# в текущем терминале

# выкатываем с тегом
#docker_image_build_gateway:
#	$(MAKE) -C  python/gateway docker_build

docker_images_build: \
	docker_image_build_gateway \
	docker_image_build_data \
	docker_image_build_stats \
	docker_image_build_users \
	docker_image_build_object \
	docker_image_build_auth \
	docker_image_build_receiver \
	docker_image_build_companies \
	docker_image_build_tariffs \

#выкатываем без перетеггирования 

docker_images_build_curr: \
	docker_image_build_curr_gateway \
	docker_image_build_curr_data \
	docker_image_build_curr_stats \
	docker_image_build_curr_object \
	docker_image_build_curr_users \
	docker_image_build_curr_receiver \
	docker_image_build_curr_companies \
	docker_image_build_curr_tariffs \


rebuild_protobuf: 
	python3 -m grpc_tools.protoc -I./protobuf/ ./protobuf/proto/*.proto --python_out=./depends/python/ --grpc_python_out=./depends/python/

kubernetes_buildnload_all: \
	kubernetes_buildnload_data \
	kubernetes_buildnload_stats \
	kubernetes_buildnload_users \
	kubernetes_buildnload_object \
	kubernetes_buildnload_gateway \
	kubernetes_buildnload_companies \
	kubernetes_buildnload_tariffs \

# устанавливаем dns
kubernetes_install_dns:
	kubectl --namespace=kube-system scale deployment kube-dns --replicas=$(DNSREPLICAS)

# устанавливаем mongo replica set:
helm_install_mongo:
	helm install --name mongodb --set replicas=1 stable/mongodb-replicaset

# NOTES:
# PostgreSQL can be accessed via port 5432 on the following DNS name from within your cluster:
# postgresql.default.svc.cluster.local

# To get your user password run:

#     PGPASSWORD=$(kubectl get secret --namespace default postgresql -o jsonpath="{.data.postgres-password}" | base64 --decode; echo)

# To connect to your database run the following command (using the env variable from above):

#    kubectl run --namespace default postgresql-client --restart=Never --rm --tty -i --image postgres \
#    --env "PGPASSWORD=$PGPASSWORD" \
#    --command -- psql -U user \
#    -h postgresql postgres



# To connect to your database directly from outside the K8s cluster:
#      PGHOST=127.0.0.1
#      PGPORT=5432

#      # Execute the following commands to route the connection:
#      export POD_NAME=$(kubectl get pods --namespace default -l "app=postgresql" -o jsonpath="{.items[0].metadata.name}")
#      kubectl port-forward --namespace default $POD_NAME 5432:5432

# устанавливаем postgresql:
helm_install_postgresql:
	helm install --name postgresql stable/postgresql --set postgresUser=user,postgresPassword=user

# echo URL : http://127.0.0.1:15672
# kubectl port-forward rabbitmq-0  --namespace default 5672:5672 15672:15672
# устанавливаем rabbitmq 
helm_install_rabbitmq:
	helm install --name rabbitmq --set rabbitmq.username=user,rabbitmq.password=user,persistence.enabled=false,rbacEnabled=true stable/rabbitmq 