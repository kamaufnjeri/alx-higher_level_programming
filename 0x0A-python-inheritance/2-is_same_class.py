#!/usr/bin/python3
"""Defines if obj is exactly the specified class a_class"""


def is_same_class(obj, a_class):
    """Check if obj is class a_class

    Args:
        obj: object to check
        a_class: class to find if obj belongs t0
    Returs:
        If obj is of type a_class - True
        Otherwise - False
        """
    if type(obj) == a_class:
        return True
    else:
        return False
