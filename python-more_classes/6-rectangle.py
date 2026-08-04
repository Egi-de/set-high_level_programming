#!/usr/bin/python3
"""Module that defines a Rectangle tracking its instance count."""


class Rectangle:
    """Represents a rectangle, tracking how many instances exist."""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle and increment the instance count."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Return the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width, validating it is a non-negative integer."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Return the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height, validating it is a non-negative integer."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the rectangle, or 0 if empty."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """Return the rectangle as a string of # characters."""
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = "\n".join(
            ["#" * self.__width for _ in range(self.__height)])
        return rect

    def __repr__(self):
        """Return a string that can recreate this Rectangle via eval()."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print a message and decrement the instance count on deletion."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
