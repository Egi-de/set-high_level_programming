#!/usr/bin/python3
"""Module that defines MyInt, a rebellious integer class."""


class MyInt(int):
    """An int subclass with the == and != operators inverted."""

    def __eq__(self, other):
        """Return True if self is NOT numerically equal to other."""
        return int(self) != int(other)

    def __ne__(self, other):
        """Return True if self IS numerically equal to other."""
        return int(self) == int(other)
