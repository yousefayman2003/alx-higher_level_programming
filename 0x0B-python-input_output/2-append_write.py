#!/usr/bin/python3
"""Module that contains append_write function."""


def append_write(filename="", text=""):
    """
            appends content to file.

            Args:
                filename (str): the file name to read.
                text (str): text to write
    """
    with open(file=filename, encoding="utf-8", mode="a") as f:
        f.write(text)
