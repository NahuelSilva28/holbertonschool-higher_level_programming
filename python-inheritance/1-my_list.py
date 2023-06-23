#!/usr/bin/python3
"""my list"""


class MyList(list):
    """_summary_

    Args:
        list (_type_): _description_
    """
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
