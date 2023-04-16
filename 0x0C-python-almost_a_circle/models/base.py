#!/usr/bin/python3
"""
A module of class Base a base of all
other classes and manages the id attribute
"""
import json
import csv


class Base:
    """Base class"""

    __nd_objects = 0

    def __init__(self, id=None):
        """initialization"""

        if id is not None:
            self.id = id
        else:
            Base.__nd_objects += 1
            self.id = Base.__nd_objects

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
        """Deserialize strings stored in a json file"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r', encoding="utf-8") as f:
                k = Base.from_json_string(f.read())
            return [cls.create(**l) for l in k]
        except FileNotFoundError:
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
            if list_objs is None:
                csv_writer.write("[]")
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
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares)
    """draw a list of rectangles"""
