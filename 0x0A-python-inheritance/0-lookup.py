#!/usr/bin/python3
""""def lookup
"""


def lookup(obj):
    """
    returns the list of available attributes and methods of an object.

    Args:
        @obj: the object to be lookedup

    Return:
        list of available attributes and methods of an object.
    """
    return dir(obj)
