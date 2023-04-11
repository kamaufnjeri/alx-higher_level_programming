#!/usr/bin/python3
"""Defines if obj is subclass of a_class directly or indirectly"""


def inherits_from(obj, a_class):
    """
        Checks sub class of a_class of obj
        Args:
            obj: Check if class of object is subclass of a_class
        Returns:
            IF it is - True
            otherwise - False
        """

    if type(obj) is not a_class and issubclass(type(obj), a_class):
        return True
    else:
        return False
