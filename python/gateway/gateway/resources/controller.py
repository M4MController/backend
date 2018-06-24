from flask_restful import Resource
from flask_restful import reqparse
from gateway.views.errors import InvalidRequest
from gateway.views.errors import NotFound
from gateway.views.objects_lvl import Listed
from gateway.views.objects_lvl import ObjectInfo
from gateway.views.objects_lvl import ControllerInfo
from gateway.views.objects_lvl import SensorInfo
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

class GetUserControllers(Resource):
    def __init__(self, **kwargs):
        pass
        
    def get(self):
        controllers = {
        "code": 0,
        "msg": [
            {
            "id": 0,
            "name": "string",
            "object_id": 1,
            "adres": "string",
            "activation_date": "string",
            "status": 0,
            "mac": "string",
            "deactivation_date": "string",
            "controller_type": 0
            }
        ], 
        }
        return controllers, 200


class GetControllerStats(Resource):
    def __init__(self, **kwargs):
        self.stats_chan = kwargs['stats']
        
    def get(self, controller_id):
        stats = {
        "code": 0,
        "msg": {
            "month": 0,
            "prev_month": 0,
            "prev_year": 0
        },
        }
        stub = stats_pb2_grpc.StatsServiceStub(self.stats_chan)
        id = utils_pb2.ControllerId(controller_id=controller_id)
        rsp = stub.GetControllerStat(id)
        stats["msg"]["month"] = rsp.current_month
        stats["msg"]["prev_month"] = rsp.prev_year_month
        stats["msg"]["prev_year"] = rsp.prev_year_average
        return stats, 200

class AddController(Resource):
    def __init__(self, **kwargs):
        pass
    def post(self):
        return {"code":0,"msg":{"error message":"Controller Registration Success!"}}, 200

class GetControllerSensors(Resource):
    def __init__(self, **kwargs):
        self.data_chan = kwargs['data']
        self.stats_chan = kwargs['stats']
        self.object = kwargs['object']

    def get(self, controller_id):
        stub = objects_pb2_grpc.ObjectServiceStub(self.object)
        log.info("some shitty log")
        uu = utils_pb2.ControllerId(controller_id=controller_id)
        try:
            rsp = stub.GetControllerInfo(uu)
        except Exception as e: 
            log.error("Error handling {}".format(str(e)))
            return NotFound("Not found error").get_message()
        
        def sensor(ssr):
            rs = SensorInfo(ssr.id,
                            ssr.name,
                            ssr.activation_date,
                            None,
                            ssr.sensor_type,
                            ssr.company)
            if ssr.HasField("deactivation_date_val"):
                rs.deactivation_date = ssr.deactivation_date_val
            return rs

        uo = Listed(
            [sensor(i) for i in rsp.sensors]
        )
        return uo.get_message()
