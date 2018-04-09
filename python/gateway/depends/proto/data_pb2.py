# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/data.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from proto import utils_pb2 as proto_dot_utils__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/data.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x10proto/data.proto\x1a\x11proto/utils.proto\";\n\tMeterData\x12\x11\n\ttimestamp\x18\x01 \x01(\x04\x12\r\n\x05value\x18\x02 \x01(\x01\x12\x0c\n\x04hash\x18\x03 \x01(\x0c\"+\n\tTimeQuery\x12\x0b\n\x03set\x18\x01 \x01(\x08\x12\x11\n\ttimestamp\x18\x02 \x01(\x04\"^\n\nMeterQuery\x12\x17\n\x03low\x18\x01 \x01(\x0b\x32\n.TimeQuery\x12\x19\n\x05hight\x18\x02 \x01(\x0b\x32\n.TimeQuery\x12\x1c\n\tsensor_id\x18\x03 \x01(\x0b\x32\t.SensorId2;\n\x0b\x44\x61taService\x12,\n\rGetSensorData\x12\x0b.MeterQuery\x1a\n.MeterData\"\x00\x30\x01\x62\x06proto3')
  ,
  dependencies=[proto_dot_utils__pb2.DESCRIPTOR,])




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
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='MeterData.value', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hash', full_name='MeterData.hash', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=39,
  serialized_end=98,
)


_TIMEQUERY = _descriptor.Descriptor(
  name='TimeQuery',
  full_name='TimeQuery',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='set', full_name='TimeQuery.set', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='TimeQuery.timestamp', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=100,
  serialized_end=143,
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
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hight', full_name='MeterQuery.hight', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sensor_id', full_name='MeterQuery.sensor_id', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=145,
  serialized_end=239,
)

_METERQUERY.fields_by_name['low'].message_type = _TIMEQUERY
_METERQUERY.fields_by_name['hight'].message_type = _TIMEQUERY
_METERQUERY.fields_by_name['sensor_id'].message_type = proto_dot_utils__pb2._SENSORID
DESCRIPTOR.message_types_by_name['MeterData'] = _METERDATA
DESCRIPTOR.message_types_by_name['TimeQuery'] = _TIMEQUERY
DESCRIPTOR.message_types_by_name['MeterQuery'] = _METERQUERY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MeterData = _reflection.GeneratedProtocolMessageType('MeterData', (_message.Message,), dict(
  DESCRIPTOR = _METERDATA,
  __module__ = 'proto.data_pb2'
  # @@protoc_insertion_point(class_scope:MeterData)
  ))
_sym_db.RegisterMessage(MeterData)

TimeQuery = _reflection.GeneratedProtocolMessageType('TimeQuery', (_message.Message,), dict(
  DESCRIPTOR = _TIMEQUERY,
  __module__ = 'proto.data_pb2'
  # @@protoc_insertion_point(class_scope:TimeQuery)
  ))
_sym_db.RegisterMessage(TimeQuery)

MeterQuery = _reflection.GeneratedProtocolMessageType('MeterQuery', (_message.Message,), dict(
  DESCRIPTOR = _METERQUERY,
  __module__ = 'proto.data_pb2'
  # @@protoc_insertion_point(class_scope:MeterQuery)
  ))
_sym_db.RegisterMessage(MeterQuery)



_DATASERVICE = _descriptor.ServiceDescriptor(
  name='DataService',
  full_name='DataService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=241,
  serialized_end=300,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetSensorData',
    full_name='DataService.GetSensorData',
    index=0,
    containing_service=None,
    input_type=_METERQUERY,
    output_type=_METERDATA,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_DATASERVICE)

DESCRIPTOR.services_by_name['DataService'] = _DATASERVICE

# @@protoc_insertion_point(module_scope)