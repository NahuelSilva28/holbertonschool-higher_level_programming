#!/usr/bin/python3
"""Write a class Square that defines a square by: (based on 4-square.py)"""


class Square:
    """class Square"""
    def __init__(self, size=0):
        """new instantance of square"""
        self.size = size
    
    @property
    def size(self):
        """get the size of the square"""
        return self.__size
    
    @size.setter
    def size(self, value):
        """set the size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
 
    def area(self):
        """calcula area of the square"""
        return self.__size ** 2
    
    def my_print(self):
        """Prints the square whit # if size = 0 empty line is printed."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
