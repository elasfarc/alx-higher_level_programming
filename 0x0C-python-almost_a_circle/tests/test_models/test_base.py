import unittest
from unittest.mock import patch, mock_open
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_Base(unittest.TestCase):

    def setUp(self) -> None:
        Base._Base__nb_objects = 0

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

    def test_JSON_to_file_vaild_writing(self):
        r1 = Rectangle(4, 12)
        r2 = Rectangle(10, 7, 2, 8)
        r3 = Rectangle(2, 4)

        file_name = Rectangle.__name__ + ".json"
        encoding = "utf-8"
        excpected_content = json.dumps(
            [rec.to_dictionary() for rec in [r1, r2, r3]]
        )

        mock_file = mock_open()
        with patch("builtins.open", mock_file):
            Rectangle.save_to_file([r1, r2, r3])
        mock_file.assert_called_once_with(file_name, 'w', encoding=encoding)
        mock_file().write.assert_called_once_with(excpected_content)

        mock_file = mock_open(read_data=excpected_content)
        with patch("builtins.open", mock_file):
            with open(file_name, 'r', encoding=encoding) as h:
                actual = h.read()

        mock_file.assert_called_once_with(file_name, 'r', encoding=encoding)
        self.assertEqual(actual, excpected_content)

    def test_JSON_to_file_empty_list(self):
        mocked_file = mock_open()
        file_name = Square.__name__ + ".json"
        excpected = json.dumps([])

        with patch("builtins.open", mocked_file):
            Square.save_to_file()

        mocked_file.assert_called_once_with(file_name, 'w', encoding="utf-8")
        mocked_file().write.assert_called_once_with(excpected)

        mocked_file = mock_open(read_data=excpected)
        with patch("builtins.open", mocked_file):
            with open(file_name, 'r', encoding="utf-8") as h:
                actual = h.read()
        mocked_file.assert_called_once_with(file_name, 'r', encoding="utf-8")
        self.assertEqual(actual, excpected)

    def test_JSON_to_file_fail(self):
        r1 = Rectangle(4, 12)
        r2 = Rectangle(10, 7, 2, 8)

        with self.assertRaises(TypeError) as err:
            Rectangle.save_to_file("")
        self.assertEqual(
            str(err.exception),
            "@list_objs: list of instances who inherits of Base"
        )

        with self.assertRaises(TypeError) as err:
            Rectangle.save_to_file([r1, r2, list()])
        self.assertEqual(
            str(err.exception),
            "@list_objs: list of instances who inherits of Base"
        )

        with self.assertRaises(TypeError) as err:
            Rectangle.save_to_file([r1, r2, Base()])
        self.assertEqual(
            str(err.exception),
            "@list_objs: list of instances who inherits of Base"
        )


if __name__ == "__main__":
    unittest.main()
