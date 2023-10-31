#!/usr/bin/python3
"""
define a function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    a function that divides all elements of a matrix

    Args:
        matrix: a list of integers or floats
        div: a number

    Returns:
        a new matrix
    """
    # Checking if matrix is a list of lists
    if not isinstance(matrix, list) or not all(
            isinstance(row, list) for row in matrix):
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

    row_size = len(matrix[0])
    for row in matrix:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")

    # Checking if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Checking for division by zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = []
        for item in row:
            new_row.append(round(item/div, 2))
        new_matrix.append(new_row)

    return new_matrix


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
