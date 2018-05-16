from flask_restful import Resource
from proto import data_pb2_grpc
from proto import data_pb2
from proto import stats_pb2_grpc
from proto import stats_pb2
from proto import utils_pb2 
import datetime
import base64

class GetSensorStats(Resource):
    def __init__(self, **kwargs):
        self.data_chan = kwargs['data']
        self.stats_chan = kwargs['stats']

    def get(self, sensor_id):
        stats = {
        "code": 0,
        "msg": {
            "type": 0,
            "name": "string",
            "status": 0,
            "accural": 0,
            "over": 0,
            "result": 0,
            "stats": {
            "current_month": 0,
            "prev_year_month": 0,
            "prev_year_average": 0
            }
        }
        }
        stub = stats_pb2_grpc.StatsServiceStub(self.stats_chan)
        id = utils_pb2.SensorId(sensor_id=sensor_id)
        rsp = stub.GetSensorStat(id)
        stats_resp = {
            "current_month": rsp.current_month,
            "prev_year_month": rsp.prev_year_month,
            "prev_year_average": rsp.prev_year_average,
        }
        stats["stats"] = stats_resp
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
        low = data_pb2.TimeQuery(set=False)
        hight = data_pb2.TimeQuery(set=False)
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
