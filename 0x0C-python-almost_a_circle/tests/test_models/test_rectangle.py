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
