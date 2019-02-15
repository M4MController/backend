# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from proto import objects_pb2 as proto_dot_objects__pb2
from proto import utils_pb2 as proto_dot_utils__pb2


class ObjectServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetUsersInfo = channel.unary_unary(
        '/ObjectService/GetUsersInfo',
        request_serializer=proto_dot_utils__pb2.UserId.SerializeToString,
        response_deserializer=proto_dot_objects__pb2.UserInfoH.FromString,
        )
    self.GetControllerInfo = channel.unary_unary(
        '/ObjectService/GetControllerInfo',
        request_serializer=proto_dot_utils__pb2.ControllerId.SerializeToString,
        response_deserializer=proto_dot_objects__pb2.ControllerInfo.FromString,
        )
    self.GetSensorInfo = channel.unary_unary(
        '/ObjectService/GetSensorInfo',
        request_serializer=proto_dot_utils__pb2.SensorId.SerializeToString,
        response_deserializer=proto_dot_objects__pb2.SensorInfo.FromString,
        )
    self.GetObjectInfo = channel.unary_unary(
        '/ObjectService/GetObjectInfo',
        request_serializer=proto_dot_utils__pb2.ObjectId.SerializeToString,
        response_deserializer=proto_dot_objects__pb2.ObjectInfo.FromString,
        )
    self.CreateObject = channel.unary_unary(
        '/ObjectService/CreateObject',
        request_serializer=proto_dot_objects__pb2.ObjectCreate.SerializeToString,
        response_deserializer=proto_dot_objects__pb2.ObjectInfo.FromString,
        )
    self.CreateController = channel.unary_unary(
        '/ObjectService/CreateController',
        request_serializer=proto_dot_objects__pb2.ControllerCreate.SerializeToString,
        response_deserializer=proto_dot_objects__pb2.ControllerInfo.FromString,
        )
    self.CreateSensor = channel.unary_unary(
        '/ObjectService/CreateSensor',
        request_serializer=proto_dot_objects__pb2.SensorCreate.SerializeToString,
        response_deserializer=proto_dot_objects__pb2.SensorInfo.FromString,
        )
    self.ActivateController = channel.unary_unary(
        '/ObjectService/ActivateController',
        request_serializer=proto_dot_objects__pb2.ControllerActivate.SerializeToString,
        response_deserializer=proto_dot_objects__pb2.ControllerInfo.FromString,
        )
    self.DeleteObject = channel.unary_unary(
        '/ObjectService/DeleteObject',
        request_serializer=proto_dot_utils__pb2.ObjectId.SerializeToString,
        response_deserializer=proto_dot_utils__pb2.Void.FromString,
        )
    self.DeleteSensor = channel.unary_unary(
        '/ObjectService/DeleteSensor',
        request_serializer=proto_dot_utils__pb2.SensorId.SerializeToString,
        response_deserializer=proto_dot_utils__pb2.Void.FromString,
        )
    self.DeleteController = channel.unary_unary(
        '/ObjectService/DeleteController',
        request_serializer=proto_dot_utils__pb2.ControllerId.SerializeToString,
        response_deserializer=proto_dot_utils__pb2.Void.FromString,
        )
    self.DeactivateController = channel.unary_unary(
        '/ObjectService/DeactivateController',
        request_serializer=proto_dot_utils__pb2.ControllerId.SerializeToString,
        response_deserializer=proto_dot_objects__pb2.ControllerInfo.FromString,
        )


class ObjectServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetUsersInfo(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetControllerInfo(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetSensorInfo(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetObjectInfo(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateObject(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateController(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateSensor(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ActivateController(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteObject(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteSensor(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteController(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeactivateController(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ObjectServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetUsersInfo': grpc.unary_unary_rpc_method_handler(
          servicer.GetUsersInfo,
          request_deserializer=proto_dot_utils__pb2.UserId.FromString,
          response_serializer=proto_dot_objects__pb2.UserInfoH.SerializeToString,
      ),
      'GetControllerInfo': grpc.unary_unary_rpc_method_handler(
          servicer.GetControllerInfo,
          request_deserializer=proto_dot_utils__pb2.ControllerId.FromString,
          response_serializer=proto_dot_objects__pb2.ControllerInfo.SerializeToString,
      ),
      'GetSensorInfo': grpc.unary_unary_rpc_method_handler(
          servicer.GetSensorInfo,
          request_deserializer=proto_dot_utils__pb2.SensorId.FromString,
          response_serializer=proto_dot_objects__pb2.SensorInfo.SerializeToString,
      ),
      'GetObjectInfo': grpc.unary_unary_rpc_method_handler(
          servicer.GetObjectInfo,
          request_deserializer=proto_dot_utils__pb2.ObjectId.FromString,
          response_serializer=proto_dot_objects__pb2.ObjectInfo.SerializeToString,
      ),
      'CreateObject': grpc.unary_unary_rpc_method_handler(
          servicer.CreateObject,
          request_deserializer=proto_dot_objects__pb2.ObjectCreate.FromString,
          response_serializer=proto_dot_objects__pb2.ObjectInfo.SerializeToString,
      ),
      'CreateController': grpc.unary_unary_rpc_method_handler(
          servicer.CreateController,
          request_deserializer=proto_dot_objects__pb2.ControllerCreate.FromString,
          response_serializer=proto_dot_objects__pb2.ControllerInfo.SerializeToString,
      ),
      'CreateSensor': grpc.unary_unary_rpc_method_handler(
          servicer.CreateSensor,
          request_deserializer=proto_dot_objects__pb2.SensorCreate.FromString,
          response_serializer=proto_dot_objects__pb2.SensorInfo.SerializeToString,
      ),
      'ActivateController': grpc.unary_unary_rpc_method_handler(
          servicer.ActivateController,
          request_deserializer=proto_dot_objects__pb2.ControllerActivate.FromString,
          response_serializer=proto_dot_objects__pb2.ControllerInfo.SerializeToString,
      ),
      'DeleteObject': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteObject,
          request_deserializer=proto_dot_utils__pb2.ObjectId.FromString,
          response_serializer=proto_dot_utils__pb2.Void.SerializeToString,
      ),
      'DeleteSensor': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteSensor,
          request_deserializer=proto_dot_utils__pb2.SensorId.FromString,
          response_serializer=proto_dot_utils__pb2.Void.SerializeToString,
      ),
      'DeleteController': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteController,
          request_deserializer=proto_dot_utils__pb2.ControllerId.FromString,
          response_serializer=proto_dot_utils__pb2.Void.SerializeToString,
      ),
      'DeactivateController': grpc.unary_unary_rpc_method_handler(
          servicer.DeactivateController,
          request_deserializer=proto_dot_utils__pb2.ControllerId.FromString,
          response_serializer=proto_dot_objects__pb2.ControllerInfo.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'ObjectService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))