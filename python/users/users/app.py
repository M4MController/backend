import proto.users_pb2_grpc as users_pb2_grpc
import proto.users_pb2 as users_pb2
from concurrent import futures
import argparse
from pymongo import MongoClient
import grpc
import time
import config
import logging

class UsersServiceServ(users_pb2_grpc.UserInfoServiceServicer):
    def __init__(self, mgocli):
        self.mgocli = mgocli
    def GetUserInfo(self, request, context):
        uid = request.user_id
        uinf = self.mgocli.users.find_one({"id":uid})
        #tss = int(time.mktime(uinf["passport"]["date_receiving"].timetuple()))
        passport = users_pb2.PassportInfo(issued_by=uinf["passport"]["issued_by"],
                                          date_receiving = int(uinf["passport"]["date_receiving"]),
                                          division_number=uinf["passport"]["division_number"])
        return users_pb2.UserInfo(
                family_name         = uinf["family_name"],
                name                = uinf["name"],
                second_name         = uinf["second_name"],
                passport            = passport,
                registration_addres = uinf["registration_addres"],
                mailing_addres      = uinf["mailing_addres"],
                birth_day           = uinf["birth_day"],
                sex                 = uinf["sex"],
                home_phone          = uinf["home_phone"],
                mobile_phone        = uinf["mobile_phone"],
                citizenship         = uinf["citizenship"],
                e_mail              = uinf["e_mail"])
        
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
    mgocli = MongoClient(confs["database"]["url"])
    databse = mgocli["user_database"]
    users_pb2_grpc.add_UserInfoServiceServicer_to_server(UsersServiceServ(databse), server)
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