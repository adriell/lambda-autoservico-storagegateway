# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import engine_pb2 as engine__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class EngineStub(object):
  """Engine is an auxiliary service offered to language and resource provider plugins. Its main purpose today is
  to serve as a common logging endpoint, but it also serves as a state storage mechanism for language hosts
  that can't store their own global state.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Log = channel.unary_unary(
        '/pulumirpc.Engine/Log',
        request_serializer=engine__pb2.LogRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.GetRootResource = channel.unary_unary(
        '/pulumirpc.Engine/GetRootResource',
        request_serializer=engine__pb2.GetRootResourceRequest.SerializeToString,
        response_deserializer=engine__pb2.GetRootResourceResponse.FromString,
        )
    self.SetRootResource = channel.unary_unary(
        '/pulumirpc.Engine/SetRootResource',
        request_serializer=engine__pb2.SetRootResourceRequest.SerializeToString,
        response_deserializer=engine__pb2.SetRootResourceResponse.FromString,
        )


class EngineServicer(object):
  """Engine is an auxiliary service offered to language and resource provider plugins. Its main purpose today is
  to serve as a common logging endpoint, but it also serves as a state storage mechanism for language hosts
  that can't store their own global state.
  """

  def Log(self, request, context):
    """Log logs a global message in the engine, including errors and warnings.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetRootResource(self, request, context):
    """GetRootResource gets the URN of the root resource, the resource that should be the root of all
    otherwise-unparented resources.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetRootResource(self, request, context):
    """SetRootResource sets the URN of the root resource.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_EngineServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Log': grpc.unary_unary_rpc_method_handler(
          servicer.Log,
          request_deserializer=engine__pb2.LogRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'GetRootResource': grpc.unary_unary_rpc_method_handler(
          servicer.GetRootResource,
          request_deserializer=engine__pb2.GetRootResourceRequest.FromString,
          response_serializer=engine__pb2.GetRootResourceResponse.SerializeToString,
      ),
      'SetRootResource': grpc.unary_unary_rpc_method_handler(
          servicer.SetRootResource,
          request_deserializer=engine__pb2.SetRootResourceRequest.FromString,
          response_serializer=engine__pb2.SetRootResourceResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'pulumirpc.Engine', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))