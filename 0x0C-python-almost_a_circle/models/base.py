#!/usr/bin/python3
"""
Module containing the Base class.
"""


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
