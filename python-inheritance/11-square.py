#!/usr/bin/python3
"""Module that defines a Square class with its own __str__."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square, implemented as a special Rectangle."""

    def __init__(self, size):
        """Initialize a new Square with a validated size."""
        super().__init__(size, size)

    def area(self):
        """Return the area of the square."""
        return self._Rectangle__width * self._Rectangle__height

    def __str__(self):
        """Return the string representation: [Square] width/height."""
        return "[Square] {}/{}".format(
            self._Rectangle__width, self._Rectangle__height)
