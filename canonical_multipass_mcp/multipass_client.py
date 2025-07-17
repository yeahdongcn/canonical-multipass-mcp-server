import grpc

from .multipass_pb2_grpc import RpcStub
from .multipass_pb2 import ListRequest, ListReply

class MultipassClient:
    def __init__(
        self,
        server_addr: str,
    ):
        self._server_addr = server_addr
        self._channel = grpc.insecure_channel(self._server_addr)
        self._stub = RpcStub(self._channel)

    def list(self):
        return self._stub.list(ListRequest())


