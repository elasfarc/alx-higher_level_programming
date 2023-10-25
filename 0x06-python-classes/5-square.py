#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""
    def __init__(self, size=0):
        """
        init the new instance

        Args:
            @size(int): size of the new instance
        """
        self.size = size

    @property
    def size(self):
        """ getter for size field"""
        return self.__size

    @size.setter
    def size(self, size):
        """
        setter for the size field

        Args:
            size(int): size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """calculate the area of the square object"""
        return self.__size * self.__size

    def my_print(self):
        for i in range(0, self.size):
            for _ in range(self.size):
                print("#", end="")
            print()
        else:
            print()
