# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import get_nex_password_rpc_pb2 as get__nex__password__rpc__pb2
from . import get_user_data_rpc_pb2 as get__user__data__rpc__pb2


class AccountStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetUserData = channel.unary_unary(
                '/account.Account/GetUserData',
                request_serializer=get__user__data__rpc__pb2.GetUserDataRequest.SerializeToString,
                response_deserializer=get__user__data__rpc__pb2.GetUserDataResponse.FromString,
                )
        self.GetNEXPassword = channel.unary_unary(
                '/account.Account/GetNEXPassword',
                request_serializer=get__nex__password__rpc__pb2.GetNEXPasswordRequest.SerializeToString,
                response_deserializer=get__nex__password__rpc__pb2.GetNEXPasswordResponse.FromString,
                )


class AccountServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetUserData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetNEXPassword(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AccountServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetUserData': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUserData,
                    request_deserializer=get__user__data__rpc__pb2.GetUserDataRequest.FromString,
                    response_serializer=get__user__data__rpc__pb2.GetUserDataResponse.SerializeToString,
            ),
            'GetNEXPassword': grpc.unary_unary_rpc_method_handler(
                    servicer.GetNEXPassword,
                    request_deserializer=get__nex__password__rpc__pb2.GetNEXPasswordRequest.FromString,
                    response_serializer=get__nex__password__rpc__pb2.GetNEXPasswordResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'account.Account', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Account(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetUserData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/account.Account/GetUserData',
            get__user__data__rpc__pb2.GetUserDataRequest.SerializeToString,
            get__user__data__rpc__pb2.GetUserDataResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetNEXPassword(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/account.Account/GetNEXPassword',
            get__nex__password__rpc__pb2.GetNEXPasswordRequest.SerializeToString,
            get__nex__password__rpc__pb2.GetNEXPasswordResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
