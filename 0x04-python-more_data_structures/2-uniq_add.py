#!/usr/bin/python3

def reduce(reducer, seq, init):
    accum = init
    for element in seq:
        accum = reducer(accum, element)
    return accum

def uniq_add(my_list=[]):
    _sum = lambda n1, n2: n1 + n2
    return reduce(_sum, set(my_list), 0)

