# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from proto import stats_pb2 as proto_dot_stats__pb2
from proto import utils_pb2 as proto_dot_utils__pb2


class StatsServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetSensorStat = channel.unary_unary(
        '/StatsService/GetSensorStat',
        request_serializer=proto_dot_utils__pb2.SensorId.SerializeToString,
        response_deserializer=proto_dot_stats__pb2.SensorStat.FromString,
        )
    self.GetObjectStat = channel.unary_unary(
        '/StatsService/GetObjectStat',
        request_serializer=proto_dot_utils__pb2.ObjectId.SerializeToString,
        response_deserializer=proto_dot_stats__pb2.ObjectStat.FromString,
        )
    self.GetControllerStat = channel.unary_unary(
        '/StatsService/GetControllerStat',
        request_serializer=proto_dot_utils__pb2.ControllerId.SerializeToString,
        response_deserializer=proto_dot_stats__pb2.ControllerStat.FromString,
        )


class StatsServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetSensorStat(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetObjectStat(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetControllerStat(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_StatsServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetSensorStat': grpc.unary_unary_rpc_method_handler(
          servicer.GetSensorStat,
          request_deserializer=proto_dot_utils__pb2.SensorId.FromString,
          response_serializer=proto_dot_stats__pb2.SensorStat.SerializeToString,
      ),
      'GetObjectStat': grpc.unary_unary_rpc_method_handler(
          servicer.GetObjectStat,
          request_deserializer=proto_dot_utils__pb2.ObjectId.FromString,
          response_serializer=proto_dot_stats__pb2.ObjectStat.SerializeToString,
      ),
      'GetControllerStat': grpc.unary_unary_rpc_method_handler(
          servicer.GetControllerStat,
          request_deserializer=proto_dot_utils__pb2.ControllerId.FromString,
          response_serializer=proto_dot_stats__pb2.ControllerStat.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'StatsService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
