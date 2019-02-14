import pika
from pymongo import MongoClient
import json
import logging
import datetime
from data_model.sensor_data import SensorDataModel

class DataConsumer:
    # вынести консюмера, нафиг
    def __init__(self, database, host, user, password, port=5672):
        logging.getLogger("pika").setLevel(logging.WARNING)
        logging.debug('starting to listen host {} user {} pass {}'.format(host, user, password))
        credentials = pika.PlainCredentials(user,password)
        self._connection = pika.BlockingConnection(pika.ConnectionParameters(host=host, port=port, credentials=credentials))
        self._channel = self._connection.channel()
        self._datamodel = SensorDataModel(database)
        self._channel.queue_declare(queue='sensor_data')
        self._channel.basic_consume(self.on_sensor_data_receive,
                                    queue='sensor_data',
                                    no_ack=True)
        logging.getLogger("pika").setLevel(logging.WARNING)

    def on_sensor_data_receive(self, ch, method, properties, body):
        body = body.decode("utf-8")
        logging.debug('body is {}'.format(body))
        data = json.loads(body)
        errs = self._datamodel.insert_data(data)
        if errs:
            logging.error(errs)
        else:
            logging.debug("Inserted")

    def start_consuming(self):
        self._channel.start_consuming()
