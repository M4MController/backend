from proto import data_pb2_grpc
from google.protobuf.timestamp_pb2 import Timestamp
from proto import data_pb2
from concurrent import futures
import grpc
import time
import argparse
from pymongo import MongoClient
from data_consumer import DataConsumer
import logging
import config
import datetime
from data_model.sensor_data import SensorDataModel
from proto import objects_pb2_grpc
from proto import objects_pb2
from proto import utils_pb2

# TODO: решить что-нибудь с дефолтными аргументами 
class DataServiceServ(data_pb2_grpc.DataServiceServicer):
    def __init__(self, model, objs):
        self.__model = model
        self._objects_channel = objs
        self._objects_stub = objects_pb2_grpc.ObjectServiceStub(self._objects_channel)
    
    def get_sensor_info(self, sensor_id):
        sid = utils_pb2.SensorId(
            sensor_id=sensor_id,
        )
        return self._objects_stub.GetSensorInfo(sid)
    
    def pack_data(self, data, sensor_type):
        if sensor_type == 0:
            value = data_pb2.DataValue(strvalue=data['value'])
            return data_pb2.MeterData(value=value, timestamp=data['timestamp'], hash=data['hash'].encode())
        if sensor_type in [1, 2, 3, 4]:
            value = data_pb2.DataValue(doublevalue=data['value'])
            return data_pb2.MeterData(value=value, timestamp=data['timestamp'], hash=data['hash'].encode())
        return None

    def GetSensorData(self, request, context):
        global client
        low = None
        if request.low.HasField("timestamp"):
            low_val = datetime.datetime.fromtimestamp(request.low.timestamp)
            kwargs = {}
            if request.low.HasField("equal"):
                kwargs.update({"equal": request.low.equal})
            low = self.__model.Gt(low_val, **kwargs)
        hight = None
        if request.hight.HasField("timestamp"):
            hight_val = datetime.datetime.fromtimestamp(request.hight.timestamp)
            kwargs = {}
            if request.hight.HasField("equal"):
                kwargs.update({"equal": request.hight.equal})
            hight = self.__model.Lt(hight_val, **kwargs)
        logging.debug("Got sensor data request {}".format(str(request)))
        number = 0
        sen_info = self.get_sensor_info(request.sensor_id.sensor_id)
        for i in self.__model.get_data_by_period(request.sensor_id.sensor_id, low, hight):
            number += 1
            i['timestamp'] = int(time.mktime(i['timestamp'].timetuple()))
            yield self.pack_data(i, sen_info.sensor_type)
        logging.debug("{} data records was found".format(number))

    def GetLimitedData(self, request, context):
        global client
        start = None
        if request.start.HasField("timestamp"):
            start_val = datetime.datetime.fromtimestamp(request.start.timestamp)
            kwargs = {}
            if request.start.HasField("equal"):
                kwargs.update({"equal": request.start.equal})
            start = self.__model.Lt(start_val, **kwargs)
        limit = 0
        if request.limit.HasField("limit"):
            limit = request.limit.limit
        logging.debug("Got sensor data request {}".format(str(request)))
        number = 0
        sen_info = self.get_sensor_info(request.sensor_id.sensor_id)
        for i in self.__model.get_data_from(request.sensor_id.sensor_id, start, limit):
            number += 1
            i['timestamp'] = int(time.mktime(i['timestamp'].timetuple()))
            yield self.pack_data(i, sen_info.sensor_type)
        logging.debug("{} data records was found".format(number))
