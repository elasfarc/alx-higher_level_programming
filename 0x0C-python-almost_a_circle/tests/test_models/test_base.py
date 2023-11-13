import unittest
import json
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

    def test_convert_dictionary_to_json(self):
        d1 = {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}
        d2 = {'x': 12, 'width': 1, 'id': 7, 'height': 81, 'y': 12}
        assert Base.to_json_string([d1, d2]) == json.dumps([d1, d2])

        assert Base.to_json_string() == json.dumps([])
        assert Base.to_json_string([]) == json.dumps([])

        with self.assertRaises(TypeError):
            Base.to_json_string("")

        with self.assertRaises(TypeError):
            Base.to_json_string([12, 14])


if __name__ == "__main__":
    unittest.main()
