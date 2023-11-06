#!/usr/bin/python3
"""define is_same_class(..)"""


def is_same_class(obj: object, a_class: type):
    """
    checks if the object is exactly an instance of the specified class

    Args:
        obj: the object to be checked
        a_class: the class to be checked against

    Return:
        True if the object is exactly an instance of the specified class;
        False otherwise.
    """
    return obj.__class__ is a_class
