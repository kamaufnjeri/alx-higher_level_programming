#!/usr/bin/python3
""" Class Base created"""
import json
import csv
import turtle
import os


class Base:
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Serialize a python dictionary"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save to file"""
        with open(cls.__name__ + ".json", "w", encoding='utf-8') as f:
            if list_objs is None:
                f.write("[]")
            else:
                k = [obj.to_dictionary() for obj in list_objs]
                f.write(cls.to_json_string(k))

    @staticmethod
    def from_json_string(json_string):
        """desirialize a json string"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """method that returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances"""
        file_name = cls.__name__ + '.json'
        if path.isfile(file_name):
            with open(file_name, 'r', encoding='utf-8') as f:
                dictionary = cls.from_json_string(f.read())
            return[cls.create(**obj) for obj in dictionary]
        return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save to csv files"""
        filename = cls.__name__ + '.csv'
        with open(filename, 'w', encoding='utf-8') as f:
            if cls.__name__ == "Rectangle":
                fieldnames = ['id', 'width', 'height', 'x', 'y']
            else:
                fieldnames = ['id', 'size', 'x', 'y']
            csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
            if list_objs is None or list_objs == []:
                f.write("[]")
            else:
                for obj in list_objs:
                    csv_writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """read from csv file"""
        filename = cls.__name__ + '.csv'
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                csv_reader = csv.DictReader(f, fieldnames=fieldnames)
                k = [dict([key, int(value)] for key, value in line.items())
                     for line in csv_reader]
            return [cls.create(**l) for l in k]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """draw a list of rectangles"""
        t = turtle.Turtle()
        t.screen.bgcolor("black")
        t.screen.title('DRAW RECTANGLES AND SQUARE')
        t.pensize(3)
        t.shape("turtle")
        list1 = ["green", "yellow", "orange"]
        k = 0
        t.color("blue")
        for rectangle in list_rectangles:
            t.showturtle()
            t.up()
            t.goto(rectangle.x, rectangle.y)
            t.down()
            t.begin_fill()
            t.fillcolor(list1[k])
            for i in range(2):
                t.forward(rectangle.width)
                t.left(90)
                t.forward(rectangle.height)
                t.left(90)
            t.end_fill()
            t.hideturtle()
            k += 1
        list2 = ["red", "violet", "indigo"]
        j = 0
        t.color("white")
        for square in list_squares:
            t.showturtle()
            t.up()
            t.goto(square.x, square.y)
            t.down()
            t.begin_fill()
            t.fillcolor(list2[j])
            for i in range(2):
                t.forward(square.width)
                t.left(90)
                t.forward(square.height)
                t.left(90)
            t.end_fill()
            t.hideturtle()
            j += 1

        turtle.exitonclick()"""
