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
                        payments=SensorPayments(0,0,0),
                        characteristics=SensorCharacteristics(
                            sensor_type=ssr.sensor_type,
                            unit_of_measurement="кВт",
                        ),
                        finance=SensorFinance(
                            tariff=1,
                            paiment_id="AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
                            service_company=CompanyView(
                                _id=1,
                                name="stubname",
                                addres="stubaddres",
                                phone="8 800 123 45 67",
                                bank_account_id="AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
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