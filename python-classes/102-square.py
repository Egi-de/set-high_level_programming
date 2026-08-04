#!/usr/bin/python3
"""Module that defines a Square class comparable by area."""


class Square:
    """Represents a square comparable to other squares by area."""

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
        """Set the size, validating it is a non-negative number."""
        if type(value) not in (int, float):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __eq__(self, other):
        """Return True if this square's area equals other's."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Return True if this square's area differs from other's."""
        return self.area() != other.area()

    def __gt__(self, other):
        """Return True if this square's area is greater than other's."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Return True if this square's area is >= other's."""
        return self.area() >= other.area()

    def __lt__(self, other):
        """Return True if this square's area is less than other's."""
        return self.area() < other.area()

    def __le__(self, other):
        """Return True if this square's area is <= other's."""
        return self.area() <= other.area()
