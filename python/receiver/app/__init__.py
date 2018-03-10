from flask import Flask
from flask_json import FlaskJSON

from .resources import register_routes


def create_api():
    app = Flask(__name__)
    FlaskJSON(app)
    register_routes(app)

    return app
