import jwt
from flask_restful import reqparse
import functools
from gateway.views.errors import NotAuthorized
import logging

SECURE_KEY = "REMOVE_ME_PLEASE"

log = logging.getLogger("flask.app")

def auth_wrapper(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        parser = reqparse.RequestParser()
        parser.add_argument("token")
        try:
            url_args = parser.parse_args()
            raw_token = url_args["token"]
            token = jwt.decode(raw_token, SECURE_KEY, algorithms=['HS256'])
        except Exception as e:
            log.error("Error, while checking auth token {}".format(str(e)))
            return NotAuthorized("Not Authorized").get_message()
        if token["user_id"] != 1:
            return NotAuthorized().get_message()
        kwargs["token"] = token
        return func(*args, **kwargs)
    return wrapper

def auth_optional_wrapper(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        parser = reqparse.RequestParser()
        parser.add_argument("auth_token")
        try:
            url_args = parser.parse_args()
            raw_token = url_args["auth_token"]
            token = jwt.decode(raw_token, SECURE_KEY, algorithms=['HS256'])
        except Exception as e:
            log.info("Error, while checking optional auth token {}".format(str(e)))
        kwargs["auth_token"] = token
        return func(*args, **kwargs)
    return wrapper
