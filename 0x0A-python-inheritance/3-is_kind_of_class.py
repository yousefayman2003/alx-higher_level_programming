#!/usr/bin/python3
"""Module that contains is_kind_of_class function."""


def is_kind_of_class(obj, a_class):
    """
        Checks if an object is subclass of a class.

        Args:
            obj (object): the object.
            a_class (Class): the class.

        Returns: True if object is subclass of the class, else False.
    """
    return isinstance(obj, a_class)
