from flask_restful import Resource
from proto import users_pb2_grpc
from proto import users_pb2
from proto import stats_pb2_grpc
from proto import stats_pb2
from proto import utils_pb2

class UserInfo(Resource):
    def __init__(self, **kwargs):
        self.user = kwargs['user']
        
    def get(self):
        user_info = {
                "code": 0,
                "msg": {
                    "family_name": "string",
                    "name": "string",
                    "second_name": "string",
                    "date_receiving": "string",
                    "issued_by": "string",
                    "division_number": "string",
                    "registration_addres": "string",
                    "mailing_addres": "string",
                    "birth_day": "string",
                    "sex": True,
                    "home_phone": "string",
                    "mobile_phone": "string",
                    "citizenship": "string",
                    "e_mail": "string"
                }
            }
        stub = users_pb2_grpc.UserInfoServiceStub(self.user)
        id = utils_pb2.UserId(user_id=1)
        rsp = stub.GetUserInfo(id)
        res = {                         
            "family_name":         rsp.family_name,
            "name":                rsp.name,
            "second_name":         rsp.second_name,
            "date_receiving":      rsp.passport.date_receiving,
            "issued_by":           rsp.passport.issued_by,
            "division_number":     rsp.passport.division_number,
            "registration_addres": rsp.registration_addres,
            "mailing_addres":      rsp.mailing_addres,
            "birth_day":           rsp.birth_day,
            "sex":                 rsp.sex,
            "home_phone":          rsp.home_phone,
            "mobile_phone":        rsp.mobile_phone,
            "citizenship":         rsp.citizenship,
            "e_mail":              rsp.e_mail
        }
        user_info["msg"] = res
        return user_info, 200

class SignIn(Resource):
    def __init__(self, **kwargs):
        pass
    
    def post(self):
        return {"code":0,"msg":{"error message":"Ok"}}, 200
