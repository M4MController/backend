PIDFILE= $(PIDDIR)/stats.pid
LOGFILE= $(LOGDIR)/stats.log

generate_proto:  
	python3 -m grpc_tools.protoc -I../../protobuf/stats ../../protobuf/stats/stats.proto --python_out=stats/ --grpc_python_out=stats/

start:
	nohup python3 stats/app.py > $(LOGFILE) 2>&1 & echo $$!> $(PIDFILE)

stop:
	cat $(PIDFILE) | xargs kill