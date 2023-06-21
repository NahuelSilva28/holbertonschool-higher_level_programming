#!/usr/bin/python3
"""Lookup"""


class MyList(list):
    def print_sorted(self):
        """Write a class MyList that inherits from list:
        """
        sorted_list = sorted(self)
        print(sorted_list)
