import proto.stats_pb2_grpc as stats_pb2_grpc
import proto.stats_pb2 as stats_pb2
import proto.data_pb2_grpc as data_pb2_grpc
import proto.data_pb2 as data_pb2
import proto.objects_pb2_grpc as objects_pb2_grpc
import proto.objects_pb2 as objects_pb2
import proto.timeq_pb2 as timeq_pb2
from dateutil import relativedelta
from proto import utils_pb2
from concurrent import futures
import grpc
import time
import config
import logging
import datetime
import argparse
from dateutil.relativedelta import relativedelta

class StatsServiceServ(stats_pb2_grpc.StatsServiceServicer):
    def __init__(self, dataserv, objects):
        self.dataserv = dataserv
        self.stub = data_pb2_grpc.DataServiceStub(self.dataserv)
        self.objects = objects
        
    def get_to_month_stat(self, l, h, s_id):
        l -= relativedelta(days=1)
        low = timeq_pb2.TimeQuery(timestamp= int(time.mktime(l.timetuple())))
        hight = timeq_pb2.TimeQuery(timestamp=int(time.mktime(h.timetuple())))
        mq = data_pb2.MeterQuery(low=low, hight=hight, sensor_id=s_id)
        # да простят меня боги
        fst = None
        lst = None
        fst_mnth = None
        lst_mnth = None
        num_of_reqs = 0
        num = 0
        for i in self.stub.GetSensorData(mq):
            num_of_reqs += 1
            if fst is None:
                fst_mnth = datetime.datetime.fromtimestamp(i.timestamp)
                fst = i.value.doublevalue
            lst = i.value.doublevalue
            lst_mnth = datetime.datetime.fromtimestamp(i.timestamp)
            #logging.debug("data got year :{}".format(i.value))
        #logging.debug("data start :{} mth {} stop:{} mth {}".format(fst, fst_mnth, lst, lst_mnth))
        if (fst is None) or (lst is None):
            y_c_month = 0
        else:
            num = relativedelta(lst_mnth, fst_mnth).months + 1
            if num:
                y_c_month = (lst - fst) / num
            else:
                y_c_month = 0
        logging.debug("data start :{} mth {} stop:{} mth {}, months_num {}, req_got {}".format(fst, fst_mnth, lst, lst_mnth, num, num_of_reqs))
        return y_c_month

    def get_sensor_stats(self, s_id):
        curr_mnth_beg = datetime.date.today().replace(day=1)
        curr = (datetime.date.today() + relativedelta(months=1)).replace(day=1)
        # TODO: А в последний месяц сработает?
        # не сработает
        curmnth = self.get_to_month_stat(curr_mnth_beg, curr, s_id)
        if curmnth is None:
            curmnth = 0
        #####
        prev_y_mnth_beg = (datetime.date.today() - relativedelta(years=1)).replace(day=1)
        prev_y_curr = (datetime.date.today() + relativedelta(months=1) - relativedelta(years=1)).replace(day=1)
        prev_curmnth = self.get_to_month_stat(prev_y_mnth_beg, prev_y_curr, s_id)
        if prev_curmnth is None:
            prev_curmnth = 0

        ####
        curr_year = datetime.date.today().replace(day=1, month=1)
        prev_year = (datetime.date.today() - relativedelta(years=1)).replace(day=1, month=1)
        y_c_month = self.get_to_month_stat(prev_year, curr_year, s_id)
        logging.debug("result is :{} {} {}".format(curmnth, prev_curmnth, y_c_month))
        return curmnth, prev_curmnth, y_c_month

    def GetSensorStat(self, request, context):
        s_id = request
        curmnth, prev_curmnth, y_c_month = self.get_sensor_stats(s_id)
        return stats_pb2.SensorStat(current_month=curmnth,
                                    prev_year_month=prev_curmnth,
                                    prev_year_average=y_c_month)
    
    def GetControllerStat(self, request, context):
        stub = objects_pb2_grpc.ObjectServiceStub(self.objects)
        logging.info("some shitty log")
        controller_id = request.controller_id
        uu = utils_pb2.ControllerId(controller_id=controller_id)
        try:
            rsp = stub.GetControllerInfo(uu)
        except Exception as e: 
            logging.error("Error handling {}".format(str(e)))
            return NotFound("Not found error").get_message()

        uo = [i.id for i in rsp.sensors]
        curmnth_sm, prev_curmnth_sm, y_c_month_sm = 0, 0, 0
        for i in uo:
            curmnth, prev_curmnth, y_c_month = self.get_sensor_stats(i)
            curmnth_sm += curmnth
            prev_curmnth_sm += prev_curmnth
            y_c_month_sm += y_c_month
        return stats_pb2.ControllerStat(current_month = curmnth_sm,
                                    prev_year_month=prev_curmnth_sm,
                                    prev_year_average=y_c_month_sm)

    def GetObjectStat(self, request, context):
        stub = objects_pb2_grpc.ObjectServiceStub(self.objects)
        logging.info("some shitty log")
        object_id = request.object_id
        uu = utils_pb2.ObjectId(object_id=object_id)
        try:
            rsp = stub.GetObjectInfo(uu)
        except Exception as e: 
            logging.error("Error handling {}".format(str(e)))
            return NotFound("Not found error").get_message()

        uo = []
        for i in rsp.controllers:
            for sns in i.sensors:
                uo.append(sns.id)
        curmnth_sm, prev_curmnth_sm, y_c_month_sm = 0,0,0
        for i in uo:
            curmnth, prev_curmnth, y_c_month = self.get_sensor_stats(i)
            curmnth_sm += curmnth
            prev_curmnth_sm += prev_curmnth
            y_c_month_sm += y_c_month
        return stats_pb2.ObjectStat(current_month = curmnth_sm,
                                    prev_year_month=prev_curmnth_sm,
                                    prev_year_average=y_c_month_sm)
        
def main():
    parser = argparse.ArgumentParser(description="""
        Service to calculate statistics
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
    objs= grpc.insecure_channel(confs["object_service"]["url"])
    data = grpc.insecure_channel(confs["data_service"]["url"])
    stats_pb2_grpc.add_StatsServiceServicer_to_server(StatsServiceServ(data, objs), server)
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