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

class DataServiceServ(data_pb2_grpc.DataServiceServicer):
    def __init__(self, model):
        self.__model = model
        
    def GetSensorData(self, request, context):
        global client
        low = datetime.datetime.fromtimestamp(request.low.timestamp)
        hight = datetime.datetime.fromtimestamp(request.hight.timestamp)
        logging.debug("Got sensor data request {}".format(str(request)))
        for i in self.__model.get_data_by_period(request.sensor_id.sensor_id, low, hight):
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