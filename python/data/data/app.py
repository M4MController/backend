from proto import data_pb2_grpc
from google.protobuf.timestamp_pb2 import Timestamp
from proto import data_pb2
from concurrent import futures
import grpc
import time
from pymongo import MongoClient
from data_consumer import DataConsumer
import logging
import config
import datetime
from data_model.sensor_data import SensorDataModel


# TODO: решить что-нибудь с дефолтными аргументами 
class DataServiceServ(data_pb2_grpc.DataServiceServicer):
    def __init__(self, model):
        self.__model = model
        
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
        for i in self.__model.get_data_by_period(request.sensor_id.sensor_id, low, hight):
            #logging.debug("Sending data{}".format(str(i)))
            tss = int(time.mktime(i['timestamp'].timetuple()))
            yield data_pb2.MeterData(value=i['value'], timestamp=tss, hash=i['hash'].encode())

    def GetLimitedData(self, request, context):
        global client
        start = None
        if request.start.HasField("timestamp"):
            start_val = datetime.datetime.fromtimestamp(request.start.timestamp)
            kwargs = {}
            if request.start.HasField("equal"):
                kwargs.update({"equal": request.start.equal})
            start = self.__model.Gt(start_val, **kwargs)
        limit = 0
        if request.limit.HasField("limit"):
            limit = request.limit.limit
        logging.debug("Got sensor data request {}".format(str(request)))
        for i in self.__model.get_data_from(request.sensor_id.sensor_id, start, limit):
            logging.debug("Sending data{}".format(str(i)))
            tss = int(time.mktime(i['timestamp'].timetuple()))
            yield data_pb2.MeterData(value=i['value'], timestamp=tss, hash=i['hash'].encode())


def run_consumer(mgocli, rabbitconf):
    client = mgocli
    # я не понял, какую ты хочешь сделать архитектуру (её пока нет), поэтому пихнул пока как попало :)
    DataConsumer(client, rabbitconf["host"], rabbitconf["user"], rabbitconf["pass"], rabbitconf["port"]).start_consuming()


def main():
    confs = config.ConfigManager()
    logging.basicConfig(level=getattr(logging, confs["LogLevel"].upper()))
    addres = confs["addres"]
    logging.info("Starting grpc server with addres :{}".format(addres))
    logging.info("Starting grpc server {} workers".format(confs["workers"]))
    mgocli = MongoClient(confs["database"]["url"])
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=confs["workers"]))
    data_pb2_grpc.add_DataServiceServicer_to_server(DataServiceServ(SensorDataModel(mgocli)), server)
    server.add_insecure_port(addres)
    server.start()
    run_consumer(mgocli, confs["rabbit"])
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        logging.info("Stop signal got")
        server.stop(0)

if __name__ == '__main__':
    main()