from flask_restful import Resource
from flask_restful import reqparse
from gateway.views.errors import InvalidRequest
from gateway.views.errors import NotFound
from gateway.views.objects_info import UserInfo
from gateway.views.objects_info import ObjectInfo
from gateway.views.objects_info import ControllerInfo
from gateway.views.objects_info import SensorInfo
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

class GetSensorStats(Resource):
    def __init__(self, **kwargs):
        self.data_chan = kwargs['data']
        self.stats_chan = kwargs['stats']

    def get(self, sensor_id):
        stats = {
        "code": 0,
        "msg": {
            "month": 0,
            "prev_month": 0,
            "prev_year": 0
        },
        }
        stub = stats_pb2_grpc.StatsServiceStub(self.stats_chan)
        id = utils_pb2.SensorId(sensor_id=sensor_id)
        rsp = stub.GetSensorStat(id)
        stats_resp = {
            "month": rsp.current_month,
            "prev_month": rsp.prev_year_month,
            "prev_year": rsp.prev_year_average,
        }
        stats["msg"] = stats_resp
        return stats, 200

class GetSensorData(Resource):
    def __init__(self, **kwargs):
        self.data_chan = kwargs['data']
        self.stats_chan = kwargs['stats']

        
    def get(self, sensor_id):
        data = {
        "code": 0,
        "msg": []
        }
        stub = data_pb2_grpc.DataServiceStub(self.data_chan)
        id = utils_pb2.SensorId(sensor_id=sensor_id)
        parser =  reqparse.RequestParser()
        parser.add_argument("from")
        parser.add_argument("to")
        args = parser.parse_args()
        frm = args["from"]
        to = args["to"]
        if to:
            if isinstance(to, list) and len(to) > 1:
                return InvalidRequest("too many values to \"to\"").get_message()
            try:
                h = datetime.datetime.strptime( to, "%Y-%m-%dT%H:%M:%S")
            except ValueError:
                return InvalidRequest("Failed to parse \"to\" date time").get_message()
        else:
            h = datetime.datetime.now()
        if frm:
            if isinstance(frm, list) and len(frm) > 1:
                return InvalidRequest("too many values to \"from\"").get_message()
            try:
                l = datetime.datetime.strptime( frm, "%Y-%m-%dT%H:%M:%S")
            except ValueError:
                return InvalidRequest("Failed to parse \"from\" date time").get_message()
        else:
            l = h - datetime.timedelta(days=7)
        low = data_pb2.TimeQuery(timestamp= int(time.mktime(l.timetuple())))
        hight = data_pb2.TimeQuery(timestamp=int(time.mktime(h.timetuple())))
        mq = data_pb2.MeterQuery(low=low, hight=hight, sensor_id=id)
        data_resp = []
        for i in  stub.GetSensorData(mq):
            dt = {
            "sensor_id": sensor_id,
            "date": datetime.datetime.fromtimestamp(i.timestamp).strftime('%Y-%m-%d %H:%M:%S'),
            "value": i.value,
            "hash": base64.b64encode(i.hash).decode('UTF-8')
            }
            data_resp.append(dt)
        data["msg"] = data_resp
        return data, 200

class AddSensor(Resource):
    def __init__(self, **kwargs):
        pass
    def post(self):
        res = {"code":0,"msg":{"error message":"Sensor Registration Success!"}}
        return res, 200

class GetUserSensors(Resource):
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
                                ssr.activation_date,
                                None,
                                ssr.sensor_type,
                                ssr.company)
                if ssr.HasField("deactivation_date_val"):
                    rs.deactivation_date = ssr.deactivation_date_val
                return rs

            ctr = ControllerInfo(cntrlr.id,
                                cntrlr.name,
                                cntrlr.meta,
                                cntrlr.activation_date,
                                cntrlr.status,
                                cntrlr.mac,
                                cntrlr.controller_type,
                                None,
                                [sensor(i) for i in cntrlr.sensors])
            if cntrlr.HasField("deactivation_date_val"):
                    ctr.deactivation_date = ssr.deactivation_date_val
            return ctr
        def obct(rsp):
            uo = ObjectInfo(
                rsp.id,
                rsp.name,
                rsp.adres,
                [controller(i) for i in rsp.controllers]
            )
            return uo
        uo = UserInfo(
            rsp.id,
            [obct(i) for i in rsp.objects]
        )
        return uo.get_message()