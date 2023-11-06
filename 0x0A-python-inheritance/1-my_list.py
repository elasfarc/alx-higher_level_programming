#!/usr/bin/python3
"""define MyList class
"""


class MyList(list):
    """class MyList that inherits from list
    """
    def print_sorted(self):
        """
        prints the list, sorted in ascending order
        """
        print(sorted(self))
