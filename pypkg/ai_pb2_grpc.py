"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings
from . import ai_pb2 as ai__pb2
GRPC_GENERATED_VERSION = '1.71.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False
try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True
if _version_not_supported:
    raise RuntimeError(f'The grpc package installed is at version {GRPC_VERSION},' + f' but the generated code in ai_pb2_grpc.py depends on' + f' grpcio>={GRPC_GENERATED_VERSION}.' + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}' + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.')

class AiStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetSuggest = channel.unary_unary('/pypkg.Ai/GetSuggest', request_serializer=ai__pb2.SuggestRequest.SerializeToString, response_deserializer=ai__pb2.SuggestResponse.FromString, _registered_method=True)
        self.ClearHistory = channel.unary_unary('/pypkg.Ai/ClearHistory', request_serializer=ai__pb2.ClearHistoryRequest.SerializeToString, response_deserializer=ai__pb2.ClearHistoryResponse.FromString, _registered_method=True)

class AiServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetSuggest(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ClearHistory(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_AiServicer_to_server(servicer, server):
    rpc_method_handlers = {'GetSuggest': grpc.unary_unary_rpc_method_handler(servicer.GetSuggest, request_deserializer=ai__pb2.SuggestRequest.FromString, response_serializer=ai__pb2.SuggestResponse.SerializeToString), 'ClearHistory': grpc.unary_unary_rpc_method_handler(servicer.ClearHistory, request_deserializer=ai__pb2.ClearHistoryRequest.FromString, response_serializer=ai__pb2.ClearHistoryResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('pypkg.Ai', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('pypkg.Ai', rpc_method_handlers)

class Ai(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetSuggest(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pypkg.Ai/GetSuggest', ai__pb2.SuggestRequest.SerializeToString, ai__pb2.SuggestResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ClearHistory(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pypkg.Ai/ClearHistory', ai__pb2.ClearHistoryRequest.SerializeToString, ai__pb2.ClearHistoryResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)