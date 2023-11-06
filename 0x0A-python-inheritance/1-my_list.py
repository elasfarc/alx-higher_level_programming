#!/usr/bin/python3

class MyList(list):
    def print_sorted(self):
        temp = self[:]
        temp.sort()
        print(temp)
        del temp
