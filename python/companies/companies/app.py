import proto.companies_pb2_grpc as companies_pb2_grpc
import proto.companies_pb2 as companies_pb2
import proto.utils_pb2 as utils_pb2
import companies.models.models as models
from google.protobuf.json_format import MessageToJson
from concurrent import futures
from collections import defaultdict
import grpc
import time
import config
import logging
import psycopg2

class ObjectServiceServ(companies_pb2_grpc.CompanyServicer):
    def __init__(self, model):
        self.__model = model

    def GetCompanyInfo(self, request, context):
        pass

    def GetTariffInfo(self, request, context):
        pass

    def GetCompanyExtendedInfo(self, request, context):
        pass

def main():
    confs = config.ConfigManager()
    logging.basicConfig(level=getattr(logging, confs["LogLevel"].upper()))
    address = confs["address"]
    logging.info("Starting grpc server with address :{}".format(address))
    logging.info("Starting grpc server {} workers".format(confs["workers"]))
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=confs["workers"]))
    dbconf = confs["database"]
    database = models.Model(host=dbconf["host"],
                            user=dbconf["username"],
                            password=dbconf["password"],
                            databasename=dbconf["database"])
    companies_pb2_grpc.add_ObjectServiceServicer_to_server(ObjectServiceServ(database), server)
    server.add_insecure_port(address)
    server.start()
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        logging.info("Stop signal got")
        server.stop(0)

if __name__ == '__main__':
    main()
