from dataclasses import dataclass

@dataclass
class StreamDeckButton:
    alias: str   # Our name, not known to Companion.
    page: int
    bank: int
    bgcolor: int
    color: int
    text: str
    size: int


