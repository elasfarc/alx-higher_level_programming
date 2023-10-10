#!/usr/bin/python3

def no_c(my_string):
    cpy = ""
    for ch in my_string:
        if ch != 'c' and ch != 'C':
            cpy += ch
    return cpy
