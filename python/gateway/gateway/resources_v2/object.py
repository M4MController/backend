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
    
    def get(self, _id):
        stub = objects_pb2_grpc.ObjectServiceStub(self.object)
        include = request.args.getlist("include")
        log.info("some shitty log {}".format(include))
        uu = utils_pb2.ObjectId(object_id=_id)
        try:
            rsp = stub.GetObjectInfo(uu)
        except Exception as e: 
            log.error("Error handling {}".format(str(e)))
            return NotFound("Not found error").get_message()
        objects = []
        controllers = []
        sensors = []
        def controller(cntrlr):
            def sensor(ssr):
                rs = SensorInfo(ssr.id,
                                ssr.controller_id,
                                ssr.name,
                                ssr.activation_date,
                                None,
                                ssr.sensor_type,
                                ssr.company)
                if ssr.HasField("deactivation_date_val"):
                    rs.deactivation_date = ssr.deactivation_date_val
                return rs
            nonlocal sensors
            sensors += [sensor(i) for i in cntrlr.sensors]

            ctr = ControllerInfo(id=cntrlr.id,
                                object_id=cntrlr.object_id,
                                name=cntrlr.name,
                                meta=cntrlr.meta,
                                activation_date=cntrlr.activation_date,
                                status=cntrlr.status,
                                mac=cntrlr.mac,
                                controller_type=cntrlr.controller_type,
                                deactivation_date=None)
            if cntrlr.HasField("deactivation_date_val"):
                    ctr.deactivation_date = ssr.deactivation_date_val
            return ctr
        
        controllers = [controller(i) for i in rsp.controllers]

        controllers=Listed(controllers)
        sensors=Listed(sensors)

        kwargs = {}
        if include:
            if 'controllers' in include:
                kwargs['controllers']=controllers
            if 'sensors' in include:
                kwargs['sensors']=sensors
        else:
            kwargs=dict(controllers=controllers, sensors=sensors)
        return ObjList(**kwargs).get_message()