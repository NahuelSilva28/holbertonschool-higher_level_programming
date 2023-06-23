#!/usr/bin/python3
"""MY LIST"""


class MyList(list):
    """my list"""
    def print_sorted(self):
        for i in self:
            if type(i) is not int:
                raise TypeError("all the values of the list must be integers")
        print(sorted(self))
        