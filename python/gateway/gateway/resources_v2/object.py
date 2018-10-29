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
from gateway.views_v2.payments import ObjectPayments
from gateway.resources_v2.input.object import object_create_schema
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

class Relations(Resource):
    def __init__(self, **kwargs):
        self.data_chan = kwargs['data']
        self.stats_chan = kwargs['stats']
        self.object = kwargs['object']

    @staticmethod
    def collect_object_info(rsp):
        uo = ObjectInfo(
                rsp.id.object_id,
                rsp.user_id.user_id,
                rsp.name,
                rsp.address,
                ObjectPayments(
                    current_month=5489,
                    prev_year=5427,
                    year_avg=5316
                )
            )
        return uo

    @staticmethod
    def collect_object_relations(rsp, data_chan, stats_chan):
        from gateway.resources_v2.controller import Relations as ContrRelations
        sensors = []
        for i in rsp.controllers:
            sensors += ContrRelations.collect_controller_relations(i, data_chan, stats_chan)
        return [ContrRelations.collect_controller_info(i) for i in rsp.controllers], sensors

    def get(self, _id):
        stub = objects_pb2_grpc.ObjectServiceStub(self.object)
        include = request.args.getlist("include")
        log.info("some shitty log {}".format(include))
        uu = utils_pb2.ObjectId(object_id=int(_id))
        try:
            rsp = stub.GetObjectInfo(uu)
        except Exception as e: 
            log.error("Error handling {}".format(str(e)))
            return NotFound("Not found error").get_message()

        controllers, sensors = Relations.collect_object_relations(rsp, self.data_chan, self.stats_chan)
        controllers = Listed(controllers)
        sensors = Listed(sensors)

        kwargs = {}
        if include:
            if 'controllers' in include:
                kwargs['controllers'] = controllers
            
            if 'sensors' in include:
                kwargs['sensors'] = sensors
        else:
            kwargs = dict(controllers=controllers, sensors=sensors)
        return ObjList(**kwargs).get_message()


class Object(Resource):
    def __init__(self, **kwargs):
        self.data_chan = kwargs['data']
        self.stats_chan = kwargs['stats']
        self.object = kwargs['object']

    def post(self):
        data = request.get_json()
        data_cleaned = object_create_schema.load(data)
        data_cleaned = data_cleaned.data
        stub = objects_pb2_grpc.ObjectServiceStub(self.object)
        uc = objects_pb2.ObjectCreate(
            name=data_cleaned["name"],
            address=data_cleaned["address"],
        )
        try:
            rsp = stub.CreateObject(uc)
        except Exception as e:
            log.error("Error handling {}".format(str(e)))
            return NotFound("Not found error").get_message()
        rsp = Relations.collect_object_info(rsp)
        return rsp.get_message()
