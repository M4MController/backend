PIDFILE= $(PIDDIR)/data.pid
LOGFILE= $(LOGDIR)/data.log

start:
	( \
		. venv/bin/activate; \
		nohup python3 data/app.py > $(LOGFILE) 2>&1 & echo $$!> $(PIDFILE); \
	)

stop:
	cat $(PIDFILE) | xargs kill