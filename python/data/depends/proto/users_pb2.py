# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/users.proto

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
  name='proto/users.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x11proto/users.proto\x1a\x11proto/utils.proto\"R\n\x0cPassportInfo\x12\x11\n\tissued_by\x18\x01 \x01(\t\x12\x17\n\x0f\x64ivision_number\x18\x02 \x01(\t\x12\x16\n\x0e\x64\x61te_receiving\x18\x03 \x01(\x04\"\x87\x02\n\x08UserInfo\x12\x13\n\x0b\x66\x61mily_name\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0bsecond_name\x18\x03 \x01(\t\x12\x1f\n\x08passport\x18\x04 \x01(\x0b\x32\r.PassportInfo\x12\x1b\n\x13registration_addres\x18\x05 \x01(\t\x12\x16\n\x0emailing_addres\x18\x06 \x01(\t\x12\x11\n\tbirth_day\x18\x07 \x01(\t\x12\x0b\n\x03sex\x18\x08 \x01(\x08\x12\x12\n\nhome_phone\x18\t \x01(\t\x12\x14\n\x0cmobile_phone\x18\n \x01(\t\x12\x13\n\x0b\x63itizenship\x18\x0b \x01(\t\x12\x0e\n\x06\x65_mail\x18\x0c \x01(\t26\n\x0fUserInfoService\x12#\n\x0bGetUserInfo\x12\x07.UserId\x1a\t.UserInfo\"\x00\x62\x06proto3')
  ,
  dependencies=[proto_dot_utils__pb2.DESCRIPTOR,])




_PASSPORTINFO = _descriptor.Descriptor(
  name='PassportInfo',
  full_name='PassportInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='issued_by', full_name='PassportInfo.issued_by', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='division_number', full_name='PassportInfo.division_number', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='date_receiving', full_name='PassportInfo.date_receiving', index=2,
      number=3, type=4, cpp_type=4, label=1,
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
  serialized_start=40,
  serialized_end=122,
)


_USERINFO = _descriptor.Descriptor(
  name='UserInfo',
  full_name='UserInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='family_name', full_name='UserInfo.family_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='UserInfo.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='second_name', full_name='UserInfo.second_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='passport', full_name='UserInfo.passport', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='registration_addres', full_name='UserInfo.registration_addres', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mailing_addres', full_name='UserInfo.mailing_addres', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='birth_day', full_name='UserInfo.birth_day', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sex', full_name='UserInfo.sex', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='home_phone', full_name='UserInfo.home_phone', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mobile_phone', full_name='UserInfo.mobile_phone', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='citizenship', full_name='UserInfo.citizenship', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='e_mail', full_name='UserInfo.e_mail', index=11,
      number=12, type=9, cpp_type=9, label=1,
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
  serialized_start=125,
  serialized_end=388,
)

_USERINFO.fields_by_name['passport'].message_type = _PASSPORTINFO
DESCRIPTOR.message_types_by_name['PassportInfo'] = _PASSPORTINFO
DESCRIPTOR.message_types_by_name['UserInfo'] = _USERINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PassportInfo = _reflection.GeneratedProtocolMessageType('PassportInfo', (_message.Message,), dict(
  DESCRIPTOR = _PASSPORTINFO,
  __module__ = 'proto.users_pb2'
  # @@protoc_insertion_point(class_scope:PassportInfo)
  ))
_sym_db.RegisterMessage(PassportInfo)

UserInfo = _reflection.GeneratedProtocolMessageType('UserInfo', (_message.Message,), dict(
  DESCRIPTOR = _USERINFO,
  __module__ = 'proto.users_pb2'
  # @@protoc_insertion_point(class_scope:UserInfo)
  ))
_sym_db.RegisterMessage(UserInfo)



_USERINFOSERVICE = _descriptor.ServiceDescriptor(
  name='UserInfoService',
  full_name='UserInfoService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=390,
  serialized_end=444,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetUserInfo',
    full_name='UserInfoService.GetUserInfo',
    index=0,
    containing_service=None,
    input_type=proto_dot_utils__pb2._USERID,
    output_type=_USERINFO,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_USERINFOSERVICE)

DESCRIPTOR.services_by_name['UserInfoService'] = _USERINFOSERVICE

# @@protoc_insertion_point(module_scope)
