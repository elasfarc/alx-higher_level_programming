#!/usr/bin/python3

def uppercase(str):
    for char in str:
        code = ord(char)
        if code in range(97, 123):
            char = chr(code - 32)
        print("{}".format(char), end="")
    print()
