#!/usr/bin/python3
"""1-write_file.py
"""


def write_file(filename="", text=""):
    """
    a function that writes a string to a text file (UTF8)
    Args:
        @filename: name of the file to be created/overwritten
        @text: text to be written to the file

    Return:
         the number of characters written

    """
    with open(filename, mode='w', encoding='utf-8') as f:
        return f.write(text)
