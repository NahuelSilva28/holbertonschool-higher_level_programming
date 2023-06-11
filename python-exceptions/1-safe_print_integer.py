#!/usr/bin/python3
    try:
        print("{:d}".format(value))
        return True
    except TypeError:
        return False
