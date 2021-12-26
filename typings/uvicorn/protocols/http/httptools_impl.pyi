"""
This type stub file was generated by pyright.
"""

import asyncio
from typing import Callable

HEADER_RE = ...
HEADER_VALUE_RE = ...
STATUS_LINE = ...

class HttpToolsProtocol(asyncio.Protocol):
    def __init__(
        self, config, server_state, on_connection_lost: Callable = ..., _loop=...
    ) -> None: ...
    def connection_made(self, transport): ...
    def connection_lost(self, exc): ...
    def eof_received(self): ...
    def data_received(self, data): ...
    def handle_upgrade(self): ...
    def on_url(self, url): ...
    def on_header(self, name: bytes, value: bytes): ...
    def on_headers_complete(self): ...
    def on_body(self, body: bytes): ...
    def on_message_complete(self): ...
    def on_response_complete(self): ...
    def shutdown(self):  # -> None:
        """
        Called by the server to commence a graceful shutdown.
        """
        ...
    def pause_writing(self):  # -> None:
        """
        Called by the transport when the write buffer exceeds the high water mark.
        """
        ...
    def resume_writing(self):  # -> None:
        """
        Called by the transport when the write buffer drops below the low water mark.
        """
        ...
    def timeout_keep_alive_handler(self):  # -> None:
        """
        Called on a keep-alive connection if no new data is received after a short
        delay.
        """
        ...

class RequestResponseCycle:
    def __init__(
        self,
        scope,
        transport,
        flow,
        logger,
        access_logger,
        access_log,
        default_headers,
        message_event,
        expect_100_continue,
        keep_alive,
        on_response,
    ) -> None: ...
    async def run_asgi(self, app): ...
    async def send_500_response(self): ...
    async def send(self, message): ...
    async def receive(self): ...
