#!/usr/bin/python3


def inherits_from(obj: object, a_class: type) -> bool:
    """
    checks if the object is an instance of a class that
    inherited (directly or indirectly) from the specified class

    Args:
        obj: the object to be checked
        a_class: the class to be checked against

    Return:
        True if the object is exactly an instance of class that
        inherited (directly or indirectly) from the specified class;
        False otherwise.
    """
    return issubclass(obj.__class__, a_class) and obj.__class__ != a_class
