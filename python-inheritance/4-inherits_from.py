#!/usr/bin/python3
"""Module for checking strict (non-exact) inheritance."""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of a class inherited from a_class."""
    return isinstance(obj, a_class) and type(obj) is not a_class
