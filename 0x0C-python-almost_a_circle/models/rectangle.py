#!/usr/bin/python3
"""
Module containing the Rectangle class
"""

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
        self.__y = y
