#!/usr/bin/python3
"""
define a class of Square with a private attribute
"""


class Square:
    """
    initializing a private attribute for instance of Square
    """
    def __init__(self, __size=0):
        """
        checking if __size is integer
        checking if __size is less than zero
        """
        self.__size = __size

        if type(self.__size) is not int:
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """
        returns the current square area
        """
        return self.__size*self.__size
