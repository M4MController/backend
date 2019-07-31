from flask_restful import Resource
from flask_restful import reqparse
from flask import request
from gateway.views.errors import InvalidRequest
from gateway.views.errors import NotFound
from gateway.views.objects_info import UserInfo
from gateway.views_v2.objects_lvl import ObjectInfo
from gateway.views_v2.objects_lvl import ControllerInfo
from gateway.views_v2.objects_lvl import SensorInfo
from gateway.views_v2.objects_lvl import ObjList
from gateway.views_v2.objects_lvl import Listed
from gateway.views_v2.objects_lvl import SensorCharacteristics
from gateway.views_v2.objects_lvl import SensorFinance
from gateway.views_v2.objects_lvl import CompanyView
from gateway.views_v2.stats import SensorStats
from gateway.views_v2.payments import SensorPayments
from gateway.views_v2.http import DeleteOk
from gateway.views_v2.payments import Tariff
from gateway.resources_v2.input.sensor import sensor_create_schema
from proto import objects_pb2_grpc
from proto import objects_pb2
from proto import data_pb2_grpc
from proto import data_pb2
from proto import stats_pb2_grpc
from proto import stats_pb2
from proto import utils_pb2
from proto import timeq_pb2
import datetime
import base64
import time
import logging
from gateway.auth.auth import auth_wrapper
import logging
from gateway.views.errors import NotAuthorized

log = logging.getLogger("flask.app")


# добавлен для однообразности
class Relations(object):

    @staticmethod
    def parse_sensor_info(ssr, data_chan, stats_chan):
        sen_id = ssr.id
        sensor_payments = None
        finance = None
        stats = None
        last_value = None
        sensor_type = ssr.sensor_type
        if ssr.name == "OBD":
            ssr.sensor_type = 5
        elif ssr.name == "GPS":
            ssr.sensor_type = 6
        characteristics = SensorCharacteristics(**Relations.get_sensor_characteristics(ssr.sensor_type))
        ssr.sensor_type = sensor_type
        if ssr.sensor_type != 0:
            sensor_payments = SensorPayments(**Relations.get_sensor_payments(ssr.sensor_type))
            finance = SensorFinance(**Relations.get_sensor_finance(ssr.sensor_type))
            stub = stats_pb2_grpc.StatsServiceStub(stats_chan)
            #id = utils_pb2.SensorId(sensor_id=sen_id)
            stts = stub.GetSensorStat(sen_id)
            stats = SensorStats(
                        month=stts.current_month,
                        prev_month=stts.prev_year_month,
                        prev_year=stts.prev_year_average),
            lim = data_pb2.LimitQuery(limit=1)
            frm = timeq_pb2.TimeQuery(timestamp_null=True)
            stub = data_pb2_grpc.DataServiceStub(data_chan)
            mq = data_pb2.TimeLimitedQuery(start=frm, limit=lim, sensor_id=sen_id)
            it = stub.GetLimitedData(mq)
            val = next(it, None)
            val = val.value if val is not None else None
            # TODO: перерделать на нормальный подход
            val_unpacked = None
            if val:
                if val.HasField("strvalue"):
                    val_unpacked = val.strvalue
                if val.HasField("doublevalue"):
                    val_unpacked = val.doublevalue
            last_value = val_unpacked

        rs = SensorInfo(id=ssr.id.sensor_id,
                        controller_id=ssr.controller_id.controller_id,
                        name=ssr.name,
                        activation_date=None,
                        deactivation_date=None,
                        stats=stats,
                        payments=sensor_payments,
                        characteristics=characteristics,
                        finance=finance,
                        last_value=last_value,
                        meta=ssr.meta)
        if ssr.HasField("deactivation_date_val"):
            rs.deactivation_date = ssr.deactivation_date_val
        if ssr.HasField("activation_date_val"):
            rs.activation_date = ssr.activation_date_val
        return rs

    @staticmethod
    def get_sensor_payments(sensor_type):
        dct = {
            1: dict(
                charge=1935,
                overpayment=0,
                for_payment=1935,
            ),
            2: dict(
                charge=1819,
                overpayment=0,
                for_payment=1819,
            ),
            3: dict(
                charge=775,
                overpayment=0,
                for_payment=775,
            ),
            4: dict(
                charge=960,
                overpayment=0,
                for_payment=960,
            ),
        }
        if sensor_type not in dct:
            return None
        return dct[sensor_type]

    @staticmethod
    def collect_sensor_info(sensor_info, data_chan, stats_chan):
        s_inf = Relations.parse_sensor_info(sensor_info, data_chan, stats_chan)
        return s_inf
    
    @staticmethod
    def get_sensor_tariff(sensor_type):
        dct = {
            1: dict (
                _id=1,
                name="Электричество",
                _type="daynight_tariff",
                vals=dict(
                    day=6.19,
                    night=1.92,
                ),
            ),
            2: dict (
                _id=2,
                name="Холодная вода",
                _type="mono",
                vals={
                    "val": 35.40,
                }
            ),
            3: dict (
                _id=3,
                name="Горячая вода",
                _type="mono",
                vals={
                    "val": 180.55,
                }
            ),
            4: dict (_id=4,
                name="Газ",
                _type="mono",
                vals={
                    "val": 6.40,
                }
            ),
        }
        if sensor_type not in dct:
            return None
        return dct[sensor_type]

    @staticmethod 
    def get_sensor_finance(sensor_type):
        tariff_data = Relations.get_sensor_tariff(sensor_type)
        if tariff_data is None:
            return None
        tariff = Tariff(**tariff_data)
        dct = {
            1: dict(
                tariff=tariff,
                payment_id="973363-379-52",
                service_company=CompanyView(
                    **Relations.get_sensor_company(sensor_type)
                )
            ),
            2: dict(
                tariff=tariff,
                payment_id="958118-379-45",
                service_company=CompanyView(
                    **Relations.get_sensor_company(sensor_type)
                )
            ),
            3: dict(
                tariff=tariff,
                payment_id="958118-379-45",
                service_company=CompanyView(
                    **Relations.get_sensor_company(sensor_type)
                )
            ),
            4: dict(
                tariff=tariff,
                payment_id="953611-379-45",
                service_company=CompanyView(
                    **Relations.get_sensor_company(sensor_type)
                )
            )
        }
        if sensor_type not in dct:
            return None
        return dct[sensor_type]

    @staticmethod
    def get_sensor_company(sensor_type):
        dct = {
            1: dict(
                _id=1,
                name="Мосэнергосбыт",
                address="Фортунатовская ул., 33/44, Москва, 105187",
                phone="8 (495) 981-98-19",
                bank_account_id="973363-379-52"),
            2: dict(
                _id=2,
                name="Мосводоканал",
                address="Чистопрудный бул., 10, Москва, 101000",
                phone="8 (499) 763-34-34",
                bank_account_id="958118-379-45"),
            3: dict(
                _id=3,
                name="МОЭК",
                address="Электродная ул., 4 а, Москва, 111141",
                phone="8 (495) 662-50-50",
                bank_account_id="958118-379-45"),
            4: dict(
                _id=4,
                name="Мосгаз",
                address="Мрузовский пер., 11, строение 1, Москва, 105120",
                phone="8 (495) 660-60-80",
                bank_account_id="953611-379-45"),
        }
        if sensor_type not in dct:
            return None
        return dct[sensor_type]

    @staticmethod
    def get_sensor_characteristics(sensor_type):
        dct = {
            0: dict(sensor_type=sensor_type,
                    unit_of_measurement=None),
            1: dict(sensor_type=sensor_type,
                    unit_of_measurement="кВт",),
            2: dict(sensor_type=sensor_type,
                    unit_of_measurement="куб.м",),
            3: dict(sensor_type=sensor_type,
                    unit_of_measurement="куб.м",),
            4: dict(sensor_type=sensor_type,
                    unit_of_measurement="куб.м",),
        }
<<<<<<< HEAD

        if sensor_type not in dct:
            return None
        return dct[sensor_type]
=======
        return dct.get(sensor_type,  dict(sensor_type=sensor_type, unit_of_measurement=None))
>>>>>>> 53c39cdeab52d2ccd1f4f221ba95f61c548de88c


class Sensor(Resource):
    def __init__(self, **kwargs):
        self.data_chan = kwargs['data']
        self.stats_chan = kwargs['stats']
        self.object = kwargs['object']

    @auth_wrapper
    def post(self, token):
        data = request.get_json()
        data_cleaned = sensor_create_schema.load(data)
        data_cleaned = data_cleaned.data
        stub = objects_pb2_grpc.ObjectServiceStub(self.object)
        uc = objects_pb2.SensorCreate(
            date=datetime.datetime.now().strftime("%Y-%m-%d"),
            sensor_type=data_cleaned["sensor_type"],
            name=data_cleaned["name"],
            company=data_cleaned["company"],
            controller_id=data_cleaned["controller_id"]
        )
        try:
            rsp = stub.CreateSensor(uc)
        except Exception as e:
            log.error("Error handling {}".format(str(e)))
            return NotFound("Not found error").get_message()
        rsp = Relations.collect_sensor_info(rsp, self.data_chan, self.stats_chan)
        return rsp.get_message()

    @auth_wrapper
    def delete(self, _id, token):
        stub = objects_pb2_grpc.ObjectServiceStub(self.object)
        uc = utils_pb2.SensorId(
            sensor_id=_id,
        )
        try:
            stub.DeleteSensor(uc)
        except Exception as e:
            log.error("Error handling {}".format(str(e)))
            return NotFound("Not found error").get_message()
        return DeleteOk("Sensor deleted").get_message()
