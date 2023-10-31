#!/usr/bin/python3
"""
define functioni that prints a square with the character #
"""


def print_square(size):
    """
    prints a square with the character #

    Args:
        size: integer

    Returns:
        print square shape with #
    """
    if (not isinstance(size, (int, float)) or
            (isinstance(size, float) and size < 0)):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end='')
        print()
