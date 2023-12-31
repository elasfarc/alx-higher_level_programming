#!/usr/bin/python3
"""
Module containing the Rectangle class
"""

from typing import Any, Tuple, TypedDict
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

    def display(self):
        """
        Display a rectangle pattern using a specified character.

        The rectangle pattern is constructed by repeating the specified
        character horizontally and vertically based on the width and height
        attributes of the Rectangle object.

        Args:
            None

        Returns:
            None
        """
        disp_char = '#'
        for _ in range(self.y):
            print("")
        for row in range(self.height):
            print(" " * self.x, end="")
            print(disp_char * self.width)

    def update(self, *args, **kwargs):
        """
            Update attributes of the object with values provided in the
            arguments.

            The method accepts both positional arguments (*args) and
            keyword arguments (**kwargs) to update specific attributes of
            the object. If positional arguments are provided,
            (**kwargs) are ignored and the order of attributes is the following
            list: ["id", "width", "height", "x", "y"].
            If there are more positional arguments than attributes,
            the excess arguments are ignored. For each "id" attribute provided,
            the method validates it using the Rectangle class's validate method

            Args:
                *args: Positional arguments representing values to update
                    the object's attributes in the order
                    ["id", "width", "height", "x", "y"].
                **kwargs: Keyword arguments representing attribute-value pairs
                    to update the object.

            Returns:
                None
            """
        attributes = ["id", "width", "height", "x", "y"]
        if args:
            for idx, value in enumerate(args):
                if idx >= len(attributes):
                    break
                attribute = attributes[idx]
                if (attribute == "id"):
                    Rectangle.validate((attribute, value))
                setattr(self, attribute, value)
        else:
            for key, value in kwargs.items():
                if key in attributes:
                    if key == "id":
                        Rectangle.validate((key, value))
                    setattr(self, key, value)
                else:
                    raise AttributeError(
                        f"'Rectangle' object has no attribute '{key}'"
                    )

    class Rectangle_Dict(TypedDict):
        """
        A rectangle represented as a dictionary.

        Attributes:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x-coordinate of the top-left corner of the rectangle.
            y (int): The y-coordinate of the top-left corner of the rectangle.
            id (int): A unique identifier for the rectangle.
        """
        width: int
        height: int
        x: int
        y: int
        id: int

    def to_dictionary(self) -> Rectangle_Dict:
        """
        Convert a rectangle object to a dictionary representation.

        Returns:
            Rectangle_Dict: A dictionary representing the rectangle.
        """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self) -> str:
        """
        Return a string representation of the object.

        Returns:
            str: A string representation of the object.
        """
        cls = self.__class__.__name__
        return f"""\
        [{cls}] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}\
        """.strip()

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
