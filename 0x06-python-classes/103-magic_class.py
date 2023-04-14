#!/usr/bin/python3
"Magic class converting python bytecode to class"""
import math


class MagicClass:
    """Class fo assemble bytecode"""

    def __init__(self, radius=0):
        self.__radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be an integer')
        self.__radius = radius

    def area(self):
        return self.__radius ** 2 * math.pi

    def circumference(self):
        return 2 * math.pi * self.__radius
