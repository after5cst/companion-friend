"""
This type stub file was generated by pyright.
"""

from typing import Any, Iterator

_BUNDLE_PREFIX = ...

class ParseError(Exception):
    """Base exception raised when a datagram parsing error occurs."""

    ...

class OscBundle:
    """Bundles elements that should be triggered at the same time.

    An element can be another OscBundle or an OscMessage.
    """

    def __init__(self, dgram: bytes) -> None:
        """Initializes the OscBundle with the given datagram.

        Args:
          dgram: a UDP datagram representing an OscBundle.

        Raises:
          ParseError: if the datagram could not be parsed into an OscBundle.
        """
        ...
    @staticmethod
    def dgram_is_bundle(dgram: bytes) -> bool:
        """Returns whether this datagram starts like an OSC bundle."""
        ...
    @property
    def timestamp(self) -> int:
        """Returns the timestamp associated with this bundle."""
        ...
    @property
    def num_contents(self) -> int:
        """Shortcut for len(*bundle) returning the number of elements."""
        ...
    @property
    def size(self) -> int:
        """Returns the length of the datagram for this bundle."""
        ...
    @property
    def dgram(self) -> bytes:
        """Returns the datagram from which this bundle was built."""
        ...
    def content(self, index) -> Any:
        """Returns the bundle's content 0-indexed."""
        ...
    def __iter__(self) -> Iterator[Any]:
        """Returns an iterator over the bundle's content."""
        ...
