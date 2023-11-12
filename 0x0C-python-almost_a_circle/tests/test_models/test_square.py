import unittest
from models.square import Square
from models.base import Base


class Test_Square(unittest.TestCase):

    def setUp(self) -> None:
        Base._Base__nb_objects = 0

    def test_valid_attributes(self):
        sq = Square(5, y=4)
        self.assertEqual(sq.id, 1)
        assert sq.width == 5
        assert sq.height == 5
        assert sq.x == 0
        assert sq.y == 4

    def test_setters_getters(self):
        rec = Square(size=15, x=2, y=4, id=15)
        rec.height = 8
        rec.x = 4
        rec.y = 2
        rec.id = 20
        assert rec.id == 20
        assert rec.height == 8
        assert rec.x == 4
        assert rec.y == 2

    def test_non_integer_attributes(self):
        with self.assertRaises(TypeError) as e:
            rec = Square([], x=2, y=4)
        self.assertEqual(str(e.exception), "width must be an integer")

        with self.assertRaises(TypeError) as e:
            rec = Square(4, x="2", y=4)
        self.assertEqual(str(e.exception), "x must be an integer")

    def test_string_rEpresentation(self):
        sq = Square(12, 5, 5, 78)
        self.assertEqual(str(sq), "[Square] (78) 5/5 - 12")

    def test_size_geeter_setter(self):
        sq = Square(2)
        self.assertEqual(sq.size, 2)

        sq.size = 15
        self.assertEqual(sq.size, 15)
        self.assertEqual(sq.width, 15)
        self.assertEqual(sq.height, 15)

        with self.assertRaises(TypeError) as err:
            sq.size = [12]
        self.assertEqual(str(err.exception), "width must be an integer")
