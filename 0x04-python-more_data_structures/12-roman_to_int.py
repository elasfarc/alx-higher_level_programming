#!/usr/bin/python3

def roman_to_int(roman_string):
    roman_nums = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
    subcase = dict(I=('X', 'V'), X=('C', 'L'), C=('M', 'D'))
    num, idx, length = 0, 0, len(roman_string)

    while (idx < length):
        c = roman_string[idx]
        nxt = roman_string[idx + 1] if idx != length - 1 else None
        if nxt and subcase.get(c) and nxt in subcase.get(c):
            num += abs(roman_nums[c] - roman_nums[nxt])
            idx += 1
        else:
            num += roman_nums[c]
        idx += 1
    return num
