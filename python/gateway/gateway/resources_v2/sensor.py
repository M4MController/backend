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
    def parse_sensor_info(ssr):
        rs = SensorInfo(ssr.id,
                        ssr.controller_id,
                        ssr.name,
                        ssr.activation_date,
                        None,
                        ssr.sensor_type,
                        ssr.company)
        if ssr.HasField("deactivation_date_val"):
            rs.deactivation_date = ssr.deactivation_date_val
        return rs

    @staticmethod
    def collect_sensor_info(sensor_info, data_chan):
        s_inf = Relations.parse_sensor_info(sensor_info)
        return s_inf