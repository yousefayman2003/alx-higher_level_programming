#!/usr/bin/python3
"""Module that has rectangle class."""


class Rectangle:
    """Rectangle Class."""

    def __init__(self, width=0, height=0):
        """
            Rectangle Initalize.

            Args:
                width (int): width of the rectangle.
                height (int): height of the rectangle.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Getter for private width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """
            Setter for private width attribute

            Raises:
                TypeError: if width is not integer.
                ValueError: if width less than zero.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Getter for private height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """
            Setter for private height attribute

            Raises:
                TypeError: if width is not integer.
                ValueError: if width less than zero.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
