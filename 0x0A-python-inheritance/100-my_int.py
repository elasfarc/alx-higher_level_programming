#!/usr/bin/python3
"""
This script defines a custom class MyInt, a subclass of the int class.
"""


class MyInt(int):
    """
    This class represents a custom integer class that extends the int class.

    Methods:
        - __eq__(self, value: object) -> bool:
            Override of the equality operator.
        - __ne__(self, value: object) -> bool:
            Override of the inequality operator.

    Attributes:
        This class inherits the attributes and behaviors of the int class.
    """

    def __eq__(self, value: object) -> bool:
        """
        Override the equality operator (==) to compare
        MyInt with another object.

        Args:
            value (object): The object to compare with.

        Returns:
            bool: True if MyInt is equal to the provided object,
            False otherwise.
        """
        return super().__ne__(value)

    def __ne__(self, value: object) -> bool:
        """
        Override the inequality operator (!=) to compare
        MyInt with another object.

        Args:
            value (object): The object to compare with.

        Returns:
            bool: True if MyInt is not equal to the provided object,
            False otherwise.
        """
        return int(self) == value
