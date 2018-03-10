from marshmallow import Schema, fields

from app.data_broker import data_broker
from app.resource import MethodHandler
from app.exceptions import (
    ControllerNotFoundException,
    SensorNotFoundException,
)


class Sensor(MethodHandler):
    MODULE = 'sensor'


class SetStatus(Sensor):
    METHOD = 'setStatus'

    class Schema(Schema):
        controller_mac = fields.Str(required=True)
        sensor_id = fields.Int(required=True)
        error_message = fields.Str()

    def method(self, data):
        # todo: remove the stub
        controller_mac = data['controller_mac']
        sensor_id = data['sensor_id']

        if controller_mac == '404':
            raise ControllerNotFoundException()
        if sensor_id == 404:
            raise SensorNotFoundException()

        return {'ok': True}


class AddRecord(Sensor):
    METHOD = 'addRecord'

    class Schema(Schema):
        controller_mac = fields.Str(required=True)
        sensor_id = fields.Int(required=True)
        value = fields.Int(required=True)
        timestamp = fields.DateTime('%Y-%m-%dT%H:%M:%S', required=True)

    def method(self, data):
        # todo: remove the stub
        data_broker.send_sensor_data(data)

        return {'ok': True}


def register_sensor_routes(app):
    SetStatus.register(app)
    AddRecord.register(app)
