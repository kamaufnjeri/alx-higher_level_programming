#!/usr/bin/python3
"""Class Override == operator with !="""

class MyInt(int):
    """Override == operator and !="""

    def __eq__(self, b):

        return super().__ne__(b)

    def __ne__(self, b):

        return super().__eq__(b)
