import pika
from pymongo import MongoClient
import json
import logging
import datetime
from data_model.sensor_data import SensorDataModel
from proto import objects_pb2_grpc
from proto import objects_pb2
from proto import utils_pb2

class DataConsumer:
    # вынести консюмера, нафиг
    def __init__(self, database, host, user, password, objs, port=5672):
        logging.getLogger("pika").setLevel(logging.WARNING)
        logging.debug('starting to listen host {} user {} pass {}'.format(host, user, password))
        credentials = pika.PlainCredentials(user,password)
        self._connection = pika.BlockingConnection(pika.ConnectionParameters(host=host, port=port, credentials=credentials))
        logging.getLogger("pika").setLevel(logging.WARNING)
        self._channel = self._connection.channel()
        self._datamodel = SensorDataModel(database)
        self._channel.queue_declare(queue='sensor_data')
        self._channel.basic_consume(self.on_sensor_data_receive,
                                    queue='sensor_data',
                                    no_ack=True)
        self._objects_channel = objs
        self._objects_stub = objects_pb2_grpc.ObjectServiceStub(self._objects_channel)

    def get_sensor_info(self, data):
        sid = utils_pb2.SensorId(
            sensor_id=data["sensor_id"],
        )
        return self._objects_stub.GetSensorInfo(sid)
        

    def on_sensor_data_receive(self, ch, method, properties, body):
        body = body.decode("utf-8")
        logging.debug('body is {}'.format(body))
        data = json.loads(body)
        sen_info = self.get_sensor_info(data)
        errs = self._datamodel.insert_data(data, sen_info.sensor_type)
        if errs:
            logging.error(errs)
        else:
            logging.debug("Inserted")

    def start_consuming(self):
        self._channel.start_consuming()
