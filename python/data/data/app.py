from proto import data_pb2_grpc
from proto import data_pb2
from concurrent import futures
import grpc
import time
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

class DataServiceServ(data_pb2_grpc.DataServiceServicer):
    def GetSensorData(self, request, context):
        global client
        low = request.low
        hight = request.hight
        sen_id = request.sensor_id.sensor_id
        coll = client['sensors_data'][str(sen_id)]
        for i in coll.find():
            yield data_pb2.MeterData(value=i['value'], timestamp=i['timestamp'], hash=i['hash'])

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