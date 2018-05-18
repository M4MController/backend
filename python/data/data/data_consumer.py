import pika
from pymongo import MongoClient
import json
import logging
import datetime

class DataConsumer:
    # вынести консюмера, нафиг
    def __init__(self, database, host, user, password, port=5672):
        logging.debug('starting to listen host {} user {} pass {}'.format(host, user, password))
        credentials = pika.PlainCredentials(user,password)
        self._connection = pika.BlockingConnection(pika.ConnectionParameters(host=host, port=port, credentials=credentials))
        self._channel = self._connection.channel()
        self._database = database
        self._channel.queue_declare(queue='sensor_data')

        self._channel.basic_consume(self.on_sensor_data_receive,
                                    queue='sensor_data',
                                    no_ack=True)

    def on_sensor_data_receive(self, ch, method, properties, body):
        body = body.decode("utf-8")
        logging.debug('body is {}'.format(body))
        data = json.loads(body)
        coll_id = 'sensor_' + str(data['sensor_id'])
        data['timestamp'] = datetime.datetime.strptime( data['timestamp'], '%Y-%m-%dT%H:%M:%S')
        self._database['sensors_data'][coll_id].insert_one(data)

    def start_consuming(self):
        self._channel.start_consuming()
