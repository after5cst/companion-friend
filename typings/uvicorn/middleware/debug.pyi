"""
This type stub file was generated by pyright.
"""

from asgiref.typing import (
    ASGI3Application,
    ASGIReceiveCallable,
    ASGISendCallable,
    WWWScope,
)

class HTMLResponse:
    def __init__(self, content: str, status_code: int) -> None: ...
    async def __call__(
        self, scope: WWWScope, receive: ASGIReceiveCallable, send: ASGISendCallable
    ) -> None: ...

class PlainTextResponse:
    def __init__(self, content: str, status_code: int) -> None: ...
    async def __call__(
        self, scope: WWWScope, receive: ASGIReceiveCallable, send: ASGISendCallable
    ) -> None: ...

def get_accept_header(scope: WWWScope) -> str: ...

class DebugMiddleware:
    def __init__(self, app: ASGI3Application) -> None: ...
    async def __call__(
        self, scope: WWWScope, receive: ASGIReceiveCallable, send: ASGISendCallable
    ) -> None: ...
