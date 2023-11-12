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

    def __str__(self):
        """
        Returns a string representation of the Square object.
        """
        cls = self.__class__.__name__
        return f"[{cls}] ({self.id}) {self.x}/{self.y} - {self.width}"
