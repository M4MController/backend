from flask import Flask
from flask_restful import Api
from gateway.resources.user import UserInfo
from gateway.resources.controller import GetUserControllers, GetControllerSensors, GetControllerStats
from gateway.resources.sensor import GetSensorData, GetSensorStats
# для того чтобы хорошо генерировались импорты сгенерированных файлов делается 
import proto.data_pb2_grpc
import proto.data_pb2
import proto.stats_pb2_grpc
import proto.stats_pb2
import grpc

app = Flask(__name__)
api = Api(app)

stats = grpc.insecure_channel('stats-service:5000')
data = grpc.insecure_channel('data-service:5000')

args = {'stats': stats, 'data': data}

api.add_resource(UserInfo, '/user/user_info', resource_class_kwargs=args)
api.add_resource(GetUserControllers, '/controller/get_user_controllers', resource_class_kwargs=args)
api.add_resource(GetControllerSensors, '/controller/<int:controller_id>/get_sensors', resource_class_kwargs=args)
api.add_resource(GetControllerStats, '/controller/<int:controller_id>/get_controller_stats', resource_class_kwargs=args)
api.add_resource(GetSensorStats, '/sensor/<int:sensor_id>/view_stats', resource_class_kwargs=args)
api.add_resource(GetSensorData, '/sensor/<int:sensor_id>/get_data', resource_class_kwargs=args)