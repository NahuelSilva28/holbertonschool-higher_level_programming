#!/usr/bin/python3
"""Write a function that adds 2 integers"""


def add_integer(a, b=98):
    """_summary_

    Args:
        a (int or float): The first number to be added.
        b (int or float, optional): The second number to be added.
            Defaults to 98.

    Raises:
        TypeError: If `a` is not an integer or float.
        TypeError: If `b` is not an integer or float.

    Returns:
        int: The addition of `a` and `b`, casted to an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")

    a = int(a)
    b = int(b)

    return a + b
