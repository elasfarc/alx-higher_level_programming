#!/usr/bin/python3
"""
Module containing the Base class.
"""
import json
from typing import List, Type, TypeVar


class Base:
    """
    Base class for managing IDs.

    Attributes:
        __nb_objects (int): A class variable to keep
        track of the number of objects.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a Base object with an optional ID.

        Args:
            id (int or None): An optional parameter representing the ID.
        """
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries: List[dict] = []) -> str:
        """
        Converts a list of dictionaries to a JSON string.

            Args:
                list_dictionaries (List[dict], optional):
                    A list of dictionaries. Defaults to [].

            Raises:
                TypeError: If list_dictionaries is not a list or
                contains non-dictionary elements.

            Returns:
                str: A JSON string representation of the list of dictionaries.
        """
        if type(list_dictionaries) is not list or not all(
            [type(element) is dict for element in list_dictionaries]
        ):
            raise TypeError("List of dictionaries")
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string: str = "") -> list[dict]:
        """
        Converts a JSON string to a list of dictionaries using the json.loads()

        Args:
            json_string (str, optional):
                a string representing a list of dictionaries. Defaults to "".

        Returns:
            If json_string is None or empty, return an empty list
            Otherwise, return the list represented by json_string
        """
        if not json_string:
            return []
        return json.loads(json_string)

    @staticmethod
    def is_indirectly_Base(obj: object):
        """
        Checks if an object is an instance of a subclass of Base.

            Args:
                obj (object): An object to check.

            Returns:
                bool: True if the object is an instance of a subclass of Base,
                False otherwise.
        """
        return isinstance(obj, Base) and obj.__class__ is not Base

    T = TypeVar('T', bound='Base')

    @classmethod
    def save_to_file(cls, list_objs: List[T] = []):
        """
        Saves a list of instances of subclasses of Base to a JSON file.

            Args:
                list_objs (List[T], optional):
                    A list of instances of subclasses of Base.
                    Defaults to [].

            Raises:
                TypeError: If list_objs is not a list or
                contains non-Base instances.

            Writes:
                A JSON file named after the class name,
                containing the list of dictionaries representing the
                attributes of each Base instance.
        """

        if type(list_objs) is not list or not all(
            [Base.is_indirectly_Base(element) for element in list_objs]
        ):
            raise TypeError(
                "@list_objs: list of instances who inherits of Base"
            )

        with open(cls.__name__ + ".json", "w", encoding="utf-8") as file:
            dictionaries: List[dict[str, int]] = [
                obj.to_dictionary() for obj in list_objs
            ]
            file.write(Base.to_json_string(dictionaries))

    @classmethod
    def create(cls, **dictionary: dict[str, int]):
        supported_classes = ["Rectangle", "Square"]
        if not issubclass(cls, Base) or cls is Base:
            raise TypeError(
                "only support classes that inherhit from Base class"
            )

        if cls.__name__ not in supported_classes:
            raise TypeError(f"class {cls.__name__} not supported")

        if type(dictionary) is not dict:
            raise TypeError("@dictionary: dict[str, int]")

        if cls.__name__ == supported_classes[0]:
            if "width" not in dictionary or "height" not in dictionary:
                raise ValueError("Rectangle must has a width and a height")

        if cls.__name__ == supported_classes[1]:
            if "size" not in dictionary:
                raise ValueError("Square must has a size")

        obj = cls(1, 1) if cls.__name__ == "Rectangle" else cls(1)
        obj.update(**dictionary)
        return obj
