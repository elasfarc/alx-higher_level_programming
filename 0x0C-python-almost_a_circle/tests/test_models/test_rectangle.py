from os import execv
import unittest
from unittest.mock import patch
from io import StringIO

from models.base import Base
from models.rectangle import Rectangle

import sys


class Test_Rectangle(unittest.TestCase):
    def setUp(self) -> None:
        Base._Base__nb_objects = 0

    def test_rectangle_base(self):
        self.assertTrue(Base in Rectangle.__bases__)

    def test_valid_parameters(self):
        rec = Rectangle(width=5, height=10, x=2, y=4, id=15)
        assert rec.id == 15
        assert rec.width == 5
        assert rec.height == 10
        assert rec.x == 2
        assert rec.y == 4

    def test_setters_getters(self):
        rec = Rectangle(width=5, height=10, x=2, y=4, id=15)
        rec.width = 12
        rec.height = 8
        rec.x = 4
        rec.y = 2
        rec.id = 20
        assert rec.id == 20
        assert rec.width == 12
        assert rec.height == 8
        assert rec.x == 4
        assert rec.y == 2

    def test_non_integers_attrubites(self):
        with self.assertRaises(TypeError) as e:
            rec = Rectangle(width=[], height=10, x=2, y=4)
        self.assertEqual(str(e.exception), "width must be an integer")

        with self.assertRaises(TypeError) as e:
            rec = Rectangle(width=5, height="l")
        self.assertEqual(str(e.exception), "height must be an integer")

        with self.assertRaises(TypeError) as e:
            rec = Rectangle(width=4, height=10, x=(2, 4))
        self.assertEqual(str(e.exception), "x must be an integer")

        with self.assertRaises(TypeError) as e:
            rec = Rectangle(width=[], height=10, x=2, y=None)
        self.assertEqual(str(e.exception), "width must be an integer")

        with self.assertRaises(TypeError) as e:
            rec = Rectangle(width=45, height=10)
            rec.width = []

    def test_non_valid_integers_attrubites(self):
        with self.assertRaises(ValueError) as err:
            rec = Rectangle(12, -58)
        self.assertEqual(str(err.exception), "height must be > 0")

        with self.assertRaises(ValueError) as err:
            rec = Rectangle(0, 58)
        self.assertEqual(str(err.exception), "width must be > 0")

        with self.assertRaises(ValueError) as err:
            rec = Rectangle(5, 45, -4)
        self.assertEqual(str(err.exception), "x must be >= 0")

        with self.assertRaises(ValueError) as err:
            rec = Rectangle(5, 45, 4)
            rec.height = -45
        self.assertEqual(str(err.exception), "height must be > 0")

        rec = Rectangle(5, 45, 0, 0)
        self.assertEqual(rec.y, 0)

    def test_area(self):
        rectangle = Rectangle(5, 10, 2, 3, 1)
        assert rectangle.area() == 50

    def test_display(self):
        rec = Rectangle(5, 5)
        expected = "#####\n" * 5

        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            rec.display()
            output = mock_stdout.getvalue()
        self.assertEqual(output, expected)

        rec = Rectangle(2, 3, 2, 2)
        expected = "\n\n" + "  ##\n" * 3
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            rec.display()
            output = mock_stdout.getvalue()
        self.assertEqual(output, expected)

        rec = Rectangle(1, 2, 0, 4)
        expected = "\n\n\n\n" + "#\n" * 2
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            rec.display()
            output = mock_stdout.getvalue()
        self.assertEqual(output, expected)

        rec = Rectangle(1, 2, 5, 0)
        expected = ((" " * 5) + "#\n") * 2
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            rec.display()
            output = mock_stdout.getvalue()
        self.assertEqual(output, expected)

    def test_string_representation(self):
        r1 = Rectangle(4, 6, 2, 1, 12)
        r2 = Rectangle(5, 5, 1)
        expected = "[Rectangle] (12) 2/1 - 4/6"
        expected2 = "[Rectangle] (1) 1/0 - 5/5"

        self.assertEqual(str(r1), expected)
        self.assertEqual(str(r2), expected2)

    def test_update_instance_valid_attributes(self):
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 10/10")
        r1.update()
        self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 10/10")

        r1.update(89)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 10/10")

        r1.update(89, 2)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/10")

        r1.update(89, 2, 3)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/3")

        r1.update(89, 2, 3, 4)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/10 - 2/3")

        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_instance_invalid_attributes(self):
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 10/10")

        r1.update(89)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 10/10")

        with self.assertRaises(ValueError) as e:
            r1.update(89, -2)
        self.assertEqual(str(e.exception), "width must be > 0")

        with self.assertRaises(TypeError) as e:
            r1.update(70, 20, [])
        self.assertEqual(str(e.exception), "height must be an integer")

        with self.assertRaises(ValueError) as e:
            r1.update(70, 20, 5, -2)
        self.assertEqual(str(e.exception), "x must be >= 0")

    def test_update_instance_number_of_args(self):
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 10/10")

        r1.update(12, 5, 12, 20, 4, "ignored", 1000, [])
        self.assertEqual(str(r1), "[Rectangle] (12) 20/4 - 5/12")
