from marshmallow import Schema, fields, post_load
import marshmallow
from flask import request
from flask import make_response
import logging
import json
import pika

log = logging.getLogger("flask.app")

class DataSchema(Schema):
    controller_mac = fields.String()
    sensor_id = fields.Integer()
    value = fields.Raw()
    hash = fields.String()
    timestamp = fields.DateTime(format="%Y-%m-%dT%H:%M:%S")

data_schema = DataSchema()

def collect_data(dependencies):
    data = request.get_json(force=True)
    loaded, errors = data_schema.load(data)
    log.debug("Got data: {}".format(json.dumps(data, indent=4)))
    log.debug("Got loaded: {}".format(print(loaded)))
    if errors:
        log.debug("Got errors: {}".format(json.dumps(errors, indent=4)))
        return {'ok': False, 'errors': errors}, 400
    try:
        dependencies.data_broker.send_sensor_data(loaded)
    except pika.exceptions.ConnectionClosed as e:
        log.error(str(e))
        return {'ok': False, 'errors': ["Failed to write data to rabbitmq!"]}, 500
    return {'ok': True}

def set_status(dependencies):
    return {'ok': True}
