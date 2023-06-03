#!/usr/bin/python3
def uppercase(string):
    for c in string:
        ascii_val = ord(c)
        if 97 <= ascii_val <= 122:
            ascii_val -= 32
        print("{:c}".format(ascii_val), end="")
    print()
