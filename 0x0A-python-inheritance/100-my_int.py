#!/usr/bin/python3
"""Module that contains MyInt class."""


class MyInt(int):
    """MyInt class."""
    def __new__(cls, *args, **kwargs):
        """create a new instance of the class"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """!= is now =="""
        return int(self) != other

    def __ne__(self, other):
        """== is now !="""
        return int(self) == other
