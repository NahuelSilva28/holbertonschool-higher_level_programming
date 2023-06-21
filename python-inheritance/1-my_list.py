#!/usr/bin/python3
"""MYLIST"""


class MyList(list):
    def print_sorted(self):
        """Write a class MyList that inherits from list:
        """
        if not all(isinstance(x, int) for x in self):
            raise TypeError("Only integers")
        
        sorted_list = sorted(self)
        print(sorted_list)
