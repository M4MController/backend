import proto.users_pb2_grpc as users_pb2_grpc
import proto.users_pb2 as users_pb2
from proto import utils_pb2
from concurrent import futures
import argparse
from pymongo import MongoClient
import grpc
import time
import config
import logging
import json
from models.models import UserDb

def get_protobuf_from_user(user):
    user_fields = user.get_fields()
    logging.info(json.dumps(user_fields, indent=4))
    uu = utils_pb2.UserId(user_id=user_fields["id"])
    user_fields["id"] = uu
    return  users_pb2.UserInfo(**user_fields)

def get_protobuf_from_passport(passport):
    passport_fields = passport.get_fields()
    return users_pb2.PassportInfo(**passport_fields)

class UsersServiceServ(users_pb2_grpc.UserInfoServiceServicer):
    def __init__(self, mgocli):
        self.mgocli = mgocli
    
    def GetUserInfo(self, request, context):
        logging.info("GOT USER INFO USER SERVICE")
        uid = request.user_id
        user = self.mgocli.get_user_by_id(uid)
        return get_protobuf_from_user(user)
        
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
    #TODO: Решить как лучше: так или как depend
    mgocli = MongoClient(confs["database"]["url"])
    databse = UserDb(mgocli["user_database"])
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