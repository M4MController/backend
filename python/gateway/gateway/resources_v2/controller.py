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
from gateway.views_v2.payments import ControllerPayments
from gateway.resources_v2.input.controller import controller_activate_schema
from gateway.resources_v2.input.controller import controller_create_schema
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
from gateway.auth.auth import auth_wrapper
import logging
from gateway.views.errors import NotAuthorized

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
                                payments=ControllerPayments(0, 0, 0),
                                deactivation_date=None)
        if cntrlr.HasField("deactivation_date_val"):
                ctr.deactivation_date = cntrlr.deactivation_date_val
        if cntrlr.HasField("activation_date_val"):
                ctr.activation_date = cntrlr.activation_date_val
        return ctr

    @staticmethod
    def collect_controller_relations(cntrlr, data_chan, stats_chan):
        from gateway.resources_v2.sensor import Relations as SensorRel
        return [SensorRel.collect_sensor_info(i, data_chan, stats_chan) for i in cntrlr.sensors]
    
    @auth_wrapper
    def get(self, _id, token):
        stub = objects_pb2_grpc.ObjectServiceStub(self.object)
        include = request.args.getlist("include")
        log.info("some shitty log {}".format(include))
        uu = utils_pb2.ControllerId(controller_id=_id)
        try:
            rsp = stub.GetControllerInfo(uu)
        except Exception as e: 
            log.error("Error handling {}".format(str(e)))
            return NotFound("Not found error").get_message()
        sensors = Relations.collect_controller_relations(rsp, self.data_chan, self.stats_chan)
        sensors = Listed(sensors)
        kwargs = {}
        if include:
            if 'sensors' in include:
                kwargs['sensors'] = sensors
        else:
            kwargs = dict(sensors=sensors)
        return ObjList(**kwargs).get_message()

class Controller(Resource):
    def __init__(self, **kwargs):
        self.data_chan = kwargs['data']
        self.stats_chan = kwargs['stats']
        self.object = kwargs['object']

    @auth_wrapper
    def post(self, token):
        data = request.get_json()
        data_cleaned = controller_create_schema.load(data)
        data_cleaned = data_cleaned.data
        stub = objects_pb2_grpc.ObjectServiceStub(self.object)
        uc = objects_pb2.ControllerCreate(
            mac=data_cleaned["mac"],
            controller_type=data_cleaned["controller_type"],
        )
        try:
            rsp = stub.CreateController(uc)
        except Exception as e:
            log.error("Error handling {}".format(str(e)))
            return NotFound("Not found error").get_message()
        rsp = Relations.collect_controller_info(rsp)
        return rsp.get_message()


class ControllerActivate(Resource):
    def __init__(self, **kwargs):
        self.data_chan = kwargs['data']
        self.stats_chan = kwargs['stats']
        self.object = kwargs['object']

    @auth_wrapper
    def post(self, controller_id, token):
        data = request.get_json()
        data_cleaned = controller_activate_schema.load(data)
        data_cleaned = data_cleaned.data
        stub = objects_pb2_grpc.ObjectServiceStub(self.object)
        # {
        #  "id":
        #  "name":
        #  "meta":
        #  "object_id":
        # }
        object_id = utils_pb2.ObjectId(
            object_id=data_cleaned["object_id"]
        )
        controllerid = utils_pb2.ControllerId(
            controller_id=controller_id
        )
        uc = objects_pb2.ControllerActivate(
            id=controllerid,
            name=data_cleaned["name"],
            meta=data_cleaned["meta"],
            object_id=object_id,
        )
        try:
            rsp = stub.ActivateController(uc)
        except Exception as e:
            log.error("Error handling {}".format(str(e)))
            return NotFound("Not found error").get_message()
        rsp = Relations.collect_controller_info(rsp)
        return rsp.get_message()
