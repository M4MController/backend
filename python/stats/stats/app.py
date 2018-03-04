import stats_pb2_grpc
import stats_pb2
from concurrent import futures
import grpc
import time

class StatsServiceServ(stats_pb2_grpc.StatsServiceServicer):
    def GetSensorStat(self, request, context):
        return stats_pb2.SensorStat()
        
def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    stats_pb2_grpc.add_StatsServiceServicer_to_server(StatsServiceServ(), server)
    server.add_insecure_port('[::]:5051')
    server.start()
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    main()