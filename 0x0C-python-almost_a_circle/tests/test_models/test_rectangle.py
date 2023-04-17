#!/usr3/bin/python3
"""module to test Rectangle class"""
import unittest
import io
import sys
from models.rectangle import Rectangle
from models.base import Base
from models.square import Square


class Test_check_Rectangle(unittest.TestCase):
    """class to check class rectangle"""
    def test_inherits_from(self):
        """class it inherits from"""
        self.assertTrue(issubclass(Rectangle, Base))

    def test_type_object_created(self):
        """type of object"""
        r1 = Rectangle(4, 2, 4, 5, 2)
        self.assertTrue(type(r1), Rectangle)
        self.assertEqual(r1.width, 4)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 5)
        self.assertEqual(r1.id, 2)

    def test_arguments(self):
        """test with arguments numbers"""
        r1 = Rectangle(4, 2)
        r2 = Rectangle(2, 1, 3)
        r3 = Rectangle(4, 1, 4, 5)
        self.assertEqual(r1.width, 4)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, r2.id - 1)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 1)
        self.assertEqual(r2.x, 3)
        self.assertEqual(r2.y, 0)
        self.assertEqual(r2.id, r3.id - 1)
        self.assertEqual(r3.width, 4)
        self.assertEqual(r3.height, 1)
        self.assertEqual(r3.x, 4)
        self.assertEqual(r3.y, 5)
        self.assertEqual(r1.id, r3.id - 2)

    def test_width_getter_setter(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(1, r.width)
        r.width = 10
        self.assertEqual(10, r.width)

    def test_height_getter_setter(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(2, r.height)
        r.height = 10
        self.assertEqual(10, r.height)

    def test_x_getter_setter(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(3, r.x)
        r.x = 10
        self.assertEqual(10, r.x)

    def test_y_getter_setter(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(4, r.y)
        r.y = 10
        self.assertEqual(10, r.y)

    def test_private_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(6, 7, 2, 3, 5).__width)
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__height)
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__x)
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__y)


    def test_wrong_numbers_arg(self):
        """Wrong numbers of elements entered"""
        with self.assertRaises(TypeError):
            Rectangle()
        with self.assertRaises(TypeError):
            Rectangle(1)
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_value_valueerror(self):
        """check value errors"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-2, 1)
            Rectangle(0, 1)

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, -1)
            Rectangle(2, 0)

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(2, 1, -1, 4)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(2, 1, 5, -4)

    def test_width_None(self):
        """typeerrors"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 1)

    def test_width_string(self):
        """string error"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle('Python', 1)

    def test_width_float(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(1.1, 2, 3, 4, 5)

    def test_width_boolean(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(True, 4, 9, 5, 8)

    def test_width_tuple(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((1, 2), 3, 2, 1, 4)

    def test_width_list(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([1, 2], 3, 2, 4, 2)

    def test_width_set(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({1, 2}, 3, 2, 1, 5)
    def test_width_dict(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({'flo': 1}, 1, 2, 3, 4)

    def test_width_inf(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('inf'), 2, 3, 4, 5)

    def test_width_nan(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('nan'), 2, 3, 4, 5)

    def test_width_func(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(print(), 2, 3, 4, 5)

    def test_height_string(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, '1')

    def test_height_None(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, None)

    def test_height_float(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, 1.1, 3, 4, 5)

    def test_height_boolean(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, True, 9, 5, 8)

    def test_height_tuple(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, (1, 2), 2, 1, 4)

    def test_height_list(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, [1, 2], 3, 4, 2)

    def test_height_set(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, {1, 2}, 2, 1, 5)

    def test_height_dict(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, {'flo': 1}, 2, 3, 4)
    def test_height_inf(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, float('inf'), 3, 4, 5)

    def test_height_nan(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, float('nan'), 3, 4, 5)

    def test_height_func(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, print(), 3, 4, 5)

    def test_x_string(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 3, '1')

    def test_x_None(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 2, None)

    def test_x_float(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 3, 1.1, 4, 5)

    def test_x_boolean(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 2, True, 5, 8)

    def test_x_tuple(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 3, (1, 2), 1, 4)

    def test_x_list(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, [1, 2], 3, 2)

    def test_x_set(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 3, {1, 2}, 1, 5)

    def test_x_dict(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 3, {'flo': 1}, 3, 4)
    def test_x_inf(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 4, float('inf'), 4, 5)

    def test_x_nan(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 4, float('nan'), 4, 5)

    def test_x_func(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 2, print(), 4, 5)

    def test_y_string(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 3, 4, '1')

    def test_y_None(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 4, 2, None)

    def test_y_float(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 3, 4, 4.4, 5)

    def test_y_boolean(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 4, 5, True, 8)

    def test_y_tuple(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 3, 4, (1, 2), 4)

    def test_y_list(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 4, 5, [1, 2], 2)

    def test_y_set(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 4, {1, 2}, 5)

    def test_y_dict(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 3, 4, {'flo': 1}, 4)
    def test_y_inf(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 4, 2, float('inf'), 5)

    def test_y_nan(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 4, 2, float('nan'), 5)

    def test_y_func(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 4, 6, print(), 5)

class test_Rectangle_area(unittest.TestCase):
    """Test method area"""
    def test_area(self):
        r = Rectangle(4, 2, 3, 4, 5)
        self.assertEqual(8, r.area())

    def test_area_after_setting_width_height(self):
        r = Rectangle(3, 4, 5, 6, 7)
        self.assertEqual(12, r.area())
        r.width = 6
        r.height = 7
        self.assertEqual(42, r.area())

    def test_area_with_args(self):
        r = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            r.area(1)


class Test_Rectangle_stdout(unittest.TestCase):
    """Unittests for testing __str__ and display methods of Rectangle class."""

    @staticmethod
    def capture_stdout(rect, method):
        """captures and returns method"""
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(rect)
        else:
            rect.display()
        sys.stdout = sys.__stdout__
        return capture

    def test_str_without_id(self):
        r = Rectangle(21, 2, 4, 7)
        capture = Test_Rectangle_stdout.capture_stdout(r, "print")
        correct = "[Rectangle] ({}) 4/7 - 21/2\n".format(r.id)
        self.assertEqual(correct, capture.getvalue())

    def test_with_id_given(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual("[Rectangle] (5) 3/4 - 1/2", str(r))
        r.width = 5
        r.height = 4
        r.x = 3
        r.y = 2
        self.assertEqual("[Rectangle] (5) 3/2 - 5/4", str(r))

    def test_str_method_one_arg(self):
        r = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            r.__str__(1)

    def test_display(self):
        r = Rectangle(2, 4)
        capture = Test_Rectangle_stdout.capture_stdout(r, "display")
        self.assertEqual("##\n##\n##\n##\n", capture.getvalue())
        r = Rectangle(2, 4, 2, 0, 1)
        capture = Test_Rectangle_stdout.capture_stdout(r, "display")
        self.assertEqual("  ##\n  ##\n  ##\n  ##\n", capture.getvalue())
        r = Rectangle(2, 4, 0, 2, 1)
        capture = Test_Rectangle_stdout.capture_stdout(r, "display")
        display = "\n\n##\n##\n##\n##\n"
        self.assertEqual(display, capture.getvalue())
        r = Rectangle(2, 4, 2, 2, 1)
        capture = Test_Rectangle_stdout.capture_stdout(r, "display")
        display = "\n\n  ##\n  ##\n  ##\n  ##\n"
        self.assertEqual(display, capture.getvalue())

    def test_display_error(self):
        r = Rectangle(5, 1, 2, 4, 7)
        with self.assertRaises(TypeError):
            r.display(1)


class Test_Rectangle_update_args(unittest.TestCase):
    """testing the update method with arguments"""

    def test_update_no_args(self):
        r = Rectangle(1, 2, 3, 4, 5)
        r.update()
        self.assertEqual("[Rectangle] (5) 3/4 - 1/2", str(r))
        r.update(76)
        self.assertEqual("[Rectangle] (76) 3/4 - 1/2", str(r))
        r.update(76, 77)
        self.assertEqual("[Rectangle] (76) 3/4 - 77/2", str(r))
        r.update(76, 77, 78)
        self.assertEqual("[Rectangle] (76) 3/4 - 77/78", str(r))
        r.update(76, 77, 78, 79)
        self.assertEqual("[Rectangle] (76) 79/4 - 77/78", str(r))
        r.update(76, 77, 78, 79, 80)
        self.assertEqual("[Rectangle] (76) 79/80 - 77/78", str(r))
        r.update(76, 77, 78, 79, 80, 81)
        self.assertEqual("[Rectangle] (76) 79/80 - 77/78", str(r))

    def test_update_args_None_id(self):
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(None)
        correct = "[Rectangle] ({}) 3/4 - 1/2".format(r.id)
        self.assertEqual(correct, str(r))
        r.update(None, 77, 78, 79, 80)
        correct = "[Rectangle] ({}) 79/80 - 77/78".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_args_wrong_width(self):
        r = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, 'python')
        r = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(89, 0)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(89, -5)

    def test_update_wrong_height(self):
        r = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(89, 2, "python")
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(89, 1, 0)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(89, 1, -5)

    def test_update_wrong_x(self):
        r = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(89, 2, 3, "python")
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(89, 1, 2, -6)

    def test_update_wrong_y(self):
        r = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(89, 2, 3, 4, "python")
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(89, 1, 2, 3, -6)

class TestRectangle_update_kwargs(unittest.TestCase):
    """Update with kew words arguments"""

    def test_update(self):
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(id=1)
        self.assertEqual("[Rectangle] (1) 3/4 - 1/2", str(r))
        r.update(width=77, id=1)
        self.assertEqual("[Rectangle] (1) 3/4 - 77/2", str(r))
        r.update(width=77, height=78, id=76)
        self.assertEqual("[Rectangle] (76) 3/4 - 77/78", str(r))
        r.update(id=76, x=79, height=78, width=77)
        self.assertEqual("[Rectangle] (76) 79/4 - 77/78", str(r))
        r.update(y=80, x=79, id=76, width=77, height=78)
        self.assertEqual("[Rectangle] (76) 79/80 - 77/78", str(r))

    def test_update_kwargs_id_none(self):
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(id=None)
        correct = "[Rectangle] ({}) 3/4 - 1/2".format(r.id)
        self.assertEqual(correct, str(r))
        r.update(id=None, height=78, y=80)
        correct = "[Rectangle] ({}) 3/80 - 1/78".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_kwargs_wrong_width(self):
        r = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(width="python")
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(width=0)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(width=-6)

    def test_update_kwargs_wrong_height(self):
        r = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(height="python")
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(height=0)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(height=-5)

    def test_update_kwargs_wrong_x(self):
        r = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(x="python")
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(x=-5)

    def test_update_kwargs_wrong_y(self):
        r = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(y="python")
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(y=-5)

    def test_update_mixed_args_kwargs(self):
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(76, 2, height=4, y=6)
        self.assertEqual("[Rectangle] (76) 3/4 - 2/2", str(r))

    def test_update_kwargs_wrong_keys(self):
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(z=5, k=10)
        self.assertEqual("[Rectangle] (5) 3/4 - 1/2", str(r))


class Test_Rectangle_to_dictionary(unittest.TestCase):
    """Test to_dictionary"""

    def test_to_dictionary(self):
        r = Rectangle(1, 2, 3, 4, 5)
        correct = {'x': 3, 'y': 4, 'id': 5, 'height': 2, 'width': 1}
        self.assertDictEqual(correct, r.to_dictionary())

    def test_to_dictionary_use_update(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(6, 7, 8, 9, 20)
        r2.update(**r1.to_dictionary())
        self.assertNotEqual(r1, r2)

    def test_to_dictionary_arg(self):
        r = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            r.to_dictionary(1)


if __name__ == "__main__":
    unittest.main()
