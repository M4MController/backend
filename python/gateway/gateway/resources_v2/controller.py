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

class Relations(Resource):
    def __init__(self, **kwargs):
        self.data_chan = kwargs['data']
        self.stats_chan = kwargs['stats']
        self.object = kwargs['object']

    @staticmethod
    def collect_controller_info(cntrlr):
        from gateway.resources_v2.sensor import Relations as SensorRel
        ctr = ControllerInfo(id=cntrlr.id.controller_id,
                                object_id=cntrlr.object_id.object_id,
                                name=cntrlr.name,
                                meta=cntrlr.meta,
                                activation_date=None,
                                status=cntrlr.status,
                                mac=cntrlr.mac,
                                controller_type=cntrlr.controller_type,
                                deactivation_date=None)
        if cntrlr.HasField("deactivation_date_val"):
                ctr.deactivation_date = cntrlr.deactivation_date_val
        if cntrlr.HasField("activation_date_val"):
                ctr.activation_date = cntrlr.activation_date_val
        return ctr

    @staticmethod
    def collect_controller_relations(cntrlr, data_chan):
        from gateway.resources_v2.sensor import Relations as SensorRel
        return [SensorRel.collect_sensor_info(i, data_chan) for i in cntrlr.sensors]

    def get(self, _id):
        stub = objects_pb2_grpc.ObjectServiceStub(self.object)
        include = request.args.getlist("include")
        log.info("some shitty log {}".format(include))
        uu = utils_pb2.ControllerId(controller_id=_id)
        try:
            rsp = stub.GetControllerInfo(uu)
        except Exception as e: 
            log.error("Error handling {}".format(str(e)))
            return NotFound("Not found error").get_message()
        sensors = Relations.collect_controller_relations(rsp, self.data_chan)
        sensors = Listed(sensors)
        kwargs = {}
        if include:
            if 'sensors' in include:
                kwargs['sensors'] = sensors
        else:
            kwargs = dict(sensors=sensors)
        return ObjList(**kwargs).get_message()