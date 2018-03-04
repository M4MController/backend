from flask import request
from flask.views import MethodView as _MethodView
from flask_json import JsonError, json_response
from marshmallow import ValidationError

from .exceptions import (
    InternalErrorException,
    NotImplementedException,
    InvalidAgrumentsException,
)


class MethodView(_MethodView):
    def dispatch_request(self, *args, **kwargs):
        try:
            return super(MethodView, self).dispatch_request(*args, **kwargs)
        except Exception as e:
            if not isinstance(e, JsonError):
                e = InternalErrorException()
            raise e


# inspired by vk api
class MethodHandler(MethodView):
    MODULE = None
    METHOD = None

    class Schema:
        pass

    def method(self, data):
        raise NotImplementedException('Method is not implemented')

    def post(self):
        json_data = request.get_json()
        self._parse_args(json_data)
        return json_response(data=self.method(json_data))

    @classmethod
    def _parse_args(cls, data):
        if cls.__schema:
            data, errors = cls.__schema.load(data)
            if errors:
                raise InvalidAgrumentsException(errors)
            return data
        return data

    @classmethod
    def register(cls, app):
        view_name = '_'.join([cls.MODULE, cls.METHOD])
        path_name = '/' + '.'.join([cls.MODULE, cls.METHOD])
        app.add_url_rule(path_name,
                         view_name,
                         cls.as_view(view_name),
                         methods=['POST'],
                         )

        cls.__schema = cls.Schema()

    __schema = None
