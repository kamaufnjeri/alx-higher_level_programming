#!/usr/bin/python3
"""Module to test the class Base"""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Testing the base class"""

    def test_id_if_positive(self):
        """Test id if positive"""
        base_positive = Base(2)
        self.assertEqual(base_positive.id, 2)
        base_positive = Base(120)
        self.assertEqual(base_positive.id, 120)

    def test_id_if_negative(self):
        """test id if negative"""
        base_negative = Base(-91)
        self.assertEqual(base_negative.id, -91)
        base_negative = Base(-4)
        self.assertEqual(base_negative.id, -4)

    def test_id_if_none(self):
        """Test for none id"""
        base_none = Base()
        self.assertEqual(base_none.id, 1)
        base_none = Base(None)
        self.assertEqual(base_none.id, 2)

    def test_id_if_string(self):
        """Test if id is string"""
        base_string = Base('Kamau')
        self.assertEqual(base_string.id, 'Kamau')
        base_string = Base('Love python')
        self.assertEqual(base_string.id, 'Love python')

    def test_to_json_string(self):
        """test to json string"""
        r1 = Rectangle(10, 7, 2, 8, 3)
        dictionary = r1.to_dictionary()
        json_string = Base.to_json_string([dictionary])
        self.assertEqual(type(json_string), str)

    def test_to_json_string_empty_list(self):
        """test t_json_string empty"""
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_wrong_no_of_args(self):
        """takes wrong arguments"""
        with self.assertRaises(TypeError):
            Base.to_json_string()
        with self.assertRaises(TypeError):
            Base.to_json_string({'id': 2}, {'x': 2})

    def test_save_to_file_rect(self):
        """Rectangle attributes saved to file"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r") as file:
            k = file.read()

        self.assertEqual(len(k), 105)

    def test_save_to_file_square(self):
        """Saving to file squares"""
        s1 = Square(10, 7, 2, 8)
        s2 = Square(2, 4)
        Square.save_to_file([s1, s2])

        with open("Square.json", "r") as file:
            k = file.read()

        self.assertEqual(len(k), 77)

    def test_save_to_file_empty(self):
        """Empty list"""
        Rectangle.save_to_file([])

        with open("Rectangle.json", "r") as file:
            k = file.read()
        self.assertEqual(len(k), 2)

    def test_save_to_file_None(self):
        """List object is None"""
        Rectangle.save_to_file(None)

        with open("Rectangle.json", "r") as file:
            k = file.read()
        self.assertEqual(len(k), 2)

    def test_from_json_string(self):
        """from json to python"""
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_output, [{"height": 4, "width": 10, "id": 89},
                          {"height": 7, "width": 1, "id": 7}])
        self.assertEqual(type(list_output), list)

    def test_from_json_string_emptylist(self):
        """empty list"""
        list_input = []
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_output, [])
        self.assertEqual(type(list_output), list)

    def test_from_json_string_None(self):
        """json_string is none"""
        list_output = Rectangle.from_json_string(None)
        self.assertEqual(list_output, [])
        self.assertEqual(type(list_output), list)

class Test_Base_create(unittest.TestCase):
    """Unittests for testing create method of Base class."""

    def test_create_rectangle(self):
        """test create method using rectangle"""
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(r1))
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(r2))
        self.assertIsNot(r1, r2)
        self.assertNotEqual(r1, r2)

    def test_create_square(self):
        """using square"""
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(s1))
        self.assertEqual("[Square] (7) 5/1 - 3", str(s2))
        self.assertIsNot(s1, s2)
        self.assertNotEqual(s1, s2)

    def test_load_from_file_rectangle(self):
        """testing load from file method rectangle"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(list_rectangles_output[0]), str(r1))
        self.assertEqual(str(list_rectangles_output[1]), str(r2))
        self.assertEqual(type(list_rectangles_output[0]), Rectangle)
        self.assertEqual(type(list_rectangles_output[1]), Rectangle)

    def test_load_from_file_square(self):
        """testing load from file method rectangle"""
        s1 = Square(5, 1, 3, 4)
        s2 = Square(2, 4)
        list_squares_input = [s1, s2]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(list_squares_output[0]), str(s1))
        self.assertEqual(str(list_squares_output[1]), str(s2))
        self.assertEqual(type(list_squares_output[0]), Square)
        self.assertEqual(type(list_squares_output[1]), Square)

    def test_load_from_file_empty(self):
        """Empty list"""
        Square.save_to_file(None)
        empty = Square.load_from_file()
        self.assertEqual([], empty)

    def test_load_from_file_argserror_nos(self):
        """if more args used"""
        with self.assertRaises(TypeError):
            Square.load_from_file([], 1)

class TestBase_save_to_file_csv(unittest.TestCase):
    """saving to csv file"""

    def test_save_to_file_csv_rectangle(self):
        """Test for rectangle"""
        r1 = Rectangle(4, 2, 4, 5, 6)
        r2 = Rectangle(3, 3, 1, 3, 4)
        Rectangle.save_to_file_csv([r1, r2])
        with open("Rectangle.csv", "r") as file:
            self.assertTrue("6,4,2,4,5\n4,3,3,1,4", file.read())

    def test_save_to_file_csv_square(self):
        """Test for square"""
        s1 = Square(10, 5, 6, 8)
        s2 = Square(12, 8, 3, 2)
        Square.save_to_file_csv([s1, s2])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,5,6\n2,12,8,3,2", f.read())

    def test_save_to_file_csv_overwrite(self):
        """Overwrite test"""
        s = Square(9, 2, 39, 2)
        Square.save_to_file_csv([s])
        s = Square(10, 7, 2, 8)
        Square.save_to_file_csv([s])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2,8", f.read())

    def test_save_to_file__csv_Empty_or_None(self):
        Square.save_to_file_csv([])
        with open("Square.csv", "r") as f:
            k = f.read()
        self.assertEqual("[]", k)
        Square.save_to_file_csv(None)
        with open("Square.csv", "r") as f:
            k = f.read()
        self.assertEqual("[]", k)

    def test_save_to_file_csv_errorss(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv()
        with self.assertRaises(TypeError):
            Square.save_to_file_csv([], 1)

class TestBase_load_from_file_csv(unittest.TestCase):
    """test loading from csv file tested"""
    def test_load_from_file_csv_rectangle(self):
        """using rectangle"""
        r1 = Rectangle(4, 5, 3, 7, 8)
        r2 = Rectangle(2, 3, 4, 5)
        Rectangle.save_to_file_csv([r1, r2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))
        self.assertEqual(str(r2), str(list_rectangles_output[1]))
        self.assertEqual(type(list_rectangles_output[0]), Rectangle)
        self.assertEqual(type(list_rectangles_output[1]), Rectangle)

    def test_load_from_file_csv_first_square(self):
        """square is used"""
        s1 = Square(6, 1, 3, 2)
        s2 = Square(4, 1, 2)
        Square.save_to_file_csv([s1, s2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(s1), str(list_squares_output[0]))
        self.assertEqual(str(s2), str(list_squares_output[1]))
        self.assertEqual(type(list_squares_output[0]), Square)
        self.assertEqual(type(list_squares_output[1]), Square)

    def test_load_from_file_csv_more_than_one_arg(self):
        """errors"""
        with self.assertRaises(TypeError):
            Base.load_from_file_csv([], 1)

if __name__ == "__main__":
    unittest.main()
