from .controller import register_controller_routes
from .sensor import register_sensor_routes


def register_routes(app):
    register_controller_routes(app)
    register_sensor_routes(app)
