"""
This type stub file was generated by pyright.
"""

import signal
from socket import socket
from types import FrameType
from typing import Callable, List, Optional
from uvicorn.config import Config

HANDLED_SIGNALS = ...
logger = ...

class BaseReload:
    def __init__(
        self,
        config: Config,
        target: Callable[[Optional[List[socket]]], None],
        sockets: List[socket],
    ) -> None: ...
    def signal_handler(self, sig: signal.Signals, frame: FrameType) -> None:
        """
        A signal handler that is registered with the parent process.
        """
        ...
    def run(self) -> None: ...
    def startup(self) -> None: ...
    def restart(self) -> None: ...
    def shutdown(self) -> None: ...
    def should_restart(self) -> bool: ...
