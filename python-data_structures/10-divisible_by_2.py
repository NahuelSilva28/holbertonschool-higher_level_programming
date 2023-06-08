#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    resul = []
    for num in my_list:
        if num % 2 == 0:
            resul.append(True)
        else:
            resul.append(False)
    return resul
