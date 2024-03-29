# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from proto import companies_pb2 as proto_dot_companies__pb2
from proto import utils_pb2 as proto_dot_utils__pb2


class CompanyStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetCompanyInfo = channel.unary_unary(
        '/Company/GetCompanyInfo',
        request_serializer=proto_dot_utils__pb2.CompanyId.SerializeToString,
        response_deserializer=proto_dot_companies__pb2.CompanyInfo.FromString,
        )
    self.GetTariffInfo = channel.unary_unary(
        '/Company/GetTariffInfo',
        request_serializer=proto_dot_utils__pb2.TariffId.SerializeToString,
        response_deserializer=proto_dot_companies__pb2.TariffInfo.FromString,
        )
    self.GetCompanyExtendedInfo = channel.unary_unary(
        '/Company/GetCompanyExtendedInfo',
        request_serializer=proto_dot_utils__pb2.CompanyId.SerializeToString,
        response_deserializer=proto_dot_companies__pb2.CompanyExtendedInfo.FromString,
        )


class CompanyServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetCompanyInfo(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetTariffInfo(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetCompanyExtendedInfo(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_CompanyServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetCompanyInfo': grpc.unary_unary_rpc_method_handler(
          servicer.GetCompanyInfo,
          request_deserializer=proto_dot_utils__pb2.CompanyId.FromString,
          response_serializer=proto_dot_companies__pb2.CompanyInfo.SerializeToString,
      ),
      'GetTariffInfo': grpc.unary_unary_rpc_method_handler(
          servicer.GetTariffInfo,
          request_deserializer=proto_dot_utils__pb2.TariffId.FromString,
          response_serializer=proto_dot_companies__pb2.TariffInfo.SerializeToString,
      ),
      'GetCompanyExtendedInfo': grpc.unary_unary_rpc_method_handler(
          servicer.GetCompanyExtendedInfo,
          request_deserializer=proto_dot_utils__pb2.CompanyId.FromString,
          response_serializer=proto_dot_companies__pb2.CompanyExtendedInfo.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Company', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
