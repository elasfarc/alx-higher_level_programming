#!/usr/bin/python3
"""Defines a matrix division function."""


def add_integer(a: int, b=98):
    """Return the integer addition of a and b.

        Float arguments are typecasted to ints before addition is performed.

        Raises:
            TypeError: If either of a or b is a non-integer and non-float.
        """
    are_type = [n == n and type(n) in [float, int] for n in [a, b]]
    if not all(are_type):
        raise TypeError(
            f"{'a' if not are_type[0] else 'b'} must be an integer"
        )
    return int(a) + int(b)
