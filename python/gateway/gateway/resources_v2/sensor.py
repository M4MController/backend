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


# добавлен для однообразности
class Relations(object):

    @staticmethod
    def parse_sensor_info(ssr, data_chan, stats_chan):
        stub = data_pb2_grpc.DataServiceStub(data_chan)
        sen_id = ssr.id
        lim = data_pb2.LimitQuery(limit=1)
        frm = data_pb2.TimeQuery(timestamp_null=True)
        mq = data_pb2.TimeLimitedQuery(start=frm, limit=lim, sensor_id=sen_id)
        it = stub.GetLimitedData(mq)
        val = next(it, None)
        val = val.value if val is not None else None
        stub = stats_pb2_grpc.StatsServiceStub(stats_chan)
        #id = utils_pb2.SensorId(sensor_id=sen_id)
        stts = stub.GetSensorStat(sen_id)
        rs = SensorInfo(id=ssr.id.sensor_id,
                        controller_id=ssr.controller_id.controller_id,
                        name=ssr.name,
                        activation_date=None,
                        deactivation_date=None,
                        stats=SensorStats(
                                month=stts.current_month,
                                prev_month=stts.prev_year_month,
                                prev_year=stts.prev_year_average),
                        payments=SensorPayments(0, 0, 0),
                        characteristics=SensorCharacteristics(
                            **Relations.get_sensor_characteristics(ssr.sensor_type)
                        ),
                        finance=SensorFinance(
                            **Relations.get_sensor_finance(ssr.sensor_type)
                        ),
                        last_value=val)
        if ssr.HasField("deactivation_date_val"):
            rs.deactivation_date = ssr.deactivation_date_val
        if ssr.HasField("activation_date_val"):
            rs.activation_date = ssr.activation_date_val
        return rs

    @staticmethod
    def collect_sensor_info(sensor_info, data_chan, stats_chan):
        s_inf = Relations.parse_sensor_info(sensor_info, data_chan, stats_chan)
        return s_inf
    
    @staticmethod 
    def get_sensor_finance(sensor_type):
        dct = {
            1: dict(
                tariff=dict(
                    day=6.19,
                    night=1.92,
                ),
                paiment_id="973363-379-52",
                service_company=CompanyView(
                    **Relations.get_sensor_company(sensor_type)
                )
            ),
            2: dict(
                tariff=35.40,
                paiment_id="958118-379-45",
                service_company=CompanyView(
                    **Relations.get_sensor_company(sensor_type)
                )
            ),
            3: dict(
                tariff=180.55,
                paiment_id="958118-379-45",
                service_company=CompanyView(
                    **Relations.get_sensor_company(sensor_type)
                )
            ),
            4: dict(
                tariff=6.40,
                paiment_id="953611-379-45",
                service_company=CompanyView(
                    **Relations.get_sensor_company(sensor_type)
                )
            )
        }
        return dct[sensor_type]

    @staticmethod
    def get_sensor_company(sensor_type):
        dct = {
            1: dict(
                _id=1,
                name="Мосэнергосбыт",
                addres="Фортунатовская ул., 33/44, Москва, 105187",
                phone="8 (495) 981-98-19",
                bank_account_id="973363-379-52"),
            2: dict(
                _id=2,
                name="Мосводоканал",
                addres="Чистопрудный бул., 10, Москва, 101000",
                phone="8 (499) 763-34-34",
                bank_account_id="958118-379-45"),
            3: dict(
                _id=3,
                name="МОЭК",
                addres="Электродная ул., 4 а, Москва, 111141",
                phone="8 (495) 662-50-50",
                bank_account_id="958118-379-45"),
            4: dict(
                _id=4,
                name="Мосгаз",
                addres="Мрузовский пер., 11, строение 1, Москва, 105120",
                phone="8 (495) 660-60-80",
                bank_account_id="953611-379-45"),
        }
        return dct[sensor_type]

    @staticmethod
    def get_sensor_characteristics(sensor_type):    
        dct = {
            1: dict(sensor_type=sensor_type,
                    unit_of_measurement="кВт",),
            2: dict(sensor_type=sensor_type,
                    unit_of_measurement="куб.м",),
            3: dict(sensor_type=sensor_type,
                    unit_of_measurement="куб.м",),
            4: dict(sensor_type=sensor_type,
                    unit_of_measurement="куб.м",),
        }
        return dct[sensor_type]