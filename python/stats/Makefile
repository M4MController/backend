PIDFILE= $(PIDDIR)/stats.pid
LOGFILE= $(LOGDIR)/stats.log

start:
	( \
		. venv/bin/activate; \
		nohup python3 stats/app.py > $(LOGFILE) 2>&1 & echo $$!> $(PIDFILE); \
	)

stop:
	cat $(PIDFILE) | xargs kill