#!/usr/bin/python3

def reduce(reducer, seq, init=None):
    has_init_value = init
    if not init:
        init = seq[0] if len(seq) else None
    accum = init
    for element in seq[0 if has_init_value else 1:]:
        accum = reducer(accum, element)
    return accum


def reducer(item1, item2):
    return item1 if item1[1] > item2[1] else item2


def best_score(a_dictionary):
    if a_dictionary:
        return reduce(reducer, list(a_dictionary.items()))[0]
    else:
        return None
