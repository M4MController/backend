from marshmallow import Schema, fields
import datetime
import pymongo

class SensorDataModel(object):
    @staticmethod
    def get_sensor_id(s_id):
        return 'sensor_' + str(s_id)

    class Schema(Schema):
        controller_mac = fields.Str(required=True)
        sensor_id = fields.Int(required=True)
        value = fields.Int(required=True)
        hash = fields.Str(required=True)
        timestamp = fields.DateTime('%Y-%m-%dT%H:%M:%S', required=True)

    def __init__(self, mongo):
        self.__mgocli = mongo
        self.schema = SensorDataModel.Schema()

    def get_data_by_period(self, sensor_id, frm=None, to=None):
        low = frm
        hight = to
        sen_id = self.get_sensor_id(sensor_id)
        coll = self.__mgocli['sensors_data'][sen_id]
        timestamp_args = {}
        filt = {}
        if low is not None:
            timestamp_args["$gt"] = low
        if hight is not None:
            timestamp_args["$lt"] = hight
        if timestamp_args:
            filt['timestamp'] = timestamp_args
        for i in coll.find(filt).sort('timestamp', pymongo.DESCENDING):
            yield i

    def get_data_from(self, sensor, frm=None, limit=0):
        hight = frm
        sen_id = self.get_sensor_id(sensor)
        coll = self.__mgocli['sensors_data'][sen_id]
        filt = {}
        timestamp_args = {}
        if hight is not None:
            timestamp_args["$lt"] = hight
        if timestamp_args:
            filt['timestamp'] = timestamp_args
        for i in coll.find(filt).sort('timestamp', pymongo.DESCENDING).limit(limit):
            yield i

    def insert_data(self, data):
        errs = self.schema.validate(data)
        if errs:
            return errs
        coll_id = self.get_sensor_id(data['sensor_id'])
        data['timestamp'] = datetime.datetime.strptime(data['timestamp'], '%Y-%m-%dT%H:%M:%S')
        self.__mgocli['sensors_data'][coll_id].insert_one(data)
        return errs