import unittest
Rectangle = __import__("2-rectangle").Rectangle


class test_rectangle(unittest.TestCase):

    def setUp(self):
        self.rec = Rectangle()

    def test_creating_instances(self):
        self.assertIsInstance(self.rec, Rectangle)

    def test_triangle_width(self):
        rec = self.rec
        with self.assertRaises(AttributeError):
            rec.__width
        rec.width = 5
        self.assertEqual(rec.width, 5)

        rec2 = Rectangle(12)
        self.assertEqual(rec2.width, 12)
        rec2.width = 122
        self.assertEqual(rec2.width, 122)

        with self.assertRaises(TypeError) as e:
            Rectangle(7.5)

        self.assertEqual(str(e.exception), "width must be an integer")

        with self.assertRaises(ValueError) as e:
            Rectangle(-4)
        self.assertEqual(str(e.exception), "width must be >= 0")

    def test_triangle_height(self):
        rec = self.rec
        with self.assertRaises(AttributeError):
            rec.__height
        rec.height = 5
        self.assertEqual(rec.height, 5)

        rec2 = Rectangle(12)
        self.assertEqual(rec2.height, 0)
        rec2.height = 122
        self.assertEqual(rec2.height, 122)

        with self.assertRaises(TypeError) as e:
            Rectangle(0, 7.5)

        self.assertEqual(str(e.exception), "height must be an integer")

        with self.assertRaises(ValueError) as e:
            Rectangle(0, -4)
        self.assertEqual(str(e.exception), "height must be >= 0")

    def test_area(self):
        rec = Rectangle(10, 2)
        self.assertEqual(rec.area(), 20)

    def test_perimeter(self):
        rec = Rectangle()
        self.assertEqual(rec.perimeter(), 0)
        rec.width = 20
        rec.height = 10
        self.assertEqual(rec.perimeter(), 60)


if __name__ == "__main__":
    unittest.main()
