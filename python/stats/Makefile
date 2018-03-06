PIDFILE= $(PIDDIR)/stats.pid
LOGFILE= $(LOGDIR)/stats.log

start:
	nohup python3 stats/app.py > $(LOGFILE) 2>&1 & echo $$!> $(PIDFILE)

stop:
	cat $(PIDFILE) | xargs kill