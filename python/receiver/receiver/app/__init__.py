from flask import Flask
from app import pinger
from app import controller
from app import sensor
import functools
import json
from flask import jsonify
from app.data_broker import data_broker
import logging

app = Flask(__name__, instance_relative_config=True)

def bicycle(handler, dependencies):
    @functools.wraps(handler)
    def handler_wrapped(*args, **kwargs):
        kwargs["dependencies"] = dependencies
        rsp = handler(*args, **kwargs)
        if isinstance(rsp, tuple):
            body, code = rsp
            rsp = jsonify(body)
            rsp.status_code = code
        else:
            rsp = jsonify(rsp)
        return rsp
    return handler_wrapped

class ServerContext:
    def __init__(self, broker):
        self.data_broker = broker

def create_app(config):
    print("1111111111")
    app.config.from_mapping(config)

    rmq_config = config["rabbitmq"]
    broker = data_broker.DataBroker(**rmq_config)
    context = ServerContext(broker)
    print("222222")
    app.add_url_rule("/ping", view_func=bicycle(pinger.ping, context), methods=["GET"])
    
    app.add_url_rule("/sensor.addRecord", view_func=bicycle(sensor.collect_data, context), methods=["POST"])
    
    app.add_url_rule("/sensor.setOnline", endpoint="sensorsetonline", view_func=bicycle(sensor.set_status, context), methods=["POST"])

    app.add_url_rule("/controller.setStatus", endpoint="controlleretonline", view_func=bicycle(controller.set_status, context), methods=["POST"])
    
    return app