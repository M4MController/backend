import pika
import json
import time
import logging

log = logging.getLogger("flask.app")

class DataBroker:
    _SENSOR_DATA_QUEUE = 'sensor_data'

    def __init__(self, host, port=5672):
        credentials = pika.PlainCredentials('user','user')
        self._params = pika.ConnectionParameters(host=host, port=port,credentials=credentials)
        self.connect()
    
    def connect(self):
        self._connection = pika.BlockingConnection(self._params)
        self._chanel = self._connection.channel()
        self._declare_sensor_data_queue()

    def declare_queue(self, queue_cls):
        self._chanel.queue_declare(queue=queue_cls.NAME)

    def _declare_sensor_data_queue(self):
        self._chanel.queue_declare(queue=DataBroker._SENSOR_DATA_QUEUE)

    def _send_data(self, sensor_data):
        self._chanel.basic_publish(exchange='',
                                   routing_key='sensor_data',
                                   body=json.dumps(sensor_data))

    def send_sensor_data(self, sensor_data):
        sensor_data['timestamp'] = sensor_data['timestamp'].strftime("%Y-%m-%dT%H:%M:%S")
        try:
            self._send_data(sensor_data)
        except pika.exceptions.ConnectionClosed as e:
            log.error("failed to connect {}".format(str(e)))
            self.connect()
            self._send_data(sensor_data)