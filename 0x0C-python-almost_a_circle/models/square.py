#!/usr/bin/python3
"""module with class square which inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class square initialized"""
    def __init__(self, size, x=0, y=0, id=None):
        """inheriting attributes of Rectangle"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """get width"""
        return self.width

    @size.setter
    def size(self, value):
        """set the width of a square"""
        self.width = value
        self.height = value

    def __str__(self):
        """overriding class"""
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.width))

    def update(self, *args, **kwargs):
        """assigning args"""
        a = 0
        if len(args) != 0:
            for arg in args:
                if a == 0:
                    self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1
        elif len(args) == 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """print rectangle as a dictionary"""
        return {"id": self.id, "x": self.x, "size": self.size, "y": self.y}
