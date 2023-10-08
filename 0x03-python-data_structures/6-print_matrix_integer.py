#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    n = len(matrix)
    for i in range(n):
        k = len(matrix[i])
        for j in range(k):
            space = " " if j != k - 1 else "\n"
            print(matrix[i][j], end=space)
