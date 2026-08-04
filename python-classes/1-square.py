#!/usr/bin/python3
"""Module that defines a Square class with a private size attribute."""


class Square:
    """Represents a square with an unvalidated private size."""

    def __init__(self, size):
        """Initialize a new Square with the given size."""
        self.__size = size
