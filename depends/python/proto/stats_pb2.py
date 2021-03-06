# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/stats.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from proto import utils_pb2 as proto_dot_utils__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/stats.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x11proto/stats.proto\x1a\x11proto/utils.proto\"W\n\nSensorStat\x12\x15\n\rcurrent_month\x18\x01 \x01(\x01\x12\x17\n\x0fprev_year_month\x18\x02 \x01(\x01\x12\x19\n\x11prev_year_average\x18\x03 \x01(\x01\"[\n\x0e\x43ontrollerStat\x12\x15\n\rcurrent_month\x18\x01 \x01(\x01\x12\x17\n\x0fprev_year_month\x18\x02 \x01(\x01\x12\x19\n\x11prev_year_average\x18\x03 \x01(\x01\"W\n\nObjectStat\x12\x15\n\rcurrent_month\x18\x01 \x01(\x01\x12\x17\n\x0fprev_year_month\x18\x02 \x01(\x01\x12\x19\n\x11prev_year_average\x18\x03 \x01(\x01\x32\x9b\x01\n\x0cStatsService\x12)\n\rGetSensorStat\x12\t.SensorId\x1a\x0b.SensorStat\"\x00\x12)\n\rGetObjectStat\x12\t.ObjectId\x1a\x0b.ObjectStat\"\x00\x12\x35\n\x11GetControllerStat\x12\r.ControllerId\x1a\x0f.ControllerStat\"\x00\x62\x06proto3')
  ,
  dependencies=[proto_dot_utils__pb2.DESCRIPTOR,])




_SENSORSTAT = _descriptor.Descriptor(
  name='SensorStat',
  full_name='SensorStat',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='current_month', full_name='SensorStat.current_month', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prev_year_month', full_name='SensorStat.prev_year_month', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prev_year_average', full_name='SensorStat.prev_year_average', index=2,
      number=3, type=1, cpp_type=5, label=1,
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
  ],
  serialized_start=40,
  serialized_end=127,
)


_CONTROLLERSTAT = _descriptor.Descriptor(
  name='ControllerStat',
  full_name='ControllerStat',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='current_month', full_name='ControllerStat.current_month', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prev_year_month', full_name='ControllerStat.prev_year_month', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prev_year_average', full_name='ControllerStat.prev_year_average', index=2,
      number=3, type=1, cpp_type=5, label=1,
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
  ],
  serialized_start=129,
  serialized_end=220,
)


_OBJECTSTAT = _descriptor.Descriptor(
  name='ObjectStat',
  full_name='ObjectStat',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='current_month', full_name='ObjectStat.current_month', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prev_year_month', full_name='ObjectStat.prev_year_month', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prev_year_average', full_name='ObjectStat.prev_year_average', index=2,
      number=3, type=1, cpp_type=5, label=1,
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
  ],
  serialized_start=222,
  serialized_end=309,
)

DESCRIPTOR.message_types_by_name['SensorStat'] = _SENSORSTAT
DESCRIPTOR.message_types_by_name['ControllerStat'] = _CONTROLLERSTAT
DESCRIPTOR.message_types_by_name['ObjectStat'] = _OBJECTSTAT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SensorStat = _reflection.GeneratedProtocolMessageType('SensorStat', (_message.Message,), dict(
  DESCRIPTOR = _SENSORSTAT,
  __module__ = 'proto.stats_pb2'
  # @@protoc_insertion_point(class_scope:SensorStat)
  ))
_sym_db.RegisterMessage(SensorStat)

ControllerStat = _reflection.GeneratedProtocolMessageType('ControllerStat', (_message.Message,), dict(
  DESCRIPTOR = _CONTROLLERSTAT,
  __module__ = 'proto.stats_pb2'
  # @@protoc_insertion_point(class_scope:ControllerStat)
  ))
_sym_db.RegisterMessage(ControllerStat)

ObjectStat = _reflection.GeneratedProtocolMessageType('ObjectStat', (_message.Message,), dict(
  DESCRIPTOR = _OBJECTSTAT,
  __module__ = 'proto.stats_pb2'
  # @@protoc_insertion_point(class_scope:ObjectStat)
  ))
_sym_db.RegisterMessage(ObjectStat)



_STATSSERVICE = _descriptor.ServiceDescriptor(
  name='StatsService',
  full_name='StatsService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=312,
  serialized_end=467,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetSensorStat',
    full_name='StatsService.GetSensorStat',
    index=0,
    containing_service=None,
    input_type=proto_dot_utils__pb2._SENSORID,
    output_type=_SENSORSTAT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetObjectStat',
    full_name='StatsService.GetObjectStat',
    index=1,
    containing_service=None,
    input_type=proto_dot_utils__pb2._OBJECTID,
    output_type=_OBJECTSTAT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetControllerStat',
    full_name='StatsService.GetControllerStat',
    index=2,
    containing_service=None,
    input_type=proto_dot_utils__pb2._CONTROLLERID,
    output_type=_CONTROLLERSTAT,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_STATSSERVICE)

DESCRIPTOR.services_by_name['StatsService'] = _STATSSERVICE

# @@protoc_insertion_point(module_scope)
