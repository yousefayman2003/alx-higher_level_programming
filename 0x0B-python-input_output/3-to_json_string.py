#!/usr/bin/python3
"""Module that contains to_json_string function."""


import json


def to_json_string(my_obj):
    """
            returns the JSON representation of an object (string).

            Args:
                my_obj (any): any object

            Returns: returns the JSON representation of an object (string)
    """
    return json.dumps(my_obj)
