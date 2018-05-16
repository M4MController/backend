from proto import data_pb2_grpc
from proto import data_pb2
from concurrent import futures
import grpc
import time
from pymongo import MongoClient
from data_consumer import DataConsumer
import logging
import config

class DataServiceServ(data_pb2_grpc.DataServiceServicer):
    def __init__(self, mgocli):
        self.__mgocli = mgocli
        
    def GetSensorData(self, request, context):
        global client
        low = request.low
        hight = request.hight
        sen_id = request.sensor_id.sensor_id
        coll = self.__mgocli['sensors_data'][str(sen_id)]
        for i in coll.find():
            yield data_pb2.MeterData(value=i['value'], timestamp=i['timestamp'], hash=i['hash'])


def run_consumer(mgocli, rabbitconf):
    client = mgocli
    # я не понял, какую ты хочешь сделать архитектуру (её пока нет), поэтому пихнул пока как попало :)
    DataConsumer(client.testdatabase, rabbitconf["host"], rabbitconf["user"], rabbitconf["pass"], rabbitconf["port"]).start_consuming()


def main():
    confs = config.ConfigManager()
    logging.basicConfig(level=getattr(logging, confs["LogLevel"].upper()))
    addres = confs["addres"]
    logging.info("Starting grpc server with addres :{}".format(addres))
    logging.info("Starting grpc server {} workers".format(confs["workers"]))
    mgocli = MongoClient(confs["database"]["url"])
    run_consumer(mgocli, confs["rabbit"])
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=confs["workers"]))
    data_pb2_grpc.add_DataServiceServicer_to_server(DataServiceServ(mgocli), server)
    server.add_insecure_port(addres)
    server.start()
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        logging.info("Stop signal got")
        server.stop(0)

if __name__ == '__main__':
    main()