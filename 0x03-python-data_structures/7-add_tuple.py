#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    _sum = [0, 0]
    for i in range(2):
        if i < len(tuple_a):
            _sum[i] += tuple_a[i]
        if i < len(tuple_b):
            _sum[i] += tuple_b[i]
    return tuple(_sum)
