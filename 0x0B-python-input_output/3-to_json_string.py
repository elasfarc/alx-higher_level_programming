#!/usr/bin/python3
"""3-to_json_string.py
"""

import json


def to_json_string(my_obj):
    """
    function that returns the JSON representation of an object.

    Args:
        @my_obh: object to be converted to JSON

    Return:
        JSON representation of the object
    """
    return json.dumps(my_obj)
