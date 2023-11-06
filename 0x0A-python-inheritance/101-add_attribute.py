#!/usr/bin/python3
"""defines add_attribute(..)
"""


def add_attribute(obj, name, value):
    """
    Add a new attribute to an object.

    Args:
    obj (object): The target object to which the attribute will be added.
    name (str): The name of the new attribute.
    value (any): The value to assign to the new attribute.

    Raises:
    TypeError: If the object does not have a `__dict__` attribute, indicating
               that it is not suitable for adding new attributes.

    Example:
    >>> obj = SomeClass()
    >>> add_attribute(obj, "new_attr", 42)
    >>> print(obj.new_attr)  # Access the new attribute
    42

    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
