import unittest
from models.base import Base


class Test_Base(unittest.TestCase):
    def test_create_new_instatnce_with_id(self):
        base = Base(15)
        self.assertEqual(base.id, 15)

    def test_create_new_instance_with_no_id(self):
        base = Base()
        base2 = Base(240)
        base3 = Base()

        self.assertEqual(base.id, 1)
        self.assertEqual(base3.id, 2)


if __name__ == "__main__":
    unittest.main()
