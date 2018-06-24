import proto.users_pb2_grpc as users_pb2_grpc
import proto.users_pb2 as users_pb2
from concurrent import futures
from pymongo import MongoClient
import grpc
import time
import config
import logging
# {
#      id                  : 1,
#      family_name         : "Иванов",
#      name                : "Иван",
#      second_name         : "Иванович",
#      passport            : {issued_by:"123", date_receiving:"123", division_number:"123"},
#      registration_addres : "Улица",
#      mailing_addres      : "УлицаУлица",
#      birth_day           : "123341",
#        sex               : 1,
#      home_phone          : "8-800-555-35-35",
#      mobile_phone        : "8-800-555-35-35",
#      citizenship         : "РФ",
#      e_mail              : "ml@gmail.com"
# }
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
    confs = config.ConfigManager()
    logging.basicConfig(level=getattr(logging, confs["LogLevel"].upper()))
    addres = confs["addres"]
    logging.info("Starting grpc server with addres :{}".format(addres))
    logging.info("Starting grpc server {} workers".format(confs["workers"]))
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=confs["workers"]))
    mgocli = MongoClient(confs["database"]["url"])
    databse = mgocli["user_database"]
    users_pb2_grpc.add_UserInfoServiceServicer_to_server(UsersServiceServ(databse), server)
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