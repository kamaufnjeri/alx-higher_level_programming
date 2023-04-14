#!/usr/bin/python3
"""Creates a class square"""


class Square(object):
    """Initialization of attributes"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print("")
            return
        if self.__position[1] != 0:
            for i in range(self.__position[1]):
                print("")
        for i in range(self.__size):
            for j in range(self.__position[0]):
                print(" ", end="")
            for k in range(self.__size):
                print("#", end="")
            print("")

    def __str__(self):
        """Define the print() representation of a Square."""
        string = ""
        if self.__size == 0:
            return ("")
        for i in range(self.__position[1]):
            string += "\n"
        for i in range(self.__size):
            for j in range(self.__position[0]):
                string += " "
            for k in range(self.__size):
                string += "#"
            string += "\n"
        return string[:-1]
