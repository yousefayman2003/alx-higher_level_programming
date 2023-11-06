#!/usr/bin/python3
"""Module that contains inherits_from function."""


def inherits_from(obj, a_class):
    """
        Checks if an instance inherits from a class.

        Args:
            obj (object): the object.
            a_class (Class): the class.

        Returns: True if instance inherits from class, else False.
    """
    return isinstance(obj, a_class) and type(obj) != a_class
