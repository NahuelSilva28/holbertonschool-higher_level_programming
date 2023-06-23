#!/usr/bin/python3
"""
Write a class Square that inherits from Rectangle 
(9-rectangle.py). (task based on 10-square.py).
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a square shape
    """

    def __init__(self, size: int):
        """
        Initializes a square object
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self) -> str:
        """
        Returns a string representation of the square
        """
        return "[Square] {}/{}".format(self._Rectangle__width, self._Rectangle__height)

    def area(self) -> int:
        """
        Computes the area of the square
        """
        return self._Rectangle__width * self._Rectangle__height
