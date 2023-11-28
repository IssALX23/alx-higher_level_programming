#!/usr/bin/python3
""" define a class of Rectangle """


class Rectangle:
    """ initialize class values """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ get or retreive width """
        return self.__width

    @width.setter
    def width(self, value):
        """ set width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ get or retreive height """
        return self.__height

    @height.setter
    def height(self, value):
        """ set height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ returns the rectangle area """
        return self.__width * self.__height

    def perimeter(self):
        """ returns the rectangle perimeter """
        if self.__width == 0 or self.__height == 0:
            return 0

        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """ return a string that represents the object """
        rec_str = ''
        if self.width == 0 or self.height == 0:
            return rec_str

        for i in range(self.height):
            for j in range(self.width):
                rec_str += '#'
            if i < self.height - 1:
                rec_str += '\n'
        return rec_str

    def __repr__(self):
        """ return a string representation of the rectangle """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """ prints a farewell message to the console
        and deduct instance count as well
        when destroying a rectangle """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
