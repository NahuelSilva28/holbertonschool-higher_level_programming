#!/usr/bin/python3
"""Write a class Square that defines a square by: (based on 5-square.py)"""


class Square:
    """class Square"""

    def __init__(self, size=0, position=(0, 0)):
        """new instance of square"""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """get the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """set the position of the square"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(isinstance(i, int) and i >= 0 for i in value):
            raise ValueError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """calculate area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with '#' character"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
