#!/usr/bin/python3
"""Module that contains read_file function."""


def read_file(filename=""):
    """
            reads file content.

            Args:
                filename (str): the file name to read.
    """
    with open(file=filename, encoding="utf-8", mode='r') as f:
        print(f.read())
