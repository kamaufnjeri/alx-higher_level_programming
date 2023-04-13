#!/usr/bin/python3
"""Class Override == operator with !="""


class MyInt(int):
    """Override == operator and !="""

    def __eq__(self, b):
        """Equal to override be not equal to"""
        return super().__ne__(b)

    def __ne__(self, b):
        """Not equal to override by equal to"""
        return super().__eq__(b)
