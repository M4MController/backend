from proto import data_pb2_grpc
from google.protobuf.timestamp_pb2 import Timestamp
from proto import data_pb2
from concurrent import futures
import grpc
import time
import argparse
from pymongo import MongoClient
from data_consumer import DataConsumer
from grpc_service import DataServiceServ
import logging
import config
import datetime
from data_model.sensor_data import SensorDataModel
from proto import objects_pb2_grpc
from proto import objects_pb2
from proto import utils_pb2


def run_consumer(mgocli, rabbitconf, objs):
    DataConsumer(mgocli, rabbitconf["host"], rabbitconf["user"], rabbitconf["pass"], objs, rabbitconf["port"]).start_consuming()


def main():
    parser = argparse.ArgumentParser(description="""
        Service to store data
    """)
    parser.add_argument('--config', help='configuration file', default=None)
    args = parser.parse_args()
    confs = config.ConfigManager()
    if args.config is not None:
        with open(args.config, "r") as conffile:
            confs.load_from_file(conffile)
    logging.basicConfig(level=getattr(logging, confs["LogLevel"].upper()))
    address = confs["address"]
    objs = grpc.insecure_channel(confs["objs"])
    logging.info("Starting grpc server with address :{}".format(address))
    logging.info("Starting grpc server {} workers".format(confs["workers"]))
    mgocli = MongoClient(confs["database"]["url"])
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=confs["workers"]))
    data_pb2_grpc.add_DataServiceServicer_to_server(DataServiceServ(SensorDataModel(mgocli), objs), server)
    server.add_insecure_port(address)
    server.start()
    run_consumer(mgocli, confs["rabbit"], objs)
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        logging.info("Stop signal got")
        server.stop(0)

if __name__ == '__main__':
    main()