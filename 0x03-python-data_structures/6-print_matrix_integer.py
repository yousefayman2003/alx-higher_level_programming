#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print()
    else:
        n = len(matrix)
        for i in range(n):
            k = len(matrix[i])
            for j in range(k):
                space = " " if j != k - 1 else "\n"
                print("{:d}".format(matrix[i][j]), end=space)
