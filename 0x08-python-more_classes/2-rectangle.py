#!/usr/bin/python3
"""definie a class Rectangle representing a rectangle
"""


class Rectangle:
    """an empty class Triangle that defines a triangle:
    """
    def __init__(self, width=0, height=0):
        """int the new rectangle instace

        Args:
            @width: width of the rectangle
            @height: height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter for the width"""
        return self.__width

    @property
    def height(self):
        """getter for the height"""
        return self.__height

    @width.setter
    def width(self, width):
        """setter for the width field

        Args:
            @width: the new width
        """
        if not type(width) is int:
            raise TypeError("width must be an integer")

        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @height.setter
    def height(self, height):
        """setter for the height field

        Args:
            @height: the new height
        """
        if not type(height) is int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        """return the area of a rectangle"""
        return self.width * self.height

    def perimeter(self):
        """return the perimeter of a rectangle"""
        return (self.width + self.height) * 2
