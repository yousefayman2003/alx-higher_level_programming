#!/usr/bin/python3
"""Module that contains Rectangle Class."""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """A subclass of base geometry."""

    def __init__(self, width, height):
        """Constuctor."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
            Calculates the area of the rectangle

            Return: the area
        """
        return self.__width * self.__height

    def __str__(self):
        """String representation for rectangle"""
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
