#!/usr/bin/python3
"""Module that contains write_file function."""


def write_file(filename="", text=""):
    """
            write content to file.

            Args:
                filename (str): the file name to read.
                text (str): text to write
    """
    with open(file=filename, encoding="utf-8", mode="w") as f:
        return f.write(text)
