#!/usr/bin/python3
"""Class that raises ValueError or TypeError"""


class BaseGeometry():
    """Raise Exceptions"""

    def area(self):
        """raise Exception"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Raise ValueErro and TypeError"""

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
