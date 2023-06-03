#!/usr/bin/python3
def uppercase(string):
    for char in string:
        ascii_value = ord(char)
        if 97 <= ascii_value <= 122:
            char = chr(ascii_value - 32)
        print(char, end="")
    print()
