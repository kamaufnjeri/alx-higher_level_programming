#!/usr/bin/python3
"""Prints 
Integer"""
def safe_print_integer_err(value):
    try:
        if isinstance(value, int):
            print(value)
            return True
    except TypeError:
        return False
