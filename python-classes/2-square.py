#!/usr/bin/python3
"""Module that defines a Square class with a validated size."""


class Square:
    """Represents a square with a validated private size."""

    def __init__(self, size=0):
        """Initialize a Square, validating size is a non-negative int."""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
