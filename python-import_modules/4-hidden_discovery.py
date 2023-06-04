#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    module_dir = hidden_4
    for item in dir(module_dir):
        if item[0] != '_':
            print("{}".format(item))
