#!/usr/bin/python3
"""Class that raises ValueError or TypeError"""


class BaseGeometry():
    """Raise Exceptions"""

    def area(self):
        """raise Exception"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
            Checks errors in value
            Args:
                name: Name of value
                value: checked for error
            Raises:
                TypeError: type of value if int
                ValueError: value entered if les than 1
        """
        if type(value) != int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
