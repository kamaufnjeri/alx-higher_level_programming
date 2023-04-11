#!/usr/bin/python3

"""Class that inherits from  list and sorts a list"""


class MyList(list):
    """def function defining a list to pe printed sorted"""

    def print_sorted(self):
        """A list to be printed in sorted order"""
        print(sorted(self))
