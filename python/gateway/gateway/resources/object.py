from flask_restful import Resource
from flask_restful import reqparse
from flask import request
from gateway.views.errors import InvalidRequest
from gateway.views.errors import NotFound
from gateway.views.objects_lvl import Listed
from gateway.views.objects_lvl import ObjectInfo
from gateway.views.objects_lvl import ControllerInfo
from gateway.views.objects_lvl import SensorInfo
from gateway.views.change import Posted
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

class AddObject(Resource):
    def __init__(self, **kwargs):
        self.stats_chan = kwargs['stats']

    def post(self):
        body = request.get_json(force=True)
        log.debug("come this shit {}".format(body))
        name = body['name']
        adres = body['adres']
        return Posted().get_message()

class GetObjectStats(Resource):
    def __init__(self, **kwargs):
        self.stats_chan = kwargs['stats']

    def get(self, object_id):
        stats = {
        "code": 0,
        "msg": {
            "month": 0,
            "prev_month": 0,
            "prev_year": 0
        },
        }
        stub = stats_pb2_grpc.StatsServiceStub(self.stats_chan)
        id = utils_pb2.ObjectId(object_id=object_id)
        rsp = stub.GetObjectStat(id)
        stats["msg"]["month"] = rsp.current_month
        stats["msg"]["prev_month"] = rsp.prev_year_month
        stats["msg"]["prev_year"] = rsp.prev_year_average
        return stats, 200


class GetUserObjects(Resource):
    def __init__(self, **kwargs):
        self.data_chan = kwargs['data']
        self.stats_chan = kwargs['stats']
        self.object = kwargs['object']

    def get(self):
        stub = objects_pb2_grpc.ObjectServiceStub(self.object)
        log.info("some shitty log")
        uu = utils_pb2.UserId(user_id=1)
        try:
            rsp = stub.GetUsersInfo(uu)
        except Exception as e: 
            log.error("Error handling {}".format(str(e)))
            return NotFound("Not found error").get_message()
        def controller(cntrlr):
            def sensor(ssr):
                rs = SensorInfo(ssr.id,
                                ssr.name,
                                None,
                                None,
                                ssr.sensor_type,
                                ssr.company)
                if ssr.HasField("deactivation_date_val"):
                    rs.deactivation_date = ssr.deactivation_date_val
                if ssr.HasField("activation_date_val"):
                    rs.activation_date = ssr.activation_date_val
                return rs

            ctr = ControllerInfo(cntrlr.id,
                                cntrlr.name,
                                cntrlr.meta,
                                None,
                                cntrlr.status,
                                cntrlr.mac,
                                cntrlr.controller_type,
                                None,
                                [sensor(i) for i in cntrlr.sensors])
            if cntrlr.HasField("deactivation_date_val"):
                    ctr.deactivation_date = cntrlr.deactivation_date_val
            if cntrlr.HasField("activation_date_val"):
                    ctr.activation_date = cntrlr.activation_date_val
            return ctr
        def obct(rsp):
            uo = ObjectInfo(
                rsp.id,
                rsp.name,
                rsp.adres,
                []
            )
            return uo
        uo = Listed(
            [obct(i) for i in rsp.objects]
        )
        return uo.get_message()

class GetObjectControllers(Resource):
    def __init__(self, **kwargs):
        self.data_chan = kwargs['data']
        self.stats_chan = kwargs['stats']
        self.object = kwargs['object']
        
    def get(self, object_id):
        stub = objects_pb2_grpc.ObjectServiceStub(self.object)
        log.info("some shitty log")
        uu = utils_pb2.ObjectId(object_id=object_id)
        try:
            rsp = stub.GetObjectInfo(uu)
        except Exception as e: 
            log.error("Error handling {}".format(str(e)))
            return NotFound("Not found error").get_message()
        def controller(cntrlr):
            def sensor(ssr):
                rs = SensorInfo(ssr.id,
                                ssr.name,
                                None,
                                None,
                                ssr.sensor_type,
                                ssr.company)
                if ssr.HasField("deactivation_date_val"):
                    rs.deactivation_date = ssr.deactivation_date_val
                if ssr.HasField("activation_date_val"):
                    rs.activation_date = ssr.activation_date_val
                return rs

            ctr = ControllerInfo(cntrlr.id,
                                cntrlr.name,
                                cntrlr.meta,
                                None,
                                cntrlr.status,
                                cntrlr.mac,
                                cntrlr.controller_type,
                                None,
                                [sensor(i) for i in cntrlr.sensors])
            if cntrlr.HasField("deactivation_date_val"):
                    ctr.deactivation_date = cntrlr.deactivation_date_val
            if cntrlr.HasField("activation_date_val"):
                    ctr.activation_date = cntrlr.activation_date_val
            return ctr

        uo = Listed(
            [controller(i) for i in rsp.controllers]
        )
        return uo.get_message()