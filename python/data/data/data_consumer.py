import pika
from pymongo import MongoClient
import json


class DataConsumer:
    def __init__(self, database, host, port=5672):
        self._connection = pika.BlockingConnection(pika.ConnectionParameters(host=host, port=port))
        self._channel = self._connection.channel()
        self._database = database

        self._channel.queue_declare(queue='sensor_data')

        self._channel.basic_consume(self.on_sensor_data_receive,
                                    queue='sensor_data',
                                    no_ack=True)

    def on_sensor_data_receive(self, ch, method, properties, body):
        body = body.decode("utf-8")
        print(body)
        self._database['sensor_data'].insert_one(json.loads(body))

    def start_consuming(self):
        self._channel.start_consuming()
