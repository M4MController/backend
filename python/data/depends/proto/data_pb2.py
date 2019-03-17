# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/data.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from proto import utils_pb2 as proto_dot_utils__pb2
from proto import timeq_pb2 as proto_dot_timeq__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/data.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x10proto/data.proto\x1a\x11proto/utils.proto\x1a\x11proto/timeq.proto\"?\n\tDataValue\x12\x12\n\x08strvalue\x18\x01 \x01(\tH\x00\x12\x15\n\x0b\x64oublevalue\x18\x02 \x01(\x01H\x00\x42\x07\n\x05value\"G\n\tMeterData\x12\x11\n\ttimestamp\x18\x01 \x01(\x04\x12\x19\n\x05value\x18\x02 \x01(\x0b\x32\n.DataValue\x12\x0c\n\x04hash\x18\x03 \x01(\x0c\"^\n\nMeterQuery\x12\x17\n\x03low\x18\x01 \x01(\x0b\x32\n.TimeQuery\x12\x19\n\x05hight\x18\x02 \x01(\x0b\x32\n.TimeQuery\x12\x1c\n\tsensor_id\x18\x03 \x01(\x0b\x32\t.SensorId\"A\n\nLimitQuery\x12\x14\n\nlimit_null\x18\x01 \x01(\x08H\x00\x12\x0f\n\x05limit\x18\x02 \x01(\x04H\x00\x42\x0c\n\ntime_query\"g\n\x10TimeLimitedQuery\x12\x1c\n\tsensor_id\x18\x01 \x01(\x0b\x32\t.SensorId\x12\x19\n\x05start\x18\x02 \x01(\x0b\x32\n.TimeQuery\x12\x1a\n\x05limit\x18\x03 \x01(\x0b\x32\x0b.LimitQuery2p\n\x0b\x44\x61taService\x12,\n\rGetSensorData\x12\x0b.MeterQuery\x1a\n.MeterData\"\x00\x30\x01\x12\x33\n\x0eGetLimitedData\x12\x11.TimeLimitedQuery\x1a\n.MeterData\"\x00\x30\x01\x62\x06proto3')
  ,
  dependencies=[proto_dot_utils__pb2.DESCRIPTOR,proto_dot_timeq__pb2.DESCRIPTOR,])




_DATAVALUE = _descriptor.Descriptor(
  name='DataValue',
  full_name='DataValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='strvalue', full_name='DataValue.strvalue', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='doublevalue', full_name='DataValue.doublevalue', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='value', full_name='DataValue.value',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=58,
  serialized_end=121,
)


_METERDATA = _descriptor.Descriptor(
  name='MeterData',
  full_name='MeterData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='MeterData.timestamp', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='MeterData.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hash', full_name='MeterData.hash', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=123,
  serialized_end=194,
)


_METERQUERY = _descriptor.Descriptor(
  name='MeterQuery',
  full_name='MeterQuery',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='low', full_name='MeterQuery.low', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hight', full_name='MeterQuery.hight', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sensor_id', full_name='MeterQuery.sensor_id', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=196,
  serialized_end=290,
)


_LIMITQUERY = _descriptor.Descriptor(
  name='LimitQuery',
  full_name='LimitQuery',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='limit_null', full_name='LimitQuery.limit_null', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='limit', full_name='LimitQuery.limit', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='time_query', full_name='LimitQuery.time_query',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=292,
  serialized_end=357,
)


_TIMELIMITEDQUERY = _descriptor.Descriptor(
  name='TimeLimitedQuery',
  full_name='TimeLimitedQuery',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sensor_id', full_name='TimeLimitedQuery.sensor_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start', full_name='TimeLimitedQuery.start', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='limit', full_name='TimeLimitedQuery.limit', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=359,
  serialized_end=462,
)

_DATAVALUE.oneofs_by_name['value'].fields.append(
  _DATAVALUE.fields_by_name['strvalue'])
_DATAVALUE.fields_by_name['strvalue'].containing_oneof = _DATAVALUE.oneofs_by_name['value']
_DATAVALUE.oneofs_by_name['value'].fields.append(
  _DATAVALUE.fields_by_name['doublevalue'])
_DATAVALUE.fields_by_name['doublevalue'].containing_oneof = _DATAVALUE.oneofs_by_name['value']
_METERDATA.fields_by_name['value'].message_type = _DATAVALUE
_METERQUERY.fields_by_name['low'].message_type = proto_dot_timeq__pb2._TIMEQUERY
_METERQUERY.fields_by_name['hight'].message_type = proto_dot_timeq__pb2._TIMEQUERY
_METERQUERY.fields_by_name['sensor_id'].message_type = proto_dot_utils__pb2._SENSORID
_LIMITQUERY.oneofs_by_name['time_query'].fields.append(
  _LIMITQUERY.fields_by_name['limit_null'])
_LIMITQUERY.fields_by_name['limit_null'].containing_oneof = _LIMITQUERY.oneofs_by_name['time_query']
_LIMITQUERY.oneofs_by_name['time_query'].fields.append(
  _LIMITQUERY.fields_by_name['limit'])
_LIMITQUERY.fields_by_name['limit'].containing_oneof = _LIMITQUERY.oneofs_by_name['time_query']
_TIMELIMITEDQUERY.fields_by_name['sensor_id'].message_type = proto_dot_utils__pb2._SENSORID
_TIMELIMITEDQUERY.fields_by_name['start'].message_type = proto_dot_timeq__pb2._TIMEQUERY
_TIMELIMITEDQUERY.fields_by_name['limit'].message_type = _LIMITQUERY
DESCRIPTOR.message_types_by_name['DataValue'] = _DATAVALUE
DESCRIPTOR.message_types_by_name['MeterData'] = _METERDATA
DESCRIPTOR.message_types_by_name['MeterQuery'] = _METERQUERY
DESCRIPTOR.message_types_by_name['LimitQuery'] = _LIMITQUERY
DESCRIPTOR.message_types_by_name['TimeLimitedQuery'] = _TIMELIMITEDQUERY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DataValue = _reflection.GeneratedProtocolMessageType('DataValue', (_message.Message,), dict(
  DESCRIPTOR = _DATAVALUE,
  __module__ = 'proto.data_pb2'
  # @@protoc_insertion_point(class_scope:DataValue)
  ))
_sym_db.RegisterMessage(DataValue)

MeterData = _reflection.GeneratedProtocolMessageType('MeterData', (_message.Message,), dict(
  DESCRIPTOR = _METERDATA,
  __module__ = 'proto.data_pb2'
  # @@protoc_insertion_point(class_scope:MeterData)
  ))
_sym_db.RegisterMessage(MeterData)

MeterQuery = _reflection.GeneratedProtocolMessageType('MeterQuery', (_message.Message,), dict(
  DESCRIPTOR = _METERQUERY,
  __module__ = 'proto.data_pb2'
  # @@protoc_insertion_point(class_scope:MeterQuery)
  ))
_sym_db.RegisterMessage(MeterQuery)

LimitQuery = _reflection.GeneratedProtocolMessageType('LimitQuery', (_message.Message,), dict(
  DESCRIPTOR = _LIMITQUERY,
  __module__ = 'proto.data_pb2'
  # @@protoc_insertion_point(class_scope:LimitQuery)
  ))
_sym_db.RegisterMessage(LimitQuery)

TimeLimitedQuery = _reflection.GeneratedProtocolMessageType('TimeLimitedQuery', (_message.Message,), dict(
  DESCRIPTOR = _TIMELIMITEDQUERY,
  __module__ = 'proto.data_pb2'
  # @@protoc_insertion_point(class_scope:TimeLimitedQuery)
  ))
_sym_db.RegisterMessage(TimeLimitedQuery)



_DATASERVICE = _descriptor.ServiceDescriptor(
  name='DataService',
  full_name='DataService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=464,
  serialized_end=576,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetSensorData',
    full_name='DataService.GetSensorData',
    index=0,
    containing_service=None,
    input_type=_METERQUERY,
    output_type=_METERDATA,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetLimitedData',
    full_name='DataService.GetLimitedData',
    index=1,
    containing_service=None,
    input_type=_TIMELIMITEDQUERY,
    output_type=_METERDATA,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_DATASERVICE)

DESCRIPTOR.services_by_name['DataService'] = _DATASERVICE

# @@protoc_insertion_point(module_scope)
