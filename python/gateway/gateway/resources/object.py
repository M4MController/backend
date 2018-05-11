from flask_restful import Resource

class AddObject(Resource):
    def __init__(self, **kwargs):
        pass

    def post(self):
        res = {"code":0,"msg":{"error message":"Object Registration Success!"}}
        return res, 200

class GetObjectStats(Resource):
    def __init__(self, **kwargs):
        pass

    def get(self, object_id):
        res = {"code":0,"msg":{"error message":"Object STATS"}}
        return res, 200


class GetUserObjects(Resource):
    def __init__(self, **kwargs):
        pass

    def get(self):
        res = {"code":0,
            "msg":[{
                "id":1,
                "name":"Имя Объекта",
                "user_id":1,
                "adres":"Улица Пушкина, Дом Колотушкина"}
                ]
        }
        return res, 200

class GetObjectControllers(Resource):
    def __init__(self, **kwargs):
        pass
        
    def get(self, object_id):
        controllers = {
        "code": 0,
        "msg": [
            {
            "id": 0,
            "name": "string",
            "object_id": object_id,
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
