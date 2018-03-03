from flask import Flask
from flask_restful import Api
from gateway.resources.user import UserInfo
from gateway.resources.controller import GetUserControllers, GetControllerSensors, GetControllerStats
from gateway.resources.sensor import GetSensorData, GetSensorStats

app = Flask(__name__)
api = Api(app)

api.add_resource(UserInfo, '/user/user_info',)
api.add_resource(GetUserControllers, '/controller/get_user_controllers',)
api.add_resource(GetControllerSensors, '/controller/<int:controller_id>/get_sensors',)
api.add_resource(GetControllerStats, '/controller/<int:controller_id>/get_controller_stats',)
api.add_resource(GetSensorData, '/sensor/<int:sensor_id>/view_stats',)
api.add_resource(GetSensorStats, '/sensor/<int:sensor_id>/get_data',)