#!/usr/bin/python3
"""creating class square"""


class Square:
    """make size a private instance attribute"""

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

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
                not all(val >= 0 for val in value) or
                not all(isinstance(val, int) for val in value)):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__position[1] == 0:
            for i in range(self.__position[1]):
                print("")

        for i in range(self.__size):
            for p in range(self.__position[0]):
                print(" ", end="")
            for g in range(self.__size):
                print("#", end="")
            print()

        if (self.__size) == 0:
            print("")
