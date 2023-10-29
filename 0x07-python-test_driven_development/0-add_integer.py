#!/usr/bin/python3
"""Module that contains a function for adding two numbers"""

def add_integer(a, b=98):
    """
        adds two numbers.

        Args:
            a (int): first number.
            b (int): second number.

        Raises:
            TypeError: if a or b is not int or float.

        Returns:
            the sum of a and b.
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
