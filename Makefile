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

start_object:
	-$(MAKE) -C  python/object start

start_users:
	-$(MAKE) -C  python/users start

start_receiver:
	$(MAKE) -C  python/receiver start

stop_data:
	-$(MAKE) -C  python/data stop

stop_gateway:
	-$(MAKE) -C  python/gateway stop

stop_stats:
	-$(MAKE) -C  python/stats stop

stop_object:
	-$(MAKE) -C  python/object stop

stop_users:
	-$(MAKE) -C  python/users stop

start_all: \
	start_data \
	start_stats \
	start_users \
	start_object \
	start_gateway \

stop_all: \
	stop_data \
	stop_stats \
	stop_users \
	stop_object \
	stop_gateway \

build_data:
	$(MAKE) -C  python/data build

build_gateway:
	$(MAKE) -C  python/gateway build

build_stats:
	$(MAKE) -C  python/stats build

build_object:
	$(MAKE) -C  python/object build

build_users:
	$(MAKE) -C  python/users build

build_all: \
	rebuild_protobuf \
	build_data \
	build_stats \
	build_users \
	build_object \
	build_gateway \


docker_clean_data:
	-$(MAKE) -C  python/data docker_cleanup

docker_clean_gateway:
	-$(MAKE) -C  python/gateway docker_cleanup

docker_clean_stats:
	-$(MAKE) -C  python/stats docker_cleanup

docker_clean_object:
	-$(MAKE) -C  python/object docker_cleanup

docker_clean_users:
	-$(MAKE) -C  python/users docker_cleanup

docker_clean_all: \
	docker_clean_data \
	docker_clean_stats \
	docker_clean_users \
	docker_clean_object \
	docker_clean_gateway \


# для работы с докером необходимо переключить контекст на minikube
# сделать это из makefile для родительского терминала без костылей 
# (я не уверен) нельзя, ткчт для работы с докером minikube надо ввести
# eval $(minikube docker-env)
# в текущем терминале

# выкатываем с тегом
docker_image_build_gateway:
	$(MAKE) -C  python/gateway docker_build

docker_image_build_data:
	$(MAKE) -C  python/data docker_build

docker_image_build_stats:
	$(MAKE) -C  python/stats docker_build

docker_image_build_receiver:
	$(MAKE) -C  python/receiver docker_build

docker_image_build_users:
	$(MAKE) -C  python/users docker_build

docker_image_build_object:
	$(MAKE) -C  python/object docker_build

docker_images_build: \
	docker_image_build_gateway \
	docker_image_build_data \
	docker_image_build_stats \
	docker_image_build_users \
	docker_image_build_object \
	docker_image_build_receiver

#выкатываем без перетеггирования 
docker_image_build_gateway_curr:
	$(MAKE) -C  python/gateway docker_build_curr

docker_image_build_data_curr:
	$(MAKE) -C  python/data docker_build_curr

docker_image_build_stats_curr:
	$(MAKE) -C  python/stats docker_build_curr

docker_image_build_receiver_curr:
	$(MAKE) -C  python/receiver docker_build_curr
	
docker_image_build_users_curr:
	$(MAKE) -C  python/users docker_build_curr

docker_image_build_object_curr:
	$(MAKE) -C  python/object docker_build_curr

docker_images_build_curr: \
	docker_image_build_gateway_curr \
	docker_image_build_data_curr \
	docker_image_build_stats_curr \
	docker_image_build_object_curr \
	docker_image_build_users_curr \
	docker_image_build_receiver_curr


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
	$(MAKE) -C  python/gateway kubernetes_buildnload


# receiver kubernetes
kubernetes_receiver_service:
	$(MAKE) -C  python/receiver kubernetes_service

kubernetes_receiver_deployment:
	$(MAKE) -C  python/receiver kubernetes_deployment
	
kubernetes_receiver_deployment_remove:
	$(MAKE) -C  python/receiver kubernetes_deployment_remove

kubernetes_receiver_service_remove:
	$(MAKE) -C  python/receiver kubernetes_service_remove

kubernetes_receiver_buildnload:
	$(MAKE) -C  python/receiver kubernetes_buildnload

# object kubernetes
kubernetes_object_service:
	$(MAKE) -C  python/object kubernetes_service

kubernetes_object_deployment:
	$(MAKE) -C  python/object kubernetes_deployment
	
kubernetes_object_deployment_remove:
	$(MAKE) -C  python/object kubernetes_deployment_remove

kubernetes_object_service_remove:
	$(MAKE) -C  python/object kubernetes_service_remove

kubernetes_object_buildnload:
	$(MAKE) -C  python/object kubernetes_buildnload

# users kubernetes
kubernetes_users_service:
	$(MAKE) -C  python/users kubernetes_service

kubernetes_users_deployment:
	$(MAKE) -C  python/users kubernetes_deployment
	
kubernetes_users_deployment_remove:
	$(MAKE) -C  python/users kubernetes_deployment_remove

kubernetes_users_service_remove:
	$(MAKE) -C  python/users kubernetes_service_remove

kubernetes_users_buildnload:
	$(MAKE) -C  python/users kubernetes_buildnload



kubernetes_all_buildnload: \
	kubernetes_data_buildnload \
	kubernetes_stats_buildnload \
	kubernetes_users_buildnload \
	kubernetes_object_buildnload \
	kubernetes_gateway_buildnload \

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