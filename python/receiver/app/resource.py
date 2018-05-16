from flask import request
from flask.views import MethodView as _MethodView
from flask_json import JsonError, json_response
from marshmallow import ValidationError
import logging

from .exceptions import (
    InternalErrorException,
    NotImplementedException,
    InvalidAgrumentsException,
)

log = logging.getLogger("flask.app")

class MethodView(_MethodView):
    def dispatch_request(self, *args, **kwargs):
        try:
            return super(MethodView, self).dispatch_request(*args, **kwargs)
        except Exception as e:
            if not isinstance(e, JsonError):
                e = InternalErrorException("{} {}".format(str(type(e)), str(e)))
            raise e


# inspired by vk api
class MethodHandler(MethodView):
    #MODULE = None
    #METHOD = None
    #__schema = None
    #class Schema:
    #    pass

    def method(self, data):
        raise NotImplementedException('Method is not implemented')

    def post(self):
        data = request.get_json(force=True)
        log.info(data)
        json_data = self._parse_args(data)
        return json_response(data=self.method(json_data))

    @classmethod
    def _parse_args(cls, data):
        if cls.__schema:
            log.info("data before is {}".format(str(data)))
            log.info("data type before is {}".format(str(type(data))))
            data, errors = cls.__schema.loads(data)
            log.error(errors)
            log.info("data is {}".format(str(data)))
            log.info("data type is {}".format(str(type(data))))
            if errors:
                raise InvalidAgrumentsException(errors)
            if data is None:
                raise InvalidAgrumentsException("data is empty")
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
