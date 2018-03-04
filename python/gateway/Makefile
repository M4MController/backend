PIDFILE= gateway.pid
LOGFILE= gateway.log

prepare_generation:
	mkdir ./buf/
	mkdir ./buf/gateway/
	cp -r ../../protobuf/* ./buf/gateway/

clean_buffer:
	rm -rf ./buf


data_client:
	python3 -m grpc_tools.protoc -I./buf/ ./buf/gateway/data/data.proto --python_out=. --grpc_python_out=.

stats_client:
	python3 -m grpc_tools.protoc -I./buf/ ./buf/gateway/stats/stats.proto --python_out=. --grpc_python_out=.

generate_clients: \
	prepare_generation \
	data_client \
	stats_client \
	clean_buffer

start:
	( \
		. gateway/venv/bin/activate; \
		FLASK_APP=gateway/app.py nohup python3 -m flask run  > $(LOGFILE) 2>&1 & echo $$!> $(PIDFILE); \
	)

stop:
	cat $(PIDFILE) | xargs kill