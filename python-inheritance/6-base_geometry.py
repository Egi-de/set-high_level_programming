#!/usr/bin/python3
"""Module that defines BaseGeometry with an unimplemented area method."""


class BaseGeometry:
    """Base class for geometry shapes."""

    def area(self):
        """Raise an exception, since area() is not implemented here."""
        raise Exception("area() is not implemented")
