LOGDIR= $(realpath ./logs/)
PIDDIR= $(realpath ./pids/)

export

start_data:
	$(MAKE) -C  python/data start

start_gateway:
	$(MAKE) -C  python/gateway start

start_stats:
	$(MAKE) -C  python/stats start

-stop_data:
	$(MAKE) -C  python/data stop

-stop_gateway:
	$(MAKE) -C  python/gateway stop

-stop_stats:
	$(MAKE) -C  python/stats stop


start_all: \
	start_data \
	start_stats \
	start_gateway \

stop_all: \
	-stop_data \
	-stop_stats \
	-stop_gateway \

build_data:
	$(MAKE) -C  python/data generate_proto

build_gateway:
	$(MAKE) -C  python/gateway generate_proto

build_stats:
	$(MAKE) -C  python/stats generate_proto

build_all: \
	build_data \
	build_stats \
	build_gateway \
