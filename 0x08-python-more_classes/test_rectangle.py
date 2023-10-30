import unittest
Rectangle = __import__("0-rectangle").Rectangle


class test_rectangle(unittest.TestCase):

    def test_creating_instances(self):
        rec = Rectangle()
        self.assertIsInstance(rec, Rectangle)


if __name__ == "__main__":
    unittest.main()
