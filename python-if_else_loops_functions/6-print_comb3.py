#!/usr/bin/python3
for i in range(10):
    for j in range(i + 1, 10):
        if i == 0:
            print("{:d}{:d}".format(i, j), end=', ')
        else:
            print("{:d}{:d}".format(i, j).lstrip('0'), end=', ')

print("{:d}{:d}".format(9, 9))
