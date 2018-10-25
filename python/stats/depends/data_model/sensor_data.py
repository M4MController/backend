from marshmallow import Schema, fields
import datetime

class SensorDataModel(object):
    class Gt:
        def __init__(self, value, equal=True):
            self.val = value
            self.equal = equal

        def _get_command_name(self):
            return "$gt" if not self.equal else "$gte"

        def get_command(self):
            return {self._get_command_name(): self.val}

    class Lt:
        def __init__(self, value, equal=False):
            self.val = value
            self.equal = equal
        
        def _get_command_name(self):
            return "$lt" if not self.equal else "$lte"

        def get_command(self):
            return {self._get_command_name(): self.val}
    
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
    
    def get_data_by_period(self, sensor_id, low=None, hight=None):
        sen_id = self.get_sensor_id(sensor_id)
        coll = self.__mgocli['sensors_data'][sen_id]
        timestamp_args = {}
        if low is not None:
            timestamp_args.update(low.get_command())
        if hight is not None:
            timestamp_args.update(hight.get_command())
        for i in coll.find({'timestamp':timestamp_args}).sort('timestamp'):
            yield i 

    def get_data_from(self, sensor_id, hight, limit=0):
        sen_id = self.get_sensor_id(sensor_id)
        coll = self.__mgocli['sensors_data'][sen_id]
        timestamp_args = {}
        if hight is not None:
            timestamp_args.update(hight.get_command())
        for i in coll.find({'timestamp': timestamp_args}).sort('timestamp').limit(limit):
            yield i
    
    def insert_data(self, data):
        errs = self.schema.validate(data)
        if errs:
            return errs
        coll_id = self.get_sensor_id(data['sensor_id'])
        data['timestamp'] = datetime.datetime.strptime( data['timestamp'], '%Y-%m-%dT%H:%M:%S')
        self.__mgocli['sensors_data'][coll_id].insert_one(data)
        return errs