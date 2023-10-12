#!/usr/bin/python3

def reduce(reducer, seq, init=None):
    has_init_value = init
    if not init:
        init = seq[0] if len(seq) else None
    accum = init
    for element in seq[0 if has_init_value else 1:]:
        accum = reducer(accum, element)
    return accum


def weight_average(my_list=[]):
    if len(my_list):
        aggregate_tuple = reduce(
                lambda acc, tup: (acc[0] + (tup[0] * tup[1]), acc[1] + tup[1]),
                my_list, (0, 0))
        return aggregate_tuple[0] / aggregate_tuple[1]
    else:
        return 0
