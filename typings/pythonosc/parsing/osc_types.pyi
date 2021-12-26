"""
This type stub file was generated by pyright.
"""

from datetime import datetime
from typing import Tuple, Union

"""Functions to get OSC types from datagrams and vice versa"""

class ParseError(Exception):
    """Base exception for when a datagram parsing error occurs."""

    ...

class BuildError(Exception):
    """Base exception for when a datagram building error occurs."""

    ...

IMMEDIATELY = ...
_INT_DGRAM_LEN = ...
_INT64_DGRAM_LEN = ...
_UINT64_DGRAM_LEN = ...
_FLOAT_DGRAM_LEN = ...
_DOUBLE_DGRAM_LEN = ...
_TIMETAG_DGRAM_LEN = ...
_STRING_DGRAM_PAD = ...
_BLOB_DGRAM_PAD = ...
_EMPTY_STR_DGRAM = ...

def write_string(val: str) -> bytes:
    """Returns the OSC string equivalent of the given python string.

    Raises:
      - BuildError if the string could not be encoded.
    """
    ...

def get_string(dgram: bytes, start_index: int) -> Tuple[str, int]:
    """Get a python string from the datagram, starting at pos start_index.

    According to the specifications, a string is:
    "A sequence of non-null ASCII characters followed by a null,
    followed by 0-3 additional null characters to make the total number
    of bits a multiple of 32".

    Args:
      dgram: A datagram packet.
      start_index: An index where the string starts in the datagram.

    Returns:
      A tuple containing the string and the new end index.

    Raises:
      ParseError if the datagram could not be parsed.
    """
    ...

def write_int(val: int) -> bytes:
    """Returns the datagram for the given integer parameter value

    Raises:
      - BuildError if the int could not be converted.
    """
    ...

def get_int(dgram: bytes, start_index: int) -> Tuple[int, int]:
    """Get a 32-bit big-endian two's complement integer from the datagram.

    Args:
      dgram: A datagram packet.
      start_index: An index where the integer starts in the datagram.

    Returns:
      A tuple containing the integer and the new end index.

    Raises:
      ParseError if the datagram could not be parsed.
    """
    ...

def write_int64(val: int) -> bytes:
    """Returns the datagram for the given 64-bit big-endian signed parameter value

    Raises:
      - BuildError if the int64 could not be converted.
    """
    ...

def get_int64(dgram: bytes, start_index: int) -> Tuple[int, int]:
    """Get a 64-bit big-endian signed integer from the datagram.

    Args:
      dgram: A datagram packet.
      start_index: An index where the 64-bit integer starts in the datagram.

    Returns:
      A tuple containing the 64-bit integer and the new end index.

    Raises:
      ParseError if the datagram could not be parsed.
    """
    ...

def get_uint64(dgram: bytes, start_index: int) -> Tuple[int, int]:
    """Get a 64-bit big-endian unsigned integer from the datagram.

    Args:
      dgram: A datagram packet.
      start_index: An index where the integer starts in the datagram.

    Returns:
      A tuple containing the integer and the new end index.

    Raises:
      ParseError if the datagram could not be parsed.
    """
    ...

def get_timetag(dgram: bytes, start_index: int) -> Tuple[datetime, int]:
    """Get a 64-bit OSC time tag from the datagram.

    Args:
      dgram: A datagram packet.
      start_index: An index where the osc time tag starts in the datagram.

    Returns:
      A tuple containing the tuple of time of sending in utc as datetime and the
      fraction of the current second and the new end index.

    Raises:
      ParseError if the datagram could not be parsed.
    """
    ...

def write_float(val: float) -> bytes:
    """Returns the datagram for the given float parameter value

    Raises:
      - BuildError if the float could not be converted.
    """
    ...

def get_float(dgram: bytes, start_index: int) -> Tuple[float, int]:
    """Get a 32-bit big-endian IEEE 754 floating point number from the datagram.

    Args:
      dgram: A datagram packet.
      start_index: An index where the float starts in the datagram.

    Returns:
      A tuple containing the float and the new end index.

    Raises:
      ParseError if the datagram could not be parsed.
    """
    ...

def write_double(val: float) -> bytes:
    """Returns the datagram for the given double parameter value

    Raises:
      - BuildError if the double could not be converted.
    """
    ...

def get_double(dgram: bytes, start_index: int) -> Tuple[float, int]:
    """Get a 64-bit big-endian IEEE 754 floating point number from the datagram.

    Args:
      dgram: A datagram packet.
      start_index: An index where the double starts in the datagram.

    Returns:
      A tuple containing the double and the new end index.

    Raises:
      ParseError if the datagram could not be parsed.
    """
    ...

def get_blob(dgram: bytes, start_index: int) -> Tuple[bytes, int]:
    """Get a blob from the datagram.

    According to the specifications, a blob is made of
    "an int32 size count, followed by that many 8-bit bytes of arbitrary
    binary data, followed by 0-3 additional zero bytes to make the total
    number of bits a multiple of 32".

    Args:
      dgram: A datagram packet.
      start_index: An index where the float starts in the datagram.

    Returns:
      A tuple containing the blob and the new end index.

    Raises:
      ParseError if the datagram could not be parsed.
    """
    ...

def write_blob(val: bytes) -> bytes:
    """Returns the datagram for the given blob parameter value.

    Raises:
      - BuildError if the value was empty or if its size didn't fit an OSC int.
    """
    ...

def get_date(dgram: bytes, start_index: int) -> Tuple[float, int]:
    """Get a 64-bit big-endian fixed-point time tag as a date from the datagram.

    According to the specifications, a date is represented as is:
    "the first 32 bits specify the number of seconds since midnight on
    January 1, 1900, and the last 32 bits specify fractional parts of a second
    to a precision of about 200 picoseconds".

    Args:
      dgram: A datagram packet.
      start_index: An index where the date starts in the datagram.

    Returns:
      A tuple containing the system date and the new end index.
      returns osc_immediately (0) if the corresponding OSC sequence was found.

    Raises:
      ParseError if the datagram could not be parsed.
    """
    ...

def write_date(system_time: Union[int, float]) -> bytes: ...
def write_rgba(val: bytes) -> bytes:
    """Returns the datagram for the given rgba32 parameter value

    Raises:
      - BuildError if the int could not be converted.
    """
    ...

def get_rgba(dgram: bytes, start_index: int) -> Tuple[bytes, int]:
    """Get an rgba32 integer from the datagram.

    Args:
      dgram: A datagram packet.
      start_index: An index where the integer starts in the datagram.

    Returns:
      A tuple containing the integer and the new end index.

    Raises:
      ParseError if the datagram could not be parsed.
    """
    ...

def write_midi(val: Tuple[Tuple[int, int, int, int], int]) -> bytes:
    """Returns the datagram for the given MIDI message parameter value

       A valid MIDI message: (port id, status byte, data1, data2).

    Raises:
      - BuildError if the MIDI message could not be converted.

    """
    ...

def get_midi(dgram: bytes, start_index: int) -> Tuple[Tuple[int, int, int, int], int]:
    """Get a MIDI message (port id, status byte, data1, data2) from the datagram.

    Args:
      dgram: A datagram packet.
      start_index: An index where the MIDI message starts in the datagram.

    Returns:
      A tuple containing the MIDI message and the new end index.

    Raises:
      ParseError if the datagram could not be parsed.
    """
    ...