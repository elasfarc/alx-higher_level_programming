#!/usr/bin/python3
"""
module containing the class Square
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class Square, inherites from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square.
            x (int): The x-coordinate of the square.
            y (int): The y-coordinate of the square.
            id (int): The unique identifier of the square.
        """
        super(Square, self).__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Get the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.width

    @size.setter
    def size(self, size):
        """
        Set the size of the square.

        Args:
            size (int): The new size for the square.
        """
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """
            Update attributes of the object with values provided in the
            arguments.

            The method accepts both positional arguments (*args) and
            keyword arguments (**kwargs) to update specific attributes of
            the object. If positional arguments are provided,
            (**kwargs) are ignored and the order of attributes is the following
            list: ["id","size", "x", "y"].
            If there are more positional arguments than attributes,
            the excess arguments are ignored. For each "id" attribute provided,
            the method validates it using the Rectangle class's validate method

            Args:
                *args: Positional arguments representing values to update
                    the object's attributes in the order
                    ["id", "size", "x", "y"].
                **kwargs: Keyword arguments representing attribute-value pairs
                    to update the object.

            Returns:
                None
            """
        attributes = ["id", "size", "x", "y"]
        if args:
            for idx, value in enumerate(args):
                if idx >= len(attributes):
                    break
                attribute = attributes[idx]
                if (attribute == "id"):
                    Square.validate((attribute, value))
                setattr(self, attribute, value)
        else:
            for key, value in kwargs.items():
                if key in attributes:
                    if key == "id":
                        Square.validate((key, value))
                    setattr(self, key, value)
                else:
                    raise AttributeError(
                        f"'Square' object has no attribute '{key}'"
                    )

    def to_dictionary(self):
        """
        Convert a square object to a dictionary representation.

        Returns:
            A dictionary representing the square.
        """
        return {
            "id": self.id,
            "x": self.x,
            "y": self.y,
            "size": self.size,
        }

    def __str__(self):
        """
        Returns a string representation of the Square object.
        """
        cls = self.__class__.__name__
        return f"[{cls}] ({self.id}) {self.x}/{self.y} - {self.width}"
