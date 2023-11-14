import unittest
from unittest.mock import patch, mock_open, call
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

    def test_from_json_string(self):
        sq1 = Square(7).to_dictionary()
        sq2 = Square(7, 12, 5, 22).to_dictionary()

        json_list_input = Base.to_json_string([sq1, sq2])
        list_output = Base.from_json_string(json_list_input)

        self.assertEqual(list_output, [sq1, sq2])
        self.assertEqual(Base.from_json_string(), [])

    def test_create_instance_from_dictionary(self):
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()

        r2 = Rectangle.create(**r1_dictionary)
        assert str(r1) == str(r2)
        # assert self.assertNotEqual(r1, r2)
        assert r1 is not r2

        with self.assertRaises(ValueError) as err:
            create = Rectangle.create
            create(**{"x": 2})
        self.assertEqual(
            str(err.exception),
            "Rectangle must has a width and a height"
        )

    def test_load_from_file_no_file(self):

        mocked_file = mock_open()
        with patch("os.path.exists", return_value=False):
            result = Rectangle.load_from_file()
        self.assertEqual(result, [])

    c = [
            {"width": 5, "height": 4, "x": 2},
            {"width": 15, "height": 40, "y": 20},
        ]

    @patch("os.path.exists", return_value=True)
    @patch("builtins.open", new_callable=mock_open, read_data=json.dumps(c))
    @patch("models.base.Base.from_json_string", return_value=c)
    @patch("models.base.Base.create")
    def test_load_from_file(
        self, mock_create, mock_from_json, mock_open, mock_exists
    ):
        res = Rectangle.load_from_file()

        self.assertEqual(len(res), 2)
        mock_exists.assert_called_once_with('Rectangle.json')
        mock_open.assert_called_once_with(
            'Rectangle.json', 'r', encoding='utf-8'
        )
        mock_from_json.assert_called_once_with(
            '[{"width": 5, "height": 4, "x": 2}, '
            '{"width": 15, "height": 40, "y": 20}]'
        )
        mock_create.assert_called_with(width=15, height=40, y=20)

    @patch("builtins.open", new_callable=mock_open)
    def test_save_csv(self, mock_open):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]

        Rectangle.save_to_file_csv(list_rectangles_input)

        mock_open.assert_called_once_with(
            "Rectangle.csv", 'w', encoding='utf-8', newline=''
        )
        calls = [
            call('id,width,height,x,y\r\n'),
            call('1,10,7,2,8\r\n'),
            call('2,2,4,0,0\r\n'),
        ]
        mock_open().write.assert_has_calls(calls)

    @patch("builtins.open", new_callable=mock_open)
    def test_save_csv_empty_list(self, mocked_open):
        Rectangle.save_to_file_csv()

        mocked_open.assert_called_once_with(
            "Rectangle.csv", 'w', encoding="utf-8", newline=''
        )
        mocked_open().write.assert_called_once_with(
            'id,width,height,x,y\r\n'
        )

    def test_asave_csv_invalid_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv("")

        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv([[1], [2], [3]])

        with self.assertRaises(TypeError) as base_err:
            Base.save_to_file_csv()
        self.assertEqual(
            str(base_err.exception),
            "only inherited classes from Base allowed"
        )


if __name__ == "__main__":
    unittest.main()
