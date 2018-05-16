from flask import Flask
from flask_json import FlaskJSON
import logging
from .resources import register_routes


def create_api():
    app = Flask(__name__)
    logging.basicConfig(level='DEBUG')
    print(app.logger_name)
    FlaskJSON(app)
    register_routes(app)

    return app
