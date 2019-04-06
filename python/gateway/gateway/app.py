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
import argparse
import config
import os
# Добавим ручки для добавления сенсоров и контроллеров


def build_app(confs):
    app = Flask(__name__)
    api = Api(app)
    stats = grpc.insecure_channel(confs["stats"])
    data = grpc.insecure_channel(confs["data"])
    objs = grpc.insecure_channel(confs["objs"])
    userch = grpc.insecure_channel(confs["userch"])

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
    return app

def build_config(conf_path):
    confs = config.ConfigManager()
    if conf_path is not None:
        with open(conf_path, "r") as conffile:
            confs.load_from_file(conffile)
    return confs

def gunicorn_entry(conf_path):
    return build_app(build_config(conf_path))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="""
        Service to store objects
    """)
    parser.add_argument('--config', help='configuration file', default=None)
    args = parser.parse_args()
    conf = args.config
    confs = build_config(conf)
    app = build_app(confs)
    app.run(
        debug=True,
        host=confs["address"],
        port=confs["port"],
    )
