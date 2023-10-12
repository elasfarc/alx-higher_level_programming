#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    _sum = 0
    for i, v in enumerate(argv):
        if not i == 0:
            _sum += int(v)
    print(_sum)
