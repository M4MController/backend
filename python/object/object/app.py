import models.models as models
import protobuilder as pbufbuilder
import proto.objects_pb2_grpc as objects_pb2_grpc
import proto.objects_pb2 as objects_pb2
import proto.utils_pb2 as utils_pb2
from google.protobuf.json_format import MessageToJson
from concurrent import futures
from collections import defaultdict
import grpc
import time
import config
import logging
import psycopg2
import argparse


class ObjectServiceServ(objects_pb2_grpc.ObjectServiceServicer):
    def __init__(self, model):
        self.__model = model

    def GetUsersInfo(self, request, context):
        user_id = request.user_id
        logging.info("getting user info user id = {}".format(user_id))
        data = self.__model.get_user_info(user_id)
        # TODO: IF NO DATA - error
        user_info = pbufbuilder.build_user_pb(list(data["users"].values())[0])
        logging.debug("result info")
        logging.debug(MessageToJson(user_info))
        return user_info

    def GetControllerInfo(self, request, context):
        logging.info("starting to process")
        controller_id = request.controller_id
        logging.info("getting controller info controller id = {}".format(controller_id))
        data = self.__model.get_controller_info(controller_id)
        # TODO: IF NO DATA - error
        controller_info = pbufbuilder.build_controller_pb(list(data["controllers"].values())[0])
        logging.debug("result info")
        logging.debug(MessageToJson(controller_info))
        return controller_info

    def GetSensorInfo(self, request, context):
        logging.info("starting to process")
        sensor_id = request.sensor_id
        logging.info("getting sensor info sensor id = {}".format(sensor_id))
        data = self.__model.get_sensor_info(sensor_id)
        # TODO: IF NO DATA - error
        sensor_info = pbufbuilder.build_sensor_pb(list(data["sensors"].values())[0])
        logging.debug("result info")
        logging.debug(MessageToJson(sensor_info))
        return sensor_info

    def GetObjectInfo(self, request, context):
        logging.info("starting to process")
        object_id = request.object_id
        logging.info("getting object info object id = {}".format(object_id))
        data = self.__model.get_object_info(object_id)
        # TODO: IF NO DATA - error
        object_info = pbufbuilder.build_object_pb(list(data["objects"].values())[0])
        logging.debug("result info")
        logging.debug(MessageToJson(object_info))
        return object_info

    def CreateObject(self, request, context):
        logging.info("starting to process")
        logging.info("creating object")
        user_id = 1
        data = self.__model.create_object(user_id, request.name, request.address, request.meta)
        # TODO: IF NO DATA - error
        object_info = pbufbuilder.build_object_pb(list(data["objects"].values())[0])
        logging.debug("result info")
        logging.debug(MessageToJson(object_info))
        return object_info

    def CreateController(self, request, context):
        logging.info("starting to process")
        logging.info("creating controller")
        data = self.__model.create_controller(None, None, request.meta, request.controller_type, request.mac)
        # TODO: IF NO DATA - error
        controller_info = pbufbuilder.build_controller_pb(list(data["controllers"].values())[0])
        logging.debug("result info")
        logging.debug(MessageToJson(controller_info))
        return controller_info

    def CreateSensor(self, request, context):
        logging.info("starting to process")
        logging.info("creating sensor")
        data = self.__model.create_sensor(request.name,
                                          request.meta,
                                          request.controller_id,
                                          request.sensor_type,
                                          request.company)
        # TODO: IF NO DATA - error
        sensor_info = pbufbuilder.build_sensor_pb(list(data["sensors"].values())[0])
        logging.debug("result info")
        logging.debug(MessageToJson(sensor_info))
        return sensor_info

    def ActivateController(self, request, context):
        logging.info("starting to process")
        logging.info("activate controller")
        data = self.__model.activate_controller(request.controller_id.controller_id,
                                                request.name,
                                                request.meta,
                                                request.object_id.object_id,
                                                request.status)
        # TODO: IF NO DATA - error
        controller_info = pbufbuilder.build_controller_pb(list(data["sensors"].values())[0])
        logging.debug("result info")
        logging.debug(MessageToJson(controller_info))
        return controller_info

    def DeleteObject(self, request, context):
        logging.info("starting to process")
        logging.info("delete object")
        data = self.__model.delete_object(request.object_id.object_id)
        # TODO: IF NO DATA - error
        logging.debug("result info")
        logging.info(data)
        return utils_pb2.Void()
    
    def DeleteSensor(self, request, context):
        logging.info("starting to process")
        logging.info("delete sensor")
        data = self.__model.delete_sensor(request.sensor_id.sensor_id)
        # TODO: IF NO DATA - error
        logging.debug("result info")
        logging.info(data)
        return utils_pb2.Void()

    def DeleteController(self, request, context):
        logging.info("starting to process")
        logging.info("delete controller")
        data = self.__model.delete_controller(request.sensor_id.sensor_id)
        # TODO: IF NO DATA - error
        logging.debug("result info")
        logging.info(data)
        return utils_pb2.Void()

    def DeactivateController(self, request, context):
        logging.info("starting to process")
        logging.info("activate controller")
        data = self.__model.deactivate_controller(request.controller_id.controller_id)
        # TODO: IF NO DATA - error
        controller_info = pbufbuilder.build_controller_pb(list(data["sensors"].values())[0])
        logging.debug("result info")
        logging.debug(MessageToJson(controller_info))
        return controller_info


def main():
    parser = argparse.ArgumentParser(description="""
        Service to store objects
    """)
    parser.add_argument('--config', help='configuration file', default=None)
    args = parser.parse_args()
    confs = config.ConfigManager()
    if args.config is not None:
        with open(args.config, "r") as conffile:
            confs.load_from_file(conffile)
    logging.basicConfig(level=getattr(logging, confs["LogLevel"].upper()))
    address = confs["address"]
    logging.info("Starting grpc server with address :{}".format(address))
    logging.info("Starting grpc server {} workers".format(confs["workers"]))
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=confs["workers"]))
    dbconf = confs["database"]
    logging.info("Connecting to {} with username: {}, host: {}".format(dbconf["database"],
                                                                       dbconf["username"],
                                                                       dbconf["host"]))
    database = models.Model(dbconf)
    objects_pb2_grpc.add_ObjectServiceServicer_to_server(ObjectServiceServ(database), server)
    server.add_insecure_port(address)
    server.start()
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        logging.info("Stop signal got")
        server.stop(0)

if __name__ == '__main__':
    main()
