import proto.companies_pb2_grpc as companies_pb2_grpc
import proto.companies_pb2 as companies_pb2
import proto.utils_pb2 as utils_pb2
import companies.models.models as models
import companies.models.tariff as tariff
from google.protobuf.json_format import MessageToJson
from concurrent import futures
import argparse
from collections import defaultdict
import grpc
import time
import config
import logging


def tariff_to_pb2(tariff):
    tar_id = companies_pb2.TariffId(tariff.id)
    tariff_val = tariff.tariff
    if isinstance(tariff_val, tariff.MonoTariffVal):
        tariff_val = companies_pb2.TariffCalculationMono(1)
        tariff_pb2 = companies_pb2.TariffInfo(
                    id=tar_id,
                    company=tariff.company,
                    name=tariff.name,
                    mono=tariff_val
        )
        return tariff_pb2
    raise ValueError()

def company_to_pb2(company):
    comp_id = utils_pb2.CompanyId(company_id=company.id)
    comp_pb2 = companies_pb2.CompanyInfo(
            id=comp_id,
            name=company.name,
            address=company.address,
            phone=company.phone,
            bank_account_id=company.bank_account_id)
    return comp_pb2

class ObjectServiceServ(companies_pb2_grpc.CompanyServicer):
    def __init__(self, model):
        self.__model = model

    def GetCompanyInfo(self, request, context):
        comp = self.__model.GetCompanyById(request.company_id)
        comp_pb2 = company_to_pb2(comp)
        return comp_pb2

    def GetTariffInfo(self, request, context):
        tariff = self.__model.GetTariffById(request.tariff_id)
        tariff_pb2 = tariff_to_pb2(tariff)
        return tariff_pb2

    def GetCompanyExtendedInfo(self, request, context):
        full_info = self.__model.GetFullCompanyById(request.company_id)
        if len(full_info) != 0:
            raise ValueError()
        companie = full_info[0][0]
        tariffs = []
        for _, tariff in full_info:
            tariffs.append(tariff_to_pb2(tariff))
        res = companies_pb2.CompanyExtendedInfo(inf=companie, tariffs=tariffs)
        return res

def main():
    parser = argparse.ArgumentParser(description="""
        Service to store and process data companies
    """)
    parser.add_argument('--config', help='configuration file', default=None)
    args = parser.parse_args()
    confs = config.ConfigManager()
    if args.config is not None:
        with open(args.config, "r") as conffile:
            confs.load_from_file(conffile)
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
    companies_pb2_grpc.add_CompanyServicer_to_server(ObjectServiceServ(database), server)
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
