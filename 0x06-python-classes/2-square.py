#!/usr/bin/python3
"""
define a class of Square with a private attribute
"""


class Square:
    """
    initializing a private attribute for instance of Square
    checking if __size is integer
    checking if __size is less than zero
    """
    def __init__(self, __size=0):
        self.__size = __size

        if type(self.__size) is not int:
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")
