#!/usr/bin/python3
"""Module that contains to_json_string function."""


import json


def save_to_json_file(my_obj, filename):
    """
        writes an Object to a text file, using a JSON representation

        Args:
            my_obj (any): any object
            filename: filename to write at
    """
    with open(file=filename, encoding="utf-8", mode="w") as f:
        json.dump(my_obj, f)
