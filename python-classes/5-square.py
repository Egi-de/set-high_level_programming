#!/usr/bin/python3
"""Module that defines a Square class that can print itself."""


class Square:
    """Represents a square that can print its shape with #."""

    def __init__(self, size=0):
        """Initialize a Square with the given size."""
        self.size = size

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

    def my_print(self):
        """Print the square using the # character, or a blank line."""
        if self.__size == 0:
            print("")
            return
        for _ in range(self.__size):
            print("#" * self.__size)
