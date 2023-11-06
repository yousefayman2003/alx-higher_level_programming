#!/usr/bin/python3
"""Module that contains BaseGeometry Class."""


class BaseGeometry:
    """Base Geometry Class."""

    def area(self):
        """Method that computes area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
             Method that validates value.

             Args:
                name (str): name
                value (int): value
        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
