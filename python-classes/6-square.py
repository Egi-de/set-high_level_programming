#!/usr/bin/python3
"""Module that defines a Square class with a position property."""


class Square:
    """Represents a square with a size and a printable position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a Square with the given size and position."""
        self.size = size
        self.position = position

    def area(self):
        """Return the current area of the square."""
        return self.__size * self.__size

    @property
    def size(self):
        """Return the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size, validating it is a non-negative integer."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Return the current position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position, validating a tuple of 2 positive ints."""
        valid = (type(value) is tuple and len(value) == 2 and
                 all(type(n) is int for n in value) and
                 all(n >= 0 for n in value))
        if not valid:
            raise TypeError(
                "position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Print the square using #, offset by its position."""
        if self.__size == 0:
            print("")
            return
        for _ in range(self.__position[1]):
            print("")
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
