#!/usr/bin/python3
"""7-base_geometry.py
"""


class BaseGeometry:
    """
    class BaseGeometry
    """
    def area(self):
        """Public instance method area
        Raises: Exception with the message area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value) -> None:
        """Public instance method integer_validator
        validates the value of the integer

        Args:
           @name: name of the integer
           @value: value of the integer

        Raises:
            if value is not an integer: raise a TypeError exception,
                with the message <name> must be an integer
            if value is less or equal to 0: raise a ValueError exception
                with the message <name> must be greater than 0
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
