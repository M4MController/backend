PIDFILE= $(PIDDIR)/gateway.pid
LOGFILE= $(LOGDIR)/gateway.log

start:
	( \
		. venv/bin/activate; \
		PYTHONPATH=$(PYTHONPATH) FLASK_APP=gateway/app.py nohup python3 -m flask run  > $(LOGFILE) 2>&1 & echo $$!> $(PIDFILE); \
	)


run_test:
	( \
		. venv/bin/activate; \
		PYTHONPATH=$(PYTHONPATH) python3 run_test.py; \
	)
stop:
	cat $(PIDFILE) | xargs kill