"""
This type stub file was generated by pyright.
"""

from pythonosc import osc_bundle

"""Build OSC bundles for client applications."""
IMMEDIATELY = ...

class BuildError(Exception):
    """Error raised when an error occurs building the bundle."""

    ...

class OscBundleBuilder:
    """Builds arbitrary OscBundle instances."""

    def __init__(self, timestamp: int) -> None:
        """Build a new bundle with the associated timestamp.

        Args:
          - timestamp: system time represented as a floating point number of
                       seconds since the epoch in UTC or IMMEDIATELY.
        """
        ...
    def add_content(self, content: osc_bundle.OscBundle) -> None:
        """Add a new content to this bundle.

        Args:
          - content: Either an OscBundle or an OscMessage
        """
        ...
    def build(self) -> osc_bundle.OscBundle:
        """Build an OscBundle with the current state of this builder.

        Raises:
          - BuildError: if we could not build the bundle.
        """
        ...