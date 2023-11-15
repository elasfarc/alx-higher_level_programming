#!/usr/bin/python3
"""
Module containing the Base class.
"""
import json
import csv
from os import path
from typing import Dict, List, Protocol, Type, TypeVar, Union


class DirivedFromBase_Virtual(Protocol):
    """
        Protocol defining virtual methods for a class derived from Base.

        This protocol defines virtual methods that should be implemented by
        a class derived from the Base class.
        The methods include 'to_dictionary', which should return a dictionary
        representation of the object, and 'update', which is meant to update
        the object based on certain criteria.

        Methods:
        --------
        to_dictionary() -> Dict[str, int]:
            Return a dictionary representation of the object.

        update():
            Update the object based on certain criteria.
            This method should be implemented by classes derived from Base.

    """
    def to_dictionary(self) -> Dict[str, int]:
        """Return a dictionary representation of the object.
        """
        return {}

    def update(self):
        """Update the object based on certain criteria.
        """
        pass


T = TypeVar('T', bound='DirivedFromBase_Virtual')


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
    def to_json_string(list_dictionaries: Union[List[dict], None] = []) -> str:
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
        if list_dictionaries is None:
            list_dictionaries = []
        if type(list_dictionaries) is not list or not all(
            [type(element) is dict for element in list_dictionaries]
        ):
            raise TypeError("List of dictionaries")
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string: str = "") -> List[dict]:
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

    @classmethod
    def save_to_file(cls, list_objs: Union[List[T], None] = []):
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
        if list_objs is None:
            list_objs = []

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
    def create(cls: Type[T], **dictionary: int):
        """
            Create an instance of the class with attributes
            specified in the dictionary.
            The dictionary should contain key-value pairs
            representing attribute names and their corresponding values.

            Args:
                **dictionary (Dict[str, int]):
                    A dictionary containing attribute-value pairs for
                    initializing the object.

            Returns:
                Union['Rectangle', 'Square']:
                    An instance of the class with attributes
                    initialized based on the dictionary.

            Raises:
                TypeError: If the class is not a subclass of Base or
                    is the Base class,
                    or if the class is not one of the supported classes
                    ('Rectangle' or 'Square').
                TypeError: If the dictionary argument is not of type dict.
                ValueError: If the class is 'Rectangle' and
                    either 'width' or 'height' is missing.
                ValueError: If the class is 'Square' and 'size' is missing.

            """
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

    @classmethod
    def load_from_file(cls) -> List:
        """
            Load objects from a JSON file and create instances of the class.

            This class method reads objects from a JSON file named after
            the class, converts the JSON string to dictionaries,
            and creates instances of the class using the dictionaries.

            Returns:
                List['Base']:
                    A list of instances of the class loaded from the JSON file.
                [] :
                    empty list If the JSON file for the class does not exist.
            """
        file_name = cls.__name__ + ".json"
        if not path.exists(file_name):
            return []
        with open(file_name, 'r', encoding="utf-8") as file:
            json_str = file.read()
        dicts = cls.from_json_string(json_str)
        return [cls.create(**dic) for dic in dicts]

    @classmethod
    def save_to_file_csv(cls: Type[T], list_objs: List[T] = []):
        """
        Save a list of instances to a CSV file.

        This class method saves a list of instances to a CSV file.
        The instances should inherit from the Base class.
        The CSV file is named after the class.

        Args:
            cls (Type[T]): The class type.
            list_objs (List[T]):
                A list of instances to be saved to the CSV file.

        Raises:
            TypeError: If list_objs is not a list
            or contains instances that do not inherit from Base.
        """

        if type(list_objs) is not list or not all(
            [Base.is_indirectly_Base(obj) for obj in list_objs]
        ):
            raise TypeError(
                "@list_objs: list of instances who inherits of Base"
            )

        cls_name = cls.__name__

        if cls_name == Base.__name__:
            raise TypeError("only inherited classes from Base allowed")

        file_name = cls.__name__ + ".csv"

        common = ["id", "x", "y"]
        special_keys =\
            ["width", "height"] if cls_name == "Rectangle" else ["size"]
        field_names = [common[0], *special_keys, *common[1:]]

        data = [obj.to_dictionary() for obj in list_objs]

        with open(file_name, 'w', encoding="utf-8", newline="") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=field_names)
            writer.writeheader()
            writer.writerows(data)

    @classmethod
    def load_from_file_csv(cls):
        file_name = cls.__name__ + ".csv"
        if not path.exists(file_name):
            return []

        with open(file_name, 'r', encoding="utf-8", newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            return [
                cls.create(**{k: int(v) for (k, v) in row.items()})
                for row in reader
            ]
