#!/usr/bin/python3
"""5-save_to_json_file.py
"""

import json


def save_to_json_file(my_obj: object, filename):
    """
    writes an Object to a text file, using a JSON representation.

    Args:
        @my_obj: object to be written to the file .
        @filename: name of the file to be created/overwritten.
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        json.dump(my_obj, f)
