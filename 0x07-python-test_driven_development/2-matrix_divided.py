#!/usr/bin/python3
"""Module that contains a function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """
        divides all elements of a matrix.

        Args:
            matrix (list): 2D list of integers or floats.
            div (int or float): the number to divide with.

        Raises:
            TypeError: if matrix contains a type other than `int`, `float` or
                if all rows are not of the same size or,
                div is a type other than `int`, `float`.
            ZeroDivisionError: if div equals `0`
    """
    # check if matrix is a list and contains elements
    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")

    # check if div is an int or float
    if type(div) not in (int, float):
        raise TypeError("div must be a number")

    # check if div is not 0
    if div == 0:
        raise ZeroDivisionError("division by zero")
    row_length = len(matrix[0])

    for row in matrix:
        # check if row is a list and contains elements
        if type(row) is not list or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")

        # check if all rows are of the same length
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

        # check if an element is not an int or a float
        for el in row:
            if type(el) not in (int, float):
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")

    return [[round(el / div, 2) for el in r] for r in matrix]


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
