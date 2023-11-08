#!/usr/bin/python3
"""2-append_write.py
"""


def append_write(filename="", text=""):
    """
    a function that appends a string at the end of a text file (UTF8)
    Args:
        @filename: name of the file to be created/overwritten
        @text: text to be written to the file

    Return:
         the number of characters added

    """
    with open(filename, mode='a', encoding='utf-8') as f:
        return f.write(text)
