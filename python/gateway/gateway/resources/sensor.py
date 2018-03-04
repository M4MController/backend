from flask_restful import Resource

class GetSensorStats(Resource):
    def __init__(self, **kwargs):
        pass

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