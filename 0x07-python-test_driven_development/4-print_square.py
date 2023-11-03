#!/usr/bin/python3
"""Defines a square-printing function."""


def print_square(size: int):
    """Print a square with the # character.

        Args:
            size (int): The height/width of the square.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is < 0
        """
    if not type(size) is int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(int(size)):
        for _ in range(int(size)):
            print("#", end="")
        print("")
