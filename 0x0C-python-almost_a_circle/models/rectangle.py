#!/usr/bin/python3
"""
Module containing the Rectangle class
"""

from typing import Any, Tuple
from models.base import Base


class Rectangle(Base):
    """
    class Rectangle, inherites from Base

        Properties:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x-coordinate of the rectangle.
            y (int): The y-coordinate of the rectangle.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a Rectangle object.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x-coordinate of the rectangle.
            y (int): The y-coordinate of the rectangle.
            id (int or None): An optional parameter representing the ID.
        """
        super(Rectangle, self).__init__(id)

        list(map(
            lambda item: Rectangle.validate(item),
            {"width": width, "height": height, "x": x, "y": y}.items()
        ))

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Get the width of the rectangle.
        """
        return self.__width

    @property
    def height(self):
        """
        Get the height of the rectangle.
        """
        return self.__height

    @property
    def x(self):
        """
        Get the x-coordinate of the rectangle.
        """
        return self.__x

    @property
    def y(self):
        """
        Get the y-coordinate of the rectangle.
        """
        return self.__y

    @width.setter
    def width(self, width):
        """
        Set the width of the rectangle.

        Args:
            width (int): The width of the rectangle.

        Returns:
            None
        """
        Rectangle.validate(("width", width))
        self.__width = width

    @height.setter
    def height(self, height):
        """
        Set the height of the rectangle.

        Args:
            height (int): The height of the rectangle.

        Returns:
            None
        """
        Rectangle.validate(("height", height))
        self.__height = height

    @x.setter
    def x(self, x):
        """
        Set the x-coordinate of the rectangle.

        Args:
            x (int): The x-coordinate of the rectangle.

        Returns:
            None
        """
        Rectangle.validate(("x", x))
        self.__x = x

    @y.setter
    def y(self, y):
        """
        Set the y-coordinate of the rectangle.

        Args:
            y (int): The y-coordinate of the rectangle.

        Returns:
            None
        """
        Rectangle.validate(("y", y))
        self.__y = y


    def area(self):
        """calculate the rectangle area

        Return: the rectangle area
        """
        return self.width * self.height

    @staticmethod
    def validate(item: Tuple[str, Any]):
        """
         Validate the specified key-value pair.

         Args:
             item (Tuple[str, Any]): A tuple representing a key-value pair,
             where the first element is the key (a string) and the second
             element is the value (of any type).

         Raises:
             TypeError: If the value is not an integer.
             ValueError: If the value is not within the specified range for the
                 corresponding key.

         Returns:
             None
         """
        key, value = item
        if type(value) is not int:
            raise TypeError(f"{key} must be an integer")

        if value <= 0 and key in ["width", "height"]:
            raise ValueError(f"{key} must be > 0")

        if value < 0 and key in ["x", "y"]:
            raise ValueError(f"{key} must be >= 0")
