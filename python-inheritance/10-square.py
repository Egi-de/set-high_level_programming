#!/usr/bin/python3
"""Module that defines a Square class inheriting from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square, implemented as a special Rectangle."""

    def __init__(self, size):
        """Initialize a new Square with a validated size."""
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """Return the area of the square."""
        return self._Rectangle__width * self._Rectangle__height
