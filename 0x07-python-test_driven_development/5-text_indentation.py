#!/usr/bin/python3
"""Defines a text_indentation function."""


def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.

        Args:
            text (string): The text to print.
        Raises:
            TypeError: If text is not a string.
    """
    is_special_char = True
    if not type(text) is str:
        raise TypeError("text must be a string")

    for i in range(len(text)):
        char = text[i]
        if char == " " and is_special_char:
            continue
        if char == " ":
            j = i
            while text[j] == " ":
                j += 1
            if (text[j] == '\n'):
                i = j
                continue
        print(char, end="")
        if char in ['?', '.', ':', '\n']:
            is_special_char = True
            if char in ".?:":
                print("\n")
        else:
            is_special_char = False
