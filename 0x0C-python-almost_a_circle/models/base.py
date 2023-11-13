#!/usr/bin/python3
"""
Module containing the Base class.
"""
import json
from typing import List


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
        if type(list_dictionaries) is not list or not all(
            [type(element) is dict for element in list_dictionaries]
        ):
            raise TypeError("List of dictionaries")
        return json.dumps(list_dictionaries)
