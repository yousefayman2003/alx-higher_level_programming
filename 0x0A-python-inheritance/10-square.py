#!/usr/bin/python3
"""Module that contains Square Class."""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Subclass of rectangle (Square)"""
    def __init__(self, size):
        """constructor"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Calculates the area of the square"""
        return self.__size ** 2
