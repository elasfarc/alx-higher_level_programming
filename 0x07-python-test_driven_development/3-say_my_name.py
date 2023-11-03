#!/usr/bin/python3
"""Defines say_my_name function."""


def say_my_name(first_name, last_name=""):
    """Print a name.

        Args:
            first_name (str): The first name to print.
            last_name (str): The last name to print.
        Raises:
            TypeError: If either of first_name or last_name are not strings.

    """
    valid_args = [type(name) is str for name in [first_name, last_name]]
    if not all(valid_args):
        raise TypeError("{} must be a string".format(
            "first_name" if not valid_args[0] else "last_name")
        )
    print("My name is {} {}".format(
        first_name, last_name if last_name else "")
    )
