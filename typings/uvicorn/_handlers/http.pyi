"""
This type stub file was generated by pyright.
"""

import asyncio
from typing import TYPE_CHECKING
from uvicorn.config import Config
from uvicorn.server import ServerState

if TYPE_CHECKING: ...

async def handle_http(
    reader: asyncio.StreamReader,
    writer: asyncio.StreamWriter,
    server_state: ServerState,
    config: Config,
) -> None: ...