import logging

log = logging.getLogger("flask.app")

def ping(dependencies):
    return {'ok': True}
