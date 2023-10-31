#!/usr/bin/python3
""" define a function that adds 2 integers """


def add_integer(a, b=98):
    """
    checking if a and b are numbers
    Args:
        a: integer
        b: integer
    Returns:
        sum of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)

    return a + b
