import proto.stats_pb2_grpc as stats_pb2_grpc
import proto.stats_pb2 as stats_pb2
from concurrent import futures
import grpc
import time
import config
import logging

class StatsServiceServ(stats_pb2_grpc.StatsServiceServicer):
    def GetSensorStat(self, request, context):
        return stats_pb2.SensorStat()
        
def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    stats_pb2_grpc.add_StatsServiceServicer_to_server(StatsServiceServ(), server)
    confs = config.ConfigManager()
    logging.basicConfig(level=getattr(logging, confs["LogLevel"].upper()))
    addres = confs["addres"]
    logging.info("Starting grpc server with addres :{}".format(addres))
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