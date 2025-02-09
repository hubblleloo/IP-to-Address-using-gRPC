# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ip_to_address.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ip_to_address.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x13ip_to_address.proto\"\x10\n\x02Ip\x12\n\n\x02ip\x18\x01 \x01(\t2)\n\nIpLocation\x12\x1b\n\rGetLocationIp\x12\x03.Ip\x1a\x03.Ip\"\x00\x62\x06proto3')
)




_IP = _descriptor.Descriptor(
  name='Ip',
  full_name='Ip',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ip', full_name='Ip.ip', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=23,
  serialized_end=39,
)

DESCRIPTOR.message_types_by_name['Ip'] = _IP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Ip = _reflection.GeneratedProtocolMessageType('Ip', (_message.Message,), {
  'DESCRIPTOR' : _IP,
  '__module__' : 'ip_to_address_pb2'
  # @@protoc_insertion_point(class_scope:Ip)
  })
_sym_db.RegisterMessage(Ip)



_IPLOCATION = _descriptor.ServiceDescriptor(
  name='IpLocation',
  full_name='IpLocation',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=41,
  serialized_end=82,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetLocationIp',
    full_name='IpLocation.GetLocationIp',
    index=0,
    containing_service=None,
    input_type=_IP,
    output_type=_IP,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_IPLOCATION)

DESCRIPTOR.services_by_name['IpLocation'] = _IPLOCATION

# @@protoc_insertion_point(module_scope)
