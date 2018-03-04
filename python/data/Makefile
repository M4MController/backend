PIDFILE= data.pid
LOGFILE= data.log

generate_proto:  
	python3 -m grpc_tools.protoc -I../../protobuf/data ../../protobuf/data/data.proto --python_out=data/ --grpc_python_out=data/

start:
	nohup python3 data/app.py > $(LOGFILE) 2>&1 & echo $$!> $(PIDFILE)

stop:
	cat $(PIDFILE) | xargs kill