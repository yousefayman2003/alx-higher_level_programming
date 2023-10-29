#!/usr/bin/python3
"""Module that uses numpy to muliply two matrices"""

import numpy


def lazy_matrix_mul(m_a, m_b):
    """
         multiplies 2 matrices by using the module NumPy

         Args:
            m_a (list): 2D list containing the numbers
            m_b (list): 2D list containing the numbers

        Returns: the result of mulplication
    """
    return numpy.matmul(m_a, m_b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/101-lazy_matrix_mul.txt")
