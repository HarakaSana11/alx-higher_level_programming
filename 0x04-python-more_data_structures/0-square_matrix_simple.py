#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    blank = []
    for p in matrix:
        blank.append(list(map(lambda p: p**2, p)))
    return (blank)
