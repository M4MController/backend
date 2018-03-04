from flask_restful import Resource

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
            "user_id": 0,
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

class GetControllerSensors(Resource):
    def __init__(self, **kwargs):
        pass
        
    def get(self, controller_id):
        sensors = {
        "code": 0,
        "msg": [
            {
            "id": 0,
            "name": "string",
            "controller_id": controller_id,
            "activation_date": "string",
            "status": 0,
            "deactivation_date": "string",
            "sensor_type": 0,
            "company": "string"
            },
        ],
        }
        return sensors, 200

class GetControllerStats(Resource):
    def __init__(self, **kwargs):
        pass
        
    def get(self, controller_id):
        stats = {
        "code": 0,
        "msg": {
            "controller_id": controller_id,
            "month": 0,
            "prev_month": 0,
            "prev_year": 0
        },
        }
        return stats, 200