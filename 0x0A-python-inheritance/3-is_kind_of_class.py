#!/usr/bin/python3
"""Defines for instance if obj is a class or class a_class is inherited"""


def is_kind_of_class(obj, a_class):
    """Check if obj if obj is an instance of class or parent class of a_class

    Args:
        obj: Object to check
        a_class: class to check for instance of
    Returns:
        If obj is an instance of a_class or a class a-class inherited - True
        Otherwise: False
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
