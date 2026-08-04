#!/usr/bin/python3
"""Module that adds an attribute to an object, if that object allows it."""


def add_attribute(obj, attr, value):
    """Add a new attribute to obj, or raise TypeError if not possible."""
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
