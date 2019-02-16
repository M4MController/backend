from marshmallow import Schema, fields
import datetime
import logging
import pymongo

RAW_SENSOR_TYPE = 0
ELECTRO_SENSOR_TYPE = 1
COLD_WATER_SENSOR_TYPE = 2
HOT_WATER_SENSOR_TYPE = 3
GAS_SENSOR_TYPE = 4

class BaseSchema(Schema):
    controller_mac = fields.Str(required=True)
    sensor_id = fields.Int(required=True)
    hash = fields.Str(required=True)
    timestamp = fields.DateTime('%Y-%m-%dT%H:%M:%S', required=True)

class RawSchema(BaseSchema):
    _SENSOR_TYPES = [RAW_SENSOR_TYPE, ]
    value = fields.Raw(required=True)

class FloatSchema(BaseSchema):
    _SENSOR_TYPES = [ ELECTRO_SENSOR_TYPE,
                       COLD_WATER_SENSOR_TYPE,
                       HOT_WATER_SENSOR_TYPE,
                       GAS_SENSOR_TYPE,
                    ]
    value = fields.Raw(required=True)

class DataValidator:
    @staticmethod
    def generate_schemas_map():
        schema = {}
        for concrete_schema in BaseSchema.__subclasses__():
            for typename in concrete_schema._SENSOR_TYPES:
                schema[typename] = concrete_schema()
        return schema

    def __init__(self):
        self.schemas_map = DataValidator.generate_schemas_map()

    def validate(self, data, sensor_type):
        return self.schemas_map[sensor_type].validate(data)

class SensorDataModel(object):
    _DATABASE_NAME = 'sensors_data'

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

    def __init__(self, mongo):
        self.__mgocli = mongo
        self.validator = DataValidator()
    
    def get_data_by_period(self, sensor_id, low=None, hight=None):
        sen_id = self.get_sensor_id(sensor_id)
        coll = self.__mgocli[SensorDataModel._DATABASE_NAME][sen_id]
        timestamp_args = {}
        if low is not None:
            timestamp_args.update(low.get_command())
        if hight is not None:
            timestamp_args.update(hight.get_command())
        filter_args = None
        if timestamp_args:
            filter_args = {}
            filter_args.update({'timestamp': timestamp_args})
        logging.info("filter is {}".format(filter_args))
        logging.info("sen_id is {}".format(sen_id))
        for i in coll.find(filter_args).sort('timestamp'):
            yield i

    def get_data_from(self, sensor_id, hight, limit=0):
        sen_id = self.get_sensor_id(sensor_id)
        coll = self.__mgocli['sensors_data'][sen_id]
        timestamp_args = {}
        if hight is not None:
            timestamp_args.update(hight.get_command())
        filter_args = None
        if timestamp_args:
            filter_args = {}
            filter_args.update({'timestamp': timestamp_args})
        logging.info("filter is {}".format(filter_args))
        logging.info("sen_id is {}".format(sen_id))
        for i in coll.find(filter_args).sort('timestamp', pymongo.DESCENDING).limit(limit):
            yield i
    
    def validate_data(self, data, sensor_type):
        return self.validator.validate(data, sensor_type)

    def insert_data(self, data, sensor_type):
        errs = self.validate_data(data, sensor_type)
        if errs:
            return errs
        coll_id = self.get_sensor_id(data['sensor_id'])
        data['timestamp'] = datetime.datetime.strptime( data['timestamp'], '%Y-%m-%dT%H:%M:%S')
        self.__mgocli['sensors_data'][coll_id].insert_one(data)
        return errs