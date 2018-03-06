from proto import data_pb2_grpc
from proto import data_pb2
from concurrent import futures
import grpc
import time

class DataServiceServ(data_pb2_grpc.DataServiceServicer):
    def GetSensorData(self, request, context):
        yield data_pb2.MeterQuery()
        
def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    data_pb2_grpc.add_DataServiceServicer_to_server(DataServiceServ(), server)
    server.add_insecure_port('[::]:5052')
    server.start()
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    main()