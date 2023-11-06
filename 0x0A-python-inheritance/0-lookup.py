#!/usr/bin/python3
"""Module that contains lookup function."""


def lookup(object):
    """
        Looks up attributes and methods of an object.

        Args:
            object (object): the given object.

        Returns:
            list: the list of attributes and methods.
    """
    return dir(object)
