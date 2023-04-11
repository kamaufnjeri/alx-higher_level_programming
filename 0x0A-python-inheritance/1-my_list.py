#!/usr/bin/python3
"""Class to create a list"""


class MyList(list):
    """Define a function to print a sorted list"""
    def print_sorted(self):
        """Print sorted list"""
        print(sorted(self))
