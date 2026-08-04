#!/usr/bin/python3
"""Module that defines a Rectangle class with private dimensions."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle with private, validated width and height."""

    def __init__(self, width, height):
        """Initialize a new Rectangle with validated width and height."""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
