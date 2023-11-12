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

    def test_update_instance_valid_attributes(self):
        r1 = Square(10, 10, 10)
        self.assertEqual(str(r1), "[Square] (1) 10/10 - 10")
        r1.update()
        self.assertEqual(str(r1), "[Square] (1) 10/10 - 10")

        r1.update(89)
        self.assertEqual(str(r1), "[Square] (89) 10/10 - 10")

        r1.update(89, 2)
        self.assertEqual(str(r1), "[Square] (89) 10/10 - 2")

        r1.update(89, 2, 3)
        self.assertEqual(str(r1), "[Square] (89) 3/10 - 2")

        r1.update(89, 2, 3, 4)
        self.assertEqual(str(r1), "[Square] (89) 3/4 - 2")

        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r1), "[Square] (89) 3/4 - 2")

    def test_update_instance_invalid_attributes(self):
        r1 = Square(10, 10, 10)
        self.assertEqual(str(r1), "[Square] (1) 10/10 - 10")

        r1.update(89)
        self.assertEqual(str(r1), "[Square] (89) 10/10 - 10")

        with self.assertRaises(ValueError) as e:
            r1.update(89, -2)
        self.assertEqual(str(e.exception), "width must be > 0")

        with self.assertRaises(TypeError) as e:
            r1.update(70, [])
        self.assertEqual(str(e.exception), "width must be an integer")

        with self.assertRaises(ValueError) as e:
            r1.update(70, 20, 5, -2)
        self.assertEqual(str(e.exception), "y must be >= 0")

    def test_update_instance_number_of_args(self):
        r1 = Square(10, 10, 10)
        self.assertEqual(str(r1), "[Square] (1) 10/10 - 10")

        r1.update(12, 5, 20, 4, "ignored", 1000, [])
        self.assertEqual(str(r1), "[Square] (12) 20/4 - 5")

        with self.assertRaises(TypeError) as err:
            r1.update(None)
        self.assertEqual(str(err.exception), "id must be an integer")

    def test_update_key_worded_arguments(self):
        r1 = Square(10, 10, 10)

        r1.update()
        self.assertEqual(str(r1), "[Square] (1) 10/10 - 10")

        r1.update(size=12, id=4)
        assert r1.size == 12
        assert r1.id == 4
        assert r1.x == 10

        r1.update(id=5, size=4, y=12)
        self.assertEqual(str(r1), "[Square] (5) 10/12 - 4")

        r1 = Square(20)
        r1.update(1000, id=5, size=50)
        assert r1.id == 1000
        assert r1.size == 20

        with self.assertRaises(TypeError) as err:
            r1.size = "100"
        self.assertEqual(str(err.exception), "width must be an integer")

        with self.assertRaises(AttributeError) as err:
            r1.update(ok=12)
        self.assertEqual(
            str(err.exception),
            "'Square' object has no attribute 'ok'"
        )

        with self.assertRaises(AttributeError) as e:
            r1.update(width=5)
        assert str(e.exception) == "'Square' object has no attribute 'width'"
