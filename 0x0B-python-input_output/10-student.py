#!/usr/bin/python3
"""Class that defines a student"""


class Student:
    """initialize set first_name, last_name and age"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        dictionary = {}
        if type(attrs) is list:
            for attr in attrs:
                if type(attr) is str and attr in self.__dict__:
                    dictionary[attr] = self.__dict__[attr]
            return dictionary
        return self.__dict__
