#!/usr/bin/python3
"""Module that contains print square function."""


def print_square(size):
    """
        prints a square with the character #.

        Args:
            size (int): size of the square.

        Raises:
            TypeError: if size is not a integer.
            ValueError: if size is less than 0.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    print((size * '#' + '\n') * size, end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
