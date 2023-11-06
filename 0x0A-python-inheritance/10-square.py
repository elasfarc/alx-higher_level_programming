#!/usr/bin/python3
"""
defines derived class square.
"""

Rectangle: type = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    This class represents a Square, a derived class from Rectangle.

    Attributes:
        - __size (int): The size of the square.
    """
    def __init__(self, size):
        """
        Initializes a Square instance with the specified size.

        Args:
            size (int): The size of the square.

        Raises:
            ValueError: If size is not a positive integer.
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        Calculate and return the area of the Square.

        Returns:
            int: The area of the Square (product of size by itself).
        """
        return self.__size * self.__size
