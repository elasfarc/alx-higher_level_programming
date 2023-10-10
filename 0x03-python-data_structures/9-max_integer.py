#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list):
        max_value = my_list[0]
        for integer in my_list:
            max_value = integer if (integer > max_value) else max_value
        return max_value
    else:
        return None
