#!/usr/bin/python3
"""Module that contains to_json_string function."""


import json


def load_from_json_file(filename):
    """
        creates an Object from a JSON file

        Args:
            filename: filename to write at

        Returns: json object
    """
    with open(file=filename, encoding="utf-8", mode="r") as f:
        return json.load(f)
