CURRENT_NAME = gateway
NAME := $(CURRENT_NAME)

%$(CURRENT_NAME) : DIRECTORY := $(patsubst %/,%,$(dir $(abspath $(lastword $(MAKEFILE_LIST)))))
%$(CURRENT_NAME) : NAME := CURRENT_NAME

build_$(NAME):
	$(MAKE) -C $(DIRECTORY) build

start_$(NAME):
	$(MAKE) -C $(DIRECTORY) start

stop_$(NAME):
	-$(MAKE) -C $(DIRECTORY) stop

docker_image_build_$(NAME):
	$(MAKE) -C $(DIRECTORY) docker_build

docker_image_build_$(NAME)_curr:
	$(MAKE) -C $(DIRECTORY) docker_build_curr

kubernetes_service_$(NAME):
	$(MAKE) -C $(DIRECTORY) kubernetes_service

kubernetes_deployment_$(NAME):
	$(MAKE) -C $(DIRECTORY) kubernetes_deployment
	
kubernetes_deployment_remove_$(NAME):
	$(MAKE) -C $(DIRECTORY) kubernetes_deployment_remove

kubernetes_service_remove_$(NAME):
	$(MAKE) -C $(DIRECTORY) kubernetes_service_remove

kubernetes_buildnload_$(NAME):
	$(MAKE) -C $(DIRECTORY) kubernetes_buildnload

docker_clean_$(NAME):
	-$(MAKE) -C $(DIRECTORY) docker_cleanup