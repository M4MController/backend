# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/objects.proto

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
  name='proto/objects.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x13proto/objects.proto\x1a\x11proto/utils.proto\"\x87\x03\n\nSensorInfo\x12\x15\n\x02id\x18\x01 \x01(\x0b\x32\t.SensorId\x12\x0e\n\x04name\x18\x02 \x01(\tH\x00\x12\x13\n\tname_null\x18\r \x01(\x08H\x00\x12\x1d\n\x13\x61\x63tivation_date_val\x18\x03 \x01(\x04H\x01\x12\x1e\n\x14\x61\x63tivation_date_null\x18\x0b \x01(\x08H\x01\x12\x0e\n\x06status\x18\x04 \x01(\x04\x12 \n\x16\x64\x65\x61\x63tivation_date_null\x18\x08 \x01(\x08H\x02\x12\x1f\n\x15\x64\x65\x61\x63tivation_date_val\x18\t \x01(\x04H\x02\x12\x13\n\x0bsensor_type\x18\x06 \x01(\x04\x12\x11\n\x07\x63ompany\x18\x07 \x01(\tH\x03\x12\x16\n\x0c\x63ompany_null\x18\x0c \x01(\x08H\x03\x12$\n\rcontroller_id\x18\n \x01(\x0b\x32\r.ControllerIdB\x0c\n\nname_oneofB\x11\n\x0f\x61\x63tivation_dateB\x13\n\x11\x64\x65\x61\x63tivation_dateB\x0f\n\rcompany_oneof\"g\n\x0cSensorCreate\x12\x13\n\x0bsensor_type\x18\x01 \x01(\x04\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0f\n\x07\x63ompany\x18\x03 \x01(\t\x12\x0c\n\x04\x64\x61te\x18\x05 \x01(\t\x12\x15\n\rcontroller_id\x18\x04 \x01(\x04\"\xb7\x03\n\x0e\x43ontrollerInfo\x12\x19\n\x02id\x18\x01 \x01(\x0b\x32\r.ControllerId\x12\x0e\n\x04name\x18\x02 \x01(\tH\x00\x12\x13\n\tname_null\x18\x0f \x01(\x08H\x00\x12\x0c\n\x04meta\x18\x03 \x01(\t\x12\x1d\n\x13\x61\x63tivation_date_val\x18\x04 \x01(\x04H\x01\x12\x1e\n\x14\x61\x63tivation_date_null\x18\r \x01(\x08H\x01\x12\x0e\n\x06status\x18\x05 \x01(\x04\x12\x0b\n\x03mac\x18\x06 \x01(\t\x12 \n\x16\x64\x65\x61\x63tivation_date_null\x18\x0b \x01(\x08H\x02\x12\x1f\n\x15\x64\x65\x61\x63tivation_date_val\x18\n \x01(\x04H\x02\x12\x17\n\x0f\x63ontroller_type\x18\x08 \x01(\x04\x12\x1e\n\tobject_id\x18\x0c \x01(\x0b\x32\t.ObjectIdH\x03\x12\x18\n\x0eobject_id_null\x18\x0e \x01(\x08H\x03\x12\x1c\n\x07sensors\x18\t \x03(\x0b\x32\x0b.SensorInfoB\x0c\n\nname_oneofB\x11\n\x0f\x61\x63tivation_dateB\x13\n\x11\x64\x65\x61\x63tivation_dateB\x11\n\x0fobject_id_oneof\"8\n\x10\x43ontrollerCreate\x12\x0b\n\x03mac\x18\x01 \x01(\t\x12\x17\n\x0f\x63ontroller_type\x18\x02 \x01(\x04\"\x82\x01\n\nObjectInfo\x12\x15\n\x02id\x18\x01 \x01(\x0b\x32\t.ObjectId\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x03 \x01(\t\x12$\n\x0b\x63ontrollers\x18\x04 \x03(\x0b\x32\x0f.ControllerInfo\x12\x18\n\x07user_id\x18\x05 \x01(\x0b\x32\x07.UserId\">\n\tUserInfoH\x12\x13\n\x02id\x18\x01 \x01(\x0b\x32\x07.UserId\x12\x1c\n\x07objects\x18\x02 \x03(\x0b\x32\x0b.ObjectInfo\"-\n\x0cObjectCreate\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t\"i\n\x12\x43ontrollerActivate\x12\x19\n\x02id\x18\x01 \x01(\x0b\x32\r.ControllerId\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04meta\x18\x03 \x01(\t\x12\x1c\n\tobject_id\x18\x04 \x01(\x0b\x32\t.ObjectId2\xc5\x04\n\rObjectService\x12%\n\x0cGetUsersInfo\x12\x07.UserId\x1a\n.UserInfoH\"\x00\x12\x35\n\x11GetControllerInfo\x12\r.ControllerId\x1a\x0f.ControllerInfo\"\x00\x12)\n\rGetSensorInfo\x12\t.SensorId\x1a\x0b.SensorInfo\"\x00\x12)\n\rGetObjectInfo\x12\t.ObjectId\x1a\x0b.ObjectInfo\"\x00\x12,\n\x0c\x43reateObject\x12\r.ObjectCreate\x1a\x0b.ObjectInfo\"\x00\x12\x38\n\x10\x43reateController\x12\x11.ControllerCreate\x1a\x0f.ControllerInfo\"\x00\x12,\n\x0c\x43reateSensor\x12\r.SensorCreate\x1a\x0b.SensorInfo\"\x00\x12<\n\x12\x41\x63tivateController\x12\x13.ControllerActivate\x1a\x0f.ControllerInfo\"\x00\x12\"\n\x0c\x44\x65leteObject\x12\t.ObjectId\x1a\x05.Void\"\x00\x12\"\n\x0c\x44\x65leteSensor\x12\t.SensorId\x1a\x05.Void\"\x00\x12*\n\x10\x44\x65leteController\x12\r.ControllerId\x1a\x05.Void\"\x00\x12\x38\n\x14\x44\x65\x61\x63tivateController\x12\r.ControllerId\x1a\x0f.ControllerInfo\"\x00\x62\x06proto3')
  ,
  dependencies=[proto_dot_utils__pb2.DESCRIPTOR,])




_SENSORINFO = _descriptor.Descriptor(
  name='SensorInfo',
  full_name='SensorInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='SensorInfo.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='SensorInfo.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name_null', full_name='SensorInfo.name_null', index=2,
      number=13, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='activation_date_val', full_name='SensorInfo.activation_date_val', index=3,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='activation_date_null', full_name='SensorInfo.activation_date_null', index=4,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='SensorInfo.status', index=5,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deactivation_date_null', full_name='SensorInfo.deactivation_date_null', index=6,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deactivation_date_val', full_name='SensorInfo.deactivation_date_val', index=7,
      number=9, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sensor_type', full_name='SensorInfo.sensor_type', index=8,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='company', full_name='SensorInfo.company', index=9,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='company_null', full_name='SensorInfo.company_null', index=10,
      number=12, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='controller_id', full_name='SensorInfo.controller_id', index=11,
      number=10, type=11, cpp_type=10, label=1,
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
    _descriptor.OneofDescriptor(
      name='name_oneof', full_name='SensorInfo.name_oneof',
      index=0, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='activation_date', full_name='SensorInfo.activation_date',
      index=1, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='deactivation_date', full_name='SensorInfo.deactivation_date',
      index=2, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='company_oneof', full_name='SensorInfo.company_oneof',
      index=3, containing_type=None, fields=[]),
  ],
  serialized_start=43,
  serialized_end=434,
)


_SENSORCREATE = _descriptor.Descriptor(
  name='SensorCreate',
  full_name='SensorCreate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sensor_type', full_name='SensorCreate.sensor_type', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='SensorCreate.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='company', full_name='SensorCreate.company', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='date', full_name='SensorCreate.date', index=3,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='controller_id', full_name='SensorCreate.controller_id', index=4,
      number=4, type=4, cpp_type=4, label=1,
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
  serialized_start=436,
  serialized_end=539,
)


_CONTROLLERINFO = _descriptor.Descriptor(
  name='ControllerInfo',
  full_name='ControllerInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ControllerInfo.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='ControllerInfo.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name_null', full_name='ControllerInfo.name_null', index=2,
      number=15, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='meta', full_name='ControllerInfo.meta', index=3,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='activation_date_val', full_name='ControllerInfo.activation_date_val', index=4,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='activation_date_null', full_name='ControllerInfo.activation_date_null', index=5,
      number=13, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='ControllerInfo.status', index=6,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mac', full_name='ControllerInfo.mac', index=7,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deactivation_date_null', full_name='ControllerInfo.deactivation_date_null', index=8,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deactivation_date_val', full_name='ControllerInfo.deactivation_date_val', index=9,
      number=10, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='controller_type', full_name='ControllerInfo.controller_type', index=10,
      number=8, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='object_id', full_name='ControllerInfo.object_id', index=11,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='object_id_null', full_name='ControllerInfo.object_id_null', index=12,
      number=14, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sensors', full_name='ControllerInfo.sensors', index=13,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
    _descriptor.OneofDescriptor(
      name='name_oneof', full_name='ControllerInfo.name_oneof',
      index=0, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='activation_date', full_name='ControllerInfo.activation_date',
      index=1, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='deactivation_date', full_name='ControllerInfo.deactivation_date',
      index=2, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='object_id_oneof', full_name='ControllerInfo.object_id_oneof',
      index=3, containing_type=None, fields=[]),
  ],
  serialized_start=542,
  serialized_end=981,
)


_CONTROLLERCREATE = _descriptor.Descriptor(
  name='ControllerCreate',
  full_name='ControllerCreate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mac', full_name='ControllerCreate.mac', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='controller_type', full_name='ControllerCreate.controller_type', index=1,
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
  serialized_start=983,
  serialized_end=1039,
)


_OBJECTINFO = _descriptor.Descriptor(
  name='ObjectInfo',
  full_name='ObjectInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ObjectInfo.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='ObjectInfo.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='address', full_name='ObjectInfo.address', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='controllers', full_name='ObjectInfo.controllers', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='ObjectInfo.user_id', index=4,
      number=5, type=11, cpp_type=10, label=1,
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
  serialized_start=1042,
  serialized_end=1172,
)


_USERINFOH = _descriptor.Descriptor(
  name='UserInfoH',
  full_name='UserInfoH',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='UserInfoH.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='objects', full_name='UserInfoH.objects', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=1174,
  serialized_end=1236,
)


_OBJECTCREATE = _descriptor.Descriptor(
  name='ObjectCreate',
  full_name='ObjectCreate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='ObjectCreate.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='address', full_name='ObjectCreate.address', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=1238,
  serialized_end=1283,
)


_CONTROLLERACTIVATE = _descriptor.Descriptor(
  name='ControllerActivate',
  full_name='ControllerActivate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ControllerActivate.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='ControllerActivate.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='meta', full_name='ControllerActivate.meta', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='object_id', full_name='ControllerActivate.object_id', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_start=1285,
  serialized_end=1390,
)

_SENSORINFO.fields_by_name['id'].message_type = proto_dot_utils__pb2._SENSORID
_SENSORINFO.fields_by_name['controller_id'].message_type = proto_dot_utils__pb2._CONTROLLERID
_SENSORINFO.oneofs_by_name['name_oneof'].fields.append(
  _SENSORINFO.fields_by_name['name'])
_SENSORINFO.fields_by_name['name'].containing_oneof = _SENSORINFO.oneofs_by_name['name_oneof']
_SENSORINFO.oneofs_by_name['name_oneof'].fields.append(
  _SENSORINFO.fields_by_name['name_null'])
_SENSORINFO.fields_by_name['name_null'].containing_oneof = _SENSORINFO.oneofs_by_name['name_oneof']
_SENSORINFO.oneofs_by_name['activation_date'].fields.append(
  _SENSORINFO.fields_by_name['activation_date_val'])
_SENSORINFO.fields_by_name['activation_date_val'].containing_oneof = _SENSORINFO.oneofs_by_name['activation_date']
_SENSORINFO.oneofs_by_name['activation_date'].fields.append(
  _SENSORINFO.fields_by_name['activation_date_null'])
_SENSORINFO.fields_by_name['activation_date_null'].containing_oneof = _SENSORINFO.oneofs_by_name['activation_date']
_SENSORINFO.oneofs_by_name['deactivation_date'].fields.append(
  _SENSORINFO.fields_by_name['deactivation_date_null'])
_SENSORINFO.fields_by_name['deactivation_date_null'].containing_oneof = _SENSORINFO.oneofs_by_name['deactivation_date']
_SENSORINFO.oneofs_by_name['deactivation_date'].fields.append(
  _SENSORINFO.fields_by_name['deactivation_date_val'])
_SENSORINFO.fields_by_name['deactivation_date_val'].containing_oneof = _SENSORINFO.oneofs_by_name['deactivation_date']
_SENSORINFO.oneofs_by_name['company_oneof'].fields.append(
  _SENSORINFO.fields_by_name['company'])
_SENSORINFO.fields_by_name['company'].containing_oneof = _SENSORINFO.oneofs_by_name['company_oneof']
_SENSORINFO.oneofs_by_name['company_oneof'].fields.append(
  _SENSORINFO.fields_by_name['company_null'])
_SENSORINFO.fields_by_name['company_null'].containing_oneof = _SENSORINFO.oneofs_by_name['company_oneof']
_CONTROLLERINFO.fields_by_name['id'].message_type = proto_dot_utils__pb2._CONTROLLERID
_CONTROLLERINFO.fields_by_name['object_id'].message_type = proto_dot_utils__pb2._OBJECTID
_CONTROLLERINFO.fields_by_name['sensors'].message_type = _SENSORINFO
_CONTROLLERINFO.oneofs_by_name['name_oneof'].fields.append(
  _CONTROLLERINFO.fields_by_name['name'])
_CONTROLLERINFO.fields_by_name['name'].containing_oneof = _CONTROLLERINFO.oneofs_by_name['name_oneof']
_CONTROLLERINFO.oneofs_by_name['name_oneof'].fields.append(
  _CONTROLLERINFO.fields_by_name['name_null'])
_CONTROLLERINFO.fields_by_name['name_null'].containing_oneof = _CONTROLLERINFO.oneofs_by_name['name_oneof']
_CONTROLLERINFO.oneofs_by_name['activation_date'].fields.append(
  _CONTROLLERINFO.fields_by_name['activation_date_val'])
_CONTROLLERINFO.fields_by_name['activation_date_val'].containing_oneof = _CONTROLLERINFO.oneofs_by_name['activation_date']
_CONTROLLERINFO.oneofs_by_name['activation_date'].fields.append(
  _CONTROLLERINFO.fields_by_name['activation_date_null'])
_CONTROLLERINFO.fields_by_name['activation_date_null'].containing_oneof = _CONTROLLERINFO.oneofs_by_name['activation_date']
_CONTROLLERINFO.oneofs_by_name['deactivation_date'].fields.append(
  _CONTROLLERINFO.fields_by_name['deactivation_date_null'])
_CONTROLLERINFO.fields_by_name['deactivation_date_null'].containing_oneof = _CONTROLLERINFO.oneofs_by_name['deactivation_date']
_CONTROLLERINFO.oneofs_by_name['deactivation_date'].fields.append(
  _CONTROLLERINFO.fields_by_name['deactivation_date_val'])
_CONTROLLERINFO.fields_by_name['deactivation_date_val'].containing_oneof = _CONTROLLERINFO.oneofs_by_name['deactivation_date']
_CONTROLLERINFO.oneofs_by_name['object_id_oneof'].fields.append(
  _CONTROLLERINFO.fields_by_name['object_id'])
_CONTROLLERINFO.fields_by_name['object_id'].containing_oneof = _CONTROLLERINFO.oneofs_by_name['object_id_oneof']
_CONTROLLERINFO.oneofs_by_name['object_id_oneof'].fields.append(
  _CONTROLLERINFO.fields_by_name['object_id_null'])
_CONTROLLERINFO.fields_by_name['object_id_null'].containing_oneof = _CONTROLLERINFO.oneofs_by_name['object_id_oneof']
_OBJECTINFO.fields_by_name['id'].message_type = proto_dot_utils__pb2._OBJECTID
_OBJECTINFO.fields_by_name['controllers'].message_type = _CONTROLLERINFO
_OBJECTINFO.fields_by_name['user_id'].message_type = proto_dot_utils__pb2._USERID
_USERINFOH.fields_by_name['id'].message_type = proto_dot_utils__pb2._USERID
_USERINFOH.fields_by_name['objects'].message_type = _OBJECTINFO
_CONTROLLERACTIVATE.fields_by_name['id'].message_type = proto_dot_utils__pb2._CONTROLLERID
_CONTROLLERACTIVATE.fields_by_name['object_id'].message_type = proto_dot_utils__pb2._OBJECTID
DESCRIPTOR.message_types_by_name['SensorInfo'] = _SENSORINFO
DESCRIPTOR.message_types_by_name['SensorCreate'] = _SENSORCREATE
DESCRIPTOR.message_types_by_name['ControllerInfo'] = _CONTROLLERINFO
DESCRIPTOR.message_types_by_name['ControllerCreate'] = _CONTROLLERCREATE
DESCRIPTOR.message_types_by_name['ObjectInfo'] = _OBJECTINFO
DESCRIPTOR.message_types_by_name['UserInfoH'] = _USERINFOH
DESCRIPTOR.message_types_by_name['ObjectCreate'] = _OBJECTCREATE
DESCRIPTOR.message_types_by_name['ControllerActivate'] = _CONTROLLERACTIVATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SensorInfo = _reflection.GeneratedProtocolMessageType('SensorInfo', (_message.Message,), dict(
  DESCRIPTOR = _SENSORINFO,
  __module__ = 'proto.objects_pb2'
  # @@protoc_insertion_point(class_scope:SensorInfo)
  ))
_sym_db.RegisterMessage(SensorInfo)

SensorCreate = _reflection.GeneratedProtocolMessageType('SensorCreate', (_message.Message,), dict(
  DESCRIPTOR = _SENSORCREATE,
  __module__ = 'proto.objects_pb2'
  # @@protoc_insertion_point(class_scope:SensorCreate)
  ))
_sym_db.RegisterMessage(SensorCreate)

ControllerInfo = _reflection.GeneratedProtocolMessageType('ControllerInfo', (_message.Message,), dict(
  DESCRIPTOR = _CONTROLLERINFO,
  __module__ = 'proto.objects_pb2'
  # @@protoc_insertion_point(class_scope:ControllerInfo)
  ))
_sym_db.RegisterMessage(ControllerInfo)

ControllerCreate = _reflection.GeneratedProtocolMessageType('ControllerCreate', (_message.Message,), dict(
  DESCRIPTOR = _CONTROLLERCREATE,
  __module__ = 'proto.objects_pb2'
  # @@protoc_insertion_point(class_scope:ControllerCreate)
  ))
_sym_db.RegisterMessage(ControllerCreate)

ObjectInfo = _reflection.GeneratedProtocolMessageType('ObjectInfo', (_message.Message,), dict(
  DESCRIPTOR = _OBJECTINFO,
  __module__ = 'proto.objects_pb2'
  # @@protoc_insertion_point(class_scope:ObjectInfo)
  ))
_sym_db.RegisterMessage(ObjectInfo)

UserInfoH = _reflection.GeneratedProtocolMessageType('UserInfoH', (_message.Message,), dict(
  DESCRIPTOR = _USERINFOH,
  __module__ = 'proto.objects_pb2'
  # @@protoc_insertion_point(class_scope:UserInfoH)
  ))
_sym_db.RegisterMessage(UserInfoH)

ObjectCreate = _reflection.GeneratedProtocolMessageType('ObjectCreate', (_message.Message,), dict(
  DESCRIPTOR = _OBJECTCREATE,
  __module__ = 'proto.objects_pb2'
  # @@protoc_insertion_point(class_scope:ObjectCreate)
  ))
_sym_db.RegisterMessage(ObjectCreate)

ControllerActivate = _reflection.GeneratedProtocolMessageType('ControllerActivate', (_message.Message,), dict(
  DESCRIPTOR = _CONTROLLERACTIVATE,
  __module__ = 'proto.objects_pb2'
  # @@protoc_insertion_point(class_scope:ControllerActivate)
  ))
_sym_db.RegisterMessage(ControllerActivate)



_OBJECTSERVICE = _descriptor.ServiceDescriptor(
  name='ObjectService',
  full_name='ObjectService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=1393,
  serialized_end=1974,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetUsersInfo',
    full_name='ObjectService.GetUsersInfo',
    index=0,
    containing_service=None,
    input_type=proto_dot_utils__pb2._USERID,
    output_type=_USERINFOH,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetControllerInfo',
    full_name='ObjectService.GetControllerInfo',
    index=1,
    containing_service=None,
    input_type=proto_dot_utils__pb2._CONTROLLERID,
    output_type=_CONTROLLERINFO,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetSensorInfo',
    full_name='ObjectService.GetSensorInfo',
    index=2,
    containing_service=None,
    input_type=proto_dot_utils__pb2._SENSORID,
    output_type=_SENSORINFO,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetObjectInfo',
    full_name='ObjectService.GetObjectInfo',
    index=3,
    containing_service=None,
    input_type=proto_dot_utils__pb2._OBJECTID,
    output_type=_OBJECTINFO,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CreateObject',
    full_name='ObjectService.CreateObject',
    index=4,
    containing_service=None,
    input_type=_OBJECTCREATE,
    output_type=_OBJECTINFO,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CreateController',
    full_name='ObjectService.CreateController',
    index=5,
    containing_service=None,
    input_type=_CONTROLLERCREATE,
    output_type=_CONTROLLERINFO,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CreateSensor',
    full_name='ObjectService.CreateSensor',
    index=6,
    containing_service=None,
    input_type=_SENSORCREATE,
    output_type=_SENSORINFO,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ActivateController',
    full_name='ObjectService.ActivateController',
    index=7,
    containing_service=None,
    input_type=_CONTROLLERACTIVATE,
    output_type=_CONTROLLERINFO,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteObject',
    full_name='ObjectService.DeleteObject',
    index=8,
    containing_service=None,
    input_type=proto_dot_utils__pb2._OBJECTID,
    output_type=proto_dot_utils__pb2._VOID,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteSensor',
    full_name='ObjectService.DeleteSensor',
    index=9,
    containing_service=None,
    input_type=proto_dot_utils__pb2._SENSORID,
    output_type=proto_dot_utils__pb2._VOID,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteController',
    full_name='ObjectService.DeleteController',
    index=10,
    containing_service=None,
    input_type=proto_dot_utils__pb2._CONTROLLERID,
    output_type=proto_dot_utils__pb2._VOID,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DeactivateController',
    full_name='ObjectService.DeactivateController',
    index=11,
    containing_service=None,
    input_type=proto_dot_utils__pb2._CONTROLLERID,
    output_type=_CONTROLLERINFO,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_OBJECTSERVICE)

DESCRIPTOR.services_by_name['ObjectService'] = _OBJECTSERVICE

# @@protoc_insertion_point(module_scope)