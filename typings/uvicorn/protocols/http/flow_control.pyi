"""
This type stub file was generated by pyright.
"""

import asyncio
from asgiref.typing import ASGIReceiveCallable, ASGISendCallable, Scope

CLOSE_HEADER = ...
HIGH_WATER_LIMIT = ...

class FlowControl:
    def __init__(self, transport: asyncio.Transport) -> None: ...
    async def drain(self) -> None: ...
    def pause_reading(self) -> None: ...
    def resume_reading(self) -> None: ...
    def pause_writing(self) -> None: ...
    def resume_writing(self) -> None: ...

async def service_unavailable(
    scope: Scope, receive: ASGIReceiveCallable, send: ASGISendCallable
) -> None: ...
