import proto.stats_pb2_grpc as stats_pb2_grpc
import proto.stats_pb2 as stats_pb2
import proto.data_pb2_grpc as data_pb2_grpc
import proto.data_pb2 as data_pb2
import proto.objects_pb2_grpc as objects_pb2_grpc
import proto.objects_pb2 as objects_pb2
from proto import utils_pb2
from concurrent import futures
import grpc
import time
import config
import logging
import datetime 
from dateutil import relativedelta

class StatsServiceServ(stats_pb2_grpc.StatsServiceServicer):
    def __init__(self, dataserv, objects):
        self.dataserv = dataserv
        self.stub = data_pb2_grpc.DataServiceStub(self.dataserv)
        self.objects = objects
        
    def get_to_month_stat(self, l, h, s_id):
        low = data_pb2.TimeQuery(timestamp= int(time.mktime(l.timetuple())))
        hight = data_pb2.TimeQuery(timestamp=int(time.mktime(h.timetuple())))
        mq = data_pb2.MeterQuery(low=low, hight=hight, sensor_id=s_id)
        # да простят меня боги
        fst = None
        lst = None
        fst_mnth = None
        lst_mnth = None
        for i in self.stub.GetSensorData(mq):
            if fst is None:
                if datetime.datetime.fromtimestamp(i.timestamp).day != 1:
                    continue
                fst_mnth = datetime.datetime.fromtimestamp(i.timestamp)
                fst = i.value
            lst = i.value
            lst_mnth = datetime.datetime.fromtimestamp(i.timestamp)
            #logging.debug("data got year :{}".format(i.value))
        logging.debug("data start :{} mth {} stop:{} mth {}".format(fst, fst_mnth, lst, lst_mnth))
        if (fst is None) or (lst is None):
            y_c_month = 0
        else:
            num = relativedelta.relativedelta(lst_mnth, fst_mnth).months
            if num:
                y_c_month = (lst - fst) / num
            else:
                y_c_month = 0
        return y_c_month

    def get_sensor_stats(self, s_id):
        #
        curr_mnth_beg = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0, day=1)
        curr = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        curr_year = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0, day=1, month=1)
        prev_year = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0, day=1, month=1, year=(curr_year.year - 1)) - datetime.timedelta(days=1)
        prev_y_mnth_beg = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0, day=1, year=(curr_year.year - 1))
        prev_y_curr = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0, day=1, month=prev_y_mnth_beg.month+1, year=(curr_year.year - 1)) - datetime.timedelta(days=1)
        #
        
        curmnth = self.get_to_month_stat(curr_mnth_beg, curr, s_id)
        if curmnth is None:
            curmnth = 0
        #####

        prev_curmnth = self.get_to_month_stat(prev_y_mnth_beg, prev_y_curr, s_id)
        if prev_curmnth is None:
            prev_curmnth = 0

        ####
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
        curmnth_sm, prev_curmnth_sm, y_c_month_sm = 0,0,0
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
    confs = config.ConfigManager()
    logging.basicConfig(level=getattr(logging, confs["LogLevel"].upper()))
    addres = confs["addres"]
    logging.info("Starting grpc server with addres :{}".format(addres))
    logging.info("Starting grpc server {} workers".format(confs["workers"]))
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=confs["workers"]))
    data = grpc.insecure_channel('data-service:5000')
    objs = grpc.insecure_channel('object-service:5000')
    stats_pb2_grpc.add_StatsServiceServicer_to_server(StatsServiceServ(data, objs), server)
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