#!/usr/bin/python3
"""Write a function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """_summary_

    Args:
        matrix (list of lists): The matrix to be divided. Each element of the matrix
            must be an integer or float.
        div (int or float): The number to divide the matrix elements by.

    Raises:
        TypeError: If matrix is not a matrix (list of lists) of integers/floats.
        TypeError: If each row of the matrix doesn't have the same size.
        TypeError: If div is not a number (integer or float).
        ZeroDivisionError: If div is equal to 0.

    Returns:
        list of lists: A new matrix with all elements divided by div and rounded to 2 decimal places.
    """
    if not all(isinstance(row, list) and len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(element / div, 2) for element in row] for row in matrix]
