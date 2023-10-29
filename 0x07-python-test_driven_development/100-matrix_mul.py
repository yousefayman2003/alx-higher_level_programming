#!/usr/bin/python3
"""Module that contains matrix_mul function."""


def matrix_mul(m_a, m_b):
    """
         multiplies 2 matrices:

         Args:
            m_a (list): 2D List containing the numbers
            m_b (list): 2D list containing the numbers

        Raises:
            TypeError: if m_a or m_b is not a list
            TypeError: if m_a or m_b is not a list of list
            TypeError: if one element of those list of lists is not an integer or a float
            TypeError: if m_a or m_b  rows are not of the same size
            ValueError: if m_a or m_b is empty
            ValueError: if m_a and m_b can't be multiplied

        Returns:
            Result of matrix multiplication.
    """

    # checking for all errors that could occur
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    
    m_a_rect ,m_b_rect, m_a_num, m_b_num = False, False, False, False
    for row in m_a:
        if type(row) is not list:
            raise TypeError("m_a must be a list of lists")

        if len(row) != len(m_a[0]):
            m_a_rect = True
        
        for number in row:
            if type(number) not in (int, float):
                m_a_num = True

    for row in m_b:
        if type(row) is not list:
            raise TypeError("m_b must be a list of lists")

        if len(row) != len(m_b[0]):
            m_b_rect = True

        for number in row:
            if type(number) not in (int, float):
                m_b_num = True

    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")

    if len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")

    if m_a_num:
        raise TypeError("m_a should contain only integers or floats")

    if m_b_num:
        raise TypeError("m_b should contain only integers or floats")

    if m_a_rect:
        raise TypeError("each row of m_a must should be of the same size")

    if m_b_rect:
        raise TypeError("each row of m_b must should be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[] for _ in range(len(m_a))]

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            num = 0
            for k in range(len(m_b)):
                num += m_a[i][k] * m_b[k][j]
            result[i].append(num)

    return result


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/100-matrix_mul.txt")
