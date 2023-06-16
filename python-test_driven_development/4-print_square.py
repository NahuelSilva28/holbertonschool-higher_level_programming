#!/usr/bin/python3
""" Write a function that prints a square with the character """


def print_square(size):
    """_summary_
Args:
        size (int): The length of the square's sides.

    Raises:
        TypeError: If the size is not an integer.
        ValueError: If the size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
