import pika
import json


class DataBroker:
    _SENSOR_DATA_QUEUE = 'sensor_data'

    def __init__(self, host, port=5672):
        self._connection = pika.BlockingConnection(pika.ConnectionParameters(host=host, port=port))
        self._chanel = self._connection.channel()

        self._declare_sensor_data_queue()

    def declare_queue(self, queue_cls):
        self._chanel.queue_declare(queue=queue_cls.NAME)

    def _declare_sensor_data_queue(self):
        self._chanel.queue_declare(queue=DataBroker._SENSOR_DATA_QUEUE)

    def send_sensor_data(self, sensor_data):
        self._chanel.basic_publish(exchange='',
                                   routing_key='sensor_data',
                                   body=json.dumps(sensor_data))
