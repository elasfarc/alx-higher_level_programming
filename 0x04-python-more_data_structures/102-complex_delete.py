#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    # return {key:val for key,val in a_dictionary.items() if not value == val}
    for key in list(a_dictionary):
        if a_dictionary[key] == value:
            del a_dictionary[key]
    return a_dictionary
