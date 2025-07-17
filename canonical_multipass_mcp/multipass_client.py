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

    def list(self, verbosity=0, snapshots=False, request_ipv4=False):
        def request_iterator():
            yield ListRequest(
                verbosity_level=verbosity,
                snapshots=snapshots,
                request_ipv4=request_ipv4
            )
        for resp in self._stub.list(request_iterator()):
            yield resp


