#!/usr/bin/python3

# my_list = [my_list[i] for i in range(len(my_list)) if i != idx]

def delete_at(my_list=[], idx=0):
    if idx >= 0 and idx < len(my_list):
        del my_list[idx]
    return my_list
