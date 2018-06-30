from flask_restful import Resource
from flask_restful import reqparse
from flask import request
from gateway.views.errors import InvalidRequest
from gateway.views.errors import NotFound
from gateway.views.objects_info import UserInfo
from gateway.views_v2.objects_lvl import ObjectInfo
from gateway.views_v2.objects_lvl import ControllerInfo
from gateway.views_v2.objects_lvl import SensorInfo
from gateway.views_v2.objects_lvl import ObjList
from gateway.views_v2.objects_lvl import Listed
from proto import objects_pb2_grpc
from proto import objects_pb2
from proto import data_pb2_grpc
from proto import data_pb2
from proto import stats_pb2_grpc
from proto import stats_pb2
from proto import utils_pb2
import datetime
import base64
import time
import logging

log = logging.getLogger("flask.app")


#TODO: отрефакторить это чтобы избавиться от копипасты
class Relations(Resource):
    def __init__(self, **kwargs):
        self.data_chan = kwargs['data']
        self.stats_chan = kwargs['stats']
        self.object = kwargs['object']

    @staticmethod
    def collect_user_relations(rsp, data_chan):
        from gateway.resources_v2.object import Relations as ObjRelations
        controllers = []
        sensors = []
        for i in rsp.objects:
            ctr, ssr = ObjRelations.collect_object_relations(i, data_chan)
            controllers += ctr
            sensors += ssr
        return [ObjRelations.collect_object_info(i) for i in rsp.objects], controllers, sensors
    
    def get(self):
        stub = objects_pb2_grpc.ObjectServiceStub(self.object)
        include = request.args.getlist("include")
        log.info("some shitty log {}".format(include))
        uu = utils_pb2.UserId(user_id=1)
        try:
            rsp = stub.GetUsersInfo(uu)
        except Exception as e: 
            log.error("Error handling {}".format(str(e)))
            return NotFound("Not found error").get_message()
        objects, controllers, sensors = Relations.collect_user_relations(rsp, self.data_chan)

        objects=Listed(objects)
        controllers=Listed(controllers)
        sensors=Listed(sensors)

        kwargs = {}
        if include:
            if 'objects' in include:
                kwargs['objects']=objects
            if 'controllers' in include:
                kwargs['controllers']=controllers
            if 'sensors' in include:
                kwargs['sensors']=sensors
        else:
            kwargs=dict(objects=objects, controllers=controllers, sensors=sensors)
        return ObjList(**kwargs).get_message()