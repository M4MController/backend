from flask import Flask
from flask_restful import Api
import gateway.resources.user as user 
import gateway.resources.controller as controller
import gateway.resources.sensor as sensor 
import gateway.resources.object as objects
import gateway.resources_v2.object as objectsv2
import gateway.resources_v2.controller as controllerv2
import gateway.resources_v2.user as userv2
import gateway.resources_v2.sensor as sensorv2
# для того чтобы хорошо генерировались импорты сгенерированных файлов делается 
from proto import data_pb2_grpc
from proto import data_pb2
from proto import stats_pb2_grpc
from proto import stats_pb2
import grpc

app = Flask(__name__)
api = Api(app)

stats = grpc.insecure_channel('stats-service:5000')
data = grpc.insecure_channel('data-service:5000')
objs = grpc.insecure_channel('object-service:5000')
userch = grpc.insecure_channel('users-service:5000')

args = {'stats': stats, 'data': data, 'object': objs, 'user': userch}

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
api.add_resource(sensor.GetSensorDataLimited, '/sensor/<int:sensor_id>/get_data', resource_class_kwargs=args)
api.add_resource(sensor.GetUserSensors, '/sensor/get_user_sensors', resource_class_kwargs=args)

# V2 мать его (лучшеб в отдельном приложении, потом надо переделать вместе с v2 аpi впринципе)
api.add_resource(controllerv2.Relations, '/v2/controller/<int:_id>/relations', endpoint='contrRelations', resource_class_kwargs=args)
api.add_resource(objectsv2.Relations, '/v2/object/<int:_id>/relations', endpoint='objectRelations',resource_class_kwargs=args)
api.add_resource(userv2.Relations, '/v2/user/relations', endpoint='userRelations', resource_class_kwargs=args)
api.add_resource(sensor.GetSensorDataPeriod, '/v2/sensor/<int:sensor_id>/get_data_period', resource_class_kwargs=args)


api.add_resource(objectsv2.Object, '/v2/object', '/v2/object/<int:_id>', endpoint='object', resource_class_kwargs=args)
api.add_resource(controllerv2.Controller, '/v2/controller', '/v2/controller/<int:_id>', endpoint='controller', resource_class_kwargs=args)
api.add_resource(controllerv2.ControllerActivate, '/v2/controller/<int:controller_id>/activate', endpoint='controller activate', resource_class_kwargs=args)

api.add_resource(sensorv2.Sensor, '/v2/sensor', '/v2/sensor/<int:_id>', endpoint='sensor create', resource_class_kwargs=args)
# Добавим ручки для добавления сенсоров и контроллеров