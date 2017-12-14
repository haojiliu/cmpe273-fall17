# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import token_pb2 as token__pb2


class TokenStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.transfer = channel.unary_unary(
        '/Token/transfer',
        request_serializer=token__pb2.TransferRequest.SerializeToString,
        response_deserializer=token__pb2.TransferResponse.FromString,
        )
    self.info = channel.unary_unary(
        '/Token/info',
        request_serializer=token__pb2.Empty.SerializeToString,
        response_deserializer=token__pb2.InfoResponse.FromString,
        )


class TokenServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def transfer(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def info(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_TokenServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'transfer': grpc.unary_unary_rpc_method_handler(
          servicer.transfer,
          request_deserializer=token__pb2.TransferRequest.FromString,
          response_serializer=token__pb2.TransferResponse.SerializeToString,
      ),
      'info': grpc.unary_unary_rpc_method_handler(
          servicer.info,
          request_deserializer=token__pb2.Empty.FromString,
          response_serializer=token__pb2.InfoResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Token', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))