#!/usr/bin/python3
"""0. Read file
"""


def read_file(filename=""):
    """
    function that reads a text file (UTF8) and prints it to stdout

    Args:
        @filename: name of the file to read from

    """
    with open(filename, mode='r', encoding='utf-8') as f:
        for line in f:
            print(line)
