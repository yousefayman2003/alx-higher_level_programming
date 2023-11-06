#!/usr/bin/python3
"""Module that contains is_same_class function."""


def is_same_class(obj, a_class):
    """
        Checks if an object is the same type of a class.

        Args:
            obj (object): the object.
            a_class (Class): the class.

        Returns: True if object is the same type of the class, else False.
    """
    return type(obj) == a_class
