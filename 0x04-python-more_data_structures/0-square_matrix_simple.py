#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_max = []
    for line in matrix:
        new_max.append(list(map(lambda a: a*a, line)))
    return new_max
