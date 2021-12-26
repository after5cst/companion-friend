"""
This type stub file was generated by pyright.
"""

from typing import Any, Generator, List, Tuple, Union, overload
from types import FunctionType
from pythonosc.osc_message import OscMessage

"""Maps OSC addresses to handler functions
"""

class Handler:
    """Wrapper for a callback function that will be called when an OSC message is sent to the right address.

    Represents a handler callback function that will be called whenever an OSC message is sent to the address this
    handler is mapped to. It passes the address, the fixed arguments (if any) as well as all osc arguments from the
    message if any were passed.
    """

    def __init__(
        self,
        _callback: FunctionType,
        _args: Union[Any, List[Any]],
        _needs_reply_address: bool = ...,
    ) -> None:
        """
        Args:
            _callback Function that is called when handler is invoked
            _args: Message causing invocation
            _needs_reply_address Whether the client's ip address shall be passed as an argument or not
        """
        ...
    def __eq__(self, other) -> bool: ...
    def invoke(self, client_address: str, message: OscMessage) -> None:
        """Invokes the associated callback function

        Args:
            client_address: Address match that causes the invocation
            message: Message causing invocation
        """
        ...

class Dispatcher:
    """Maps Handlers to OSC addresses and dispatches messages to the handler on matched addresses

    Maps OSC addresses to handler functions and invokes the correct handler when a message comes in.
    """

    def __init__(self) -> None: ...
    def map(
        self,
        address: str,
        handler: FunctionType,
        *args: Union[Any, List[Any]],
        needs_reply_address: bool = ...
    ) -> Handler:
        """Map an address to a handler

        The callback function must have one of the following signatures:

        ``def some_cb(address: str, *osc_args: List[Any]) -> None:``
        ``def some_cb(address: str, fixed_args: List[Any], *osc_args: List[Any]) -> None:``

        ``def some_cb(client_address: Tuple[str, int], address: str, *osc_args: List[Any]) -> None:``
        ``def some_cb(client_address: Tuple[str, int], address: str, fixed_args: List[Any], *osc_args: List[Any]) -> None:``

        Args:
            address: Address to be mapped
            handler: Callback function that will be called as the handler for the given address
            *args: Fixed arguements that will be passed to the callback function
            needs_reply_address: Whether the IP address from which the message originated from shall be passed as
                an argument to the handler callback

        Returns:
            The handler object that will be invoked should the given address match

        """
        ...
    @overload
    def unmap(self, address: str, handler: Handler) -> None:
        """Remove an already mapped handler from an address

        Args:
            address (str): Address to be unmapped
            handler (Handler): A Handler object as returned from map().
        """
        ...
    @overload
    def unmap(
        self,
        address: str,
        handler: FunctionType,
        *args: Union[Any, List[Any]],
        needs_reply_address: bool = ...
    ) -> None:
        """Remove an already mapped handler from an address

        Args:
            address: Address to be unmapped
            handler: A function that will be run when the address matches with
                the OscMessage passed as parameter.
            args: Any additional arguments that will be always passed to the
                handlers after the osc messages arguments if any.
            needs_reply_address: True if the handler function needs the
                originating client address passed (as the first argument).
        """
        ...
    def unmap(self, address, handler, *args, needs_reply_address=...): ...
    def handlers_for_address(
        self, address_pattern: str
    ) -> Generator[None, Handler, None]:
        """Yields handlers matching an address


        Args:
            address_pattern: Address to match

        Returns:
            Generator yielding Handlers matching address_pattern
        """
        ...
    def call_handlers_for_packet(
        self, data: bytes, client_address: Tuple[str, int]
    ) -> None:
        """Invoke handlers for all messages in OSC packet

        The incoming OSC Packet is decoded and the handlers for each included message is found and invoked.

        Args:
            data: Data of packet
            client_address: Address of client this packet originated from
        """
        ...
    def set_default_handler(
        self, handler: FunctionType, needs_reply_address: bool = ...
    ) -> None:
        """Sets the default handler

        The default handler is invoked every time no other handler is mapped to an address.

        Args:
            handler: Callback function to handle unmapped requests
            needs_reply_address: Whether the callback shall be passed the client address
        """
        ...