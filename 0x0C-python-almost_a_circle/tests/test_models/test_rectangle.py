import unittest
from models.base import Base
from models.rectangle import Rectangle


class Test_Rectangle(unittest.TestCase):
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
