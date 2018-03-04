from flask_restful import Resource

class UserInfo(Resource):
    def __init__(self, **kwargs):
        pass
        
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

        return user_info, 200