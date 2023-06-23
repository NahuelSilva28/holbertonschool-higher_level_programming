#!/usr/bin/python3
"""
Write a class Square that inherits 
from Rectangle (9-rectangle.py). (task based on 10-square.py).
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a square shape
    """

    def __init__(self, size):
        """
        Initializes a square object
        """
        self.__size = 0
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """
        Returns a string representation of the square
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
