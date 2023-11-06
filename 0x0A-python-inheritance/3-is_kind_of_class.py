#!/usr/bin/python3
"""define is_kind_of_class(...)
"""


def is_kind_of_class(obj: object, a_class: type) -> bool:
    """
    checks if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class

    Args:
        obj: the object to be checked
        a_class: the class to be checked against

    Return:
        True if the object is an instance of,
        or if the object is an instance of a class that inherited from,
        the specified class; False otherwise.
    """
    return isinstance(obj, a_class)
