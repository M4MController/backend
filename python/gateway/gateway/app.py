from flask import Flask
from flask_restful import Api
import gateway.resources.user as user 
import gateway.resources.controller as controller
import gateway.resources.sensor as sensor 
import gateway.resources.object as objects
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

api.add_resource(user.SignIn, '/user/sign_in', resource_class_kwargs=args)
#api.add_resource(UserInfo, '/user/sign_up', resource_class_kwargs=args)
api.add_resource(objects.AddObject, '/object/register', resource_class_kwargs=args)
api.add_resource(controller.AddController, '/controller/register', resource_class_kwargs=args)
api.add_resource(sensor.AddSensor, '/sensor/register', resource_class_kwargs=args)
api.add_resource(objects.GetUserObjects, '/object/get_user_objects', resource_class_kwargs=args)
api.add_resource(objects.GetObjectControllers, '/object/<int:object_id>/get_object_controllers', resource_class_kwargs=args)
api.add_resource(objects.GetObjectStats, '/object/<int:object_id>/get_object_stats', resource_class_kwargs=args)
api.add_resource(user.UserInfo, '/user/user_info', resource_class_kwargs=args)
api.add_resource(controller.GetUserControllers, '/controller/get_user_controllers', resource_class_kwargs=args)
api.add_resource(controller.GetControllerSensors, '/controller/<int:controller_id>/get_sensors', resource_class_kwargs=args)
api.add_resource(controller.GetControllerStats, '/controller/<int:controller_id>/get_controller_stats', resource_class_kwargs=args)
api.add_resource(sensor.GetSensorStats, '/sensor/<int:sensor_id>/view_stats', resource_class_kwargs=args)
api.add_resource(sensor.GetSensorData, '/sensor/<int:sensor_id>/get_data', resource_class_kwargs=args)