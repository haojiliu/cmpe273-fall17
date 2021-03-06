# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: replicator.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='replicator.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x10replicator.proto\"^\n\x07Request\x12\x18\n\x03\x63md\x18\x01 \x01(\x0e\x32\x0b.RocksDBCmd\x12\x10\n\x08\x61rgument\x18\x02 \x01(\t\x12\x16\n\x0emerkleRootHash\x18\x03 \x01(\t\x12\x0f\n\x07\x63mdHash\x18\x04 \x01(\t\"\x1a\n\x08Response\x12\x0e\n\x06result\x18\x01 \x01(\x08*.\n\nRocksDBCmd\x12\x0b\n\x07unknown\x10\x00\x12\x07\n\x03put\x10\x01\x12\n\n\x06\x64\x65lete\x10\x02\x32+\n\nReplicator\x12\x1d\n\x04send\x12\x08.Request\x1a\t.Response\"\x00\x62\x06proto3')
)

_ROCKSDBCMD = _descriptor.EnumDescriptor(
  name='RocksDBCmd',
  full_name='RocksDBCmd',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='unknown', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='put', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='delete', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=144,
  serialized_end=190,
)
_sym_db.RegisterEnumDescriptor(_ROCKSDBCMD)

RocksDBCmd = enum_type_wrapper.EnumTypeWrapper(_ROCKSDBCMD)
unknown = 0
put = 1
delete = 2



_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cmd', full_name='Request.cmd', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='argument', full_name='Request.argument', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='merkleRootHash', full_name='Request.merkleRootHash', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cmdHash', full_name='Request.cmdHash', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=20,
  serialized_end=114,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='Response.result', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=116,
  serialized_end=142,
)

_REQUEST.fields_by_name['cmd'].enum_type = _ROCKSDBCMD
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
DESCRIPTOR.enum_types_by_name['RocksDBCmd'] = _ROCKSDBCMD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
  DESCRIPTOR = _REQUEST,
  __module__ = 'replicator_pb2'
  # @@protoc_insertion_point(class_scope:Request)
  ))
_sym_db.RegisterMessage(Request)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSE,
  __module__ = 'replicator_pb2'
  # @@protoc_insertion_point(class_scope:Response)
  ))
_sym_db.RegisterMessage(Response)



_REPLICATOR = _descriptor.ServiceDescriptor(
  name='Replicator',
  full_name='Replicator',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=192,
  serialized_end=235,
  methods=[
  _descriptor.MethodDescriptor(
    name='send',
    full_name='Replicator.send',
    index=0,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_REPLICATOR)

DESCRIPTOR.services_by_name['Replicator'] = _REPLICATOR

try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities


  class ReplicatorStub(object):
    # missing associated documentation comment in .proto file
    pass

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.send = channel.unary_unary(
          '/Replicator/send',
          request_serializer=Request.SerializeToString,
          response_deserializer=Response.FromString,
          )


  class ReplicatorServicer(object):
    # missing associated documentation comment in .proto file
    pass

    def send(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')


  def add_ReplicatorServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'send': grpc.unary_unary_rpc_method_handler(
            servicer.send,
            request_deserializer=Request.FromString,
            response_serializer=Response.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'Replicator', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaReplicatorServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    # missing associated documentation comment in .proto file
    pass
    def send(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaReplicatorStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    # missing associated documentation comment in .proto file
    pass
    def send(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      # missing associated documentation comment in .proto file
      pass
      raise NotImplementedError()
    send.future = None


  def beta_create_Replicator_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('Replicator', 'send'): Request.FromString,
    }
    response_serializers = {
      ('Replicator', 'send'): Response.SerializeToString,
    }
    method_implementations = {
      ('Replicator', 'send'): face_utilities.unary_unary_inline(servicer.send),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_Replicator_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('Replicator', 'send'): Request.SerializeToString,
    }
    response_deserializers = {
      ('Replicator', 'send'): Response.FromString,
    }
    cardinalities = {
      'send': cardinality.Cardinality.UNARY_UNARY,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'Replicator', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
