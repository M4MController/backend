from marshmallow import Schema, fields

from app.resource import MethodHandler
from app.exceptions import ControllerNotFoundException


class Controller(MethodHandler):
    MODULE = 'controller'


class SetOnline(Controller):
    METHOD = 'setOnline'

    class Schema(Schema):
        controller_mac = fields.Str(required=True)

    def method(self, data):
        # todo: remove the stub
        controller_mac = data['controller_mac']
        if controller_mac == '404':
            raise ControllerNotFoundException()

        return {'ok': True}


def register_controller_routes(app):
    SetOnline.register(app)
