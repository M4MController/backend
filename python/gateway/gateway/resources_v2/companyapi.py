from flask_restful import Resource
from gateway.views.objects_info import UserInfo
from gateway.views_v2.objects_lvl import ObjectInfo
from gateway.views_v2.objects_lvl import ControllerInfo
from gateway.views_v2.objects_lvl import SensorInfo
from gateway.views_v2.objects_lvl import ObjList
from gateway.views_v2.objects_lvl import Listed
from gateway.views_v2.objects_lvl import UserInfo
from gateway.views_v2.objects_lvl import SensorCharacteristics
from gateway.auth.auth import auth_wrapper
from gateway.views_v2.stats import SensorStats



class Sensor(Resource):
    def __init__(self, **kwargs):
        self.data_chan = kwargs['data']
        self.stats_chan = kwargs['stats']
        self.object = kwargs['object']
    
    @auth_wrapper
    def get(self, token):
        uinf = UserInfo(
            _id = 5,
            family_name = "Пупкин",
            name = "Вася",
            second_name = "Васильевич",
            date_receiving = "21.01.2010",
            issued_by = "Уральский паспортоизготовительный завод",
            division_number = 1234,
            registration_addres = "Улица Пушкина д 6 кв 5",
            mailing_addres = "Улица Пушкина д 6 кв 5",
            birth_day = "29.02.2000",
            sex = True,
            home_phone = "666 777",
            mobile_phone = "8 800 555 35 35",
            citizenship = "Российская Федерация",
            e_mail = "sobaka@mail.ru",
        )
        sensor = SensorInfo(
            id = 88,
            name = "NAME",
            controller_id = 5,
            activation_date = "20.10.2017",
            deactivation_date = None,
            user_id = 5,
            characteristics = SensorCharacteristics(
                sensor_type = 1,
                unit_of_measurement = "kg",
            ),
            stats = SensorStats(
                        month= 123456,
                        prev_month=123400,
                        prev_year=120),
            finance = None, 
            payments = None,
        )
        return {
            "code": 0,
            "msg":{
                "sensors":[
                    sensor._get_msg(),
                ],
                "users":[
                    uinf._get_msg(),
                ]
            }
        }