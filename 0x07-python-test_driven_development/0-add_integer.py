#!/usr/bin/python3
""" define a function that return the addition of two integers """

def add_integer(a, b=98):
    """
    checking if a and b are integers before the addition
    Args:
        a: int
        b: int
    Returns:
        sum of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a+b)
