#!/usr/bin/python3
"""class that raises an exception"""


class BaseGeometry:
    """raise an exception"""

    def area(self):
        raise Exception('area() is not implemented')
