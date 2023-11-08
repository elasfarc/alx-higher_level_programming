#!/usr/bin/python3
"""4-from_json_string.py
"""

import json


def from_json_string(my_str):
    """
    a function that returns an object (Python data structure)
    represented by a JSON string

    Args:
        @my_str: the JSON representation of the python object
    """
    return json.loads(my_str)
