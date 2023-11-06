#!/usr/bin/python3
"""
defines derived class Rectangle.
"""

BaseGeometry: type = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    This class represents a Rectangle, a derived class from BaseGeometry.

    Attributes:
        - __width (int): The width of the rectangle.
        - __height (int): The height of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle instance with the specified width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: if width or height is not an integer
            ValueError: If width or height is not a positive integer.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculate and return the area of the Rectangle.

        Returns:
            int: The area of the Rectangle (product of width and height).
        """
        return self.__height * self.__width

    def __str__(self) -> str:
        """
        Return a string representation of the Rectangle.
        """
        return f"[{self.__class__.__name__}] {self.__width}/{self.__height}"
