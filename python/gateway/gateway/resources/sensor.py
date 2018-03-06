from flask_restful import Resource
from proto import data_pb2_grpc
from proto import data_pb2
from proto import stats_pb2_grpc
from proto import stats_pb2


class GetSensorStats(Resource):
    def __init__(self, **kwargs):
        self.data_chan = kwargs['data']
        self.stats_chan = kwargs['stats']
        print(self.stats_chan)

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
        id = stats_pb2.SensorId(sensor_id=sensor_id)
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
        pass
        
    def get(self, sensor_id):
        data = {
        "code": 0,
        "msg": [
            {
            "sensor_id": sensor_id,
            "date": "string",
            "value": 0,
            "hash": "string"
            }
        ]
        }
        return data, 200