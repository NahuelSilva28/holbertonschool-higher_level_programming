#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """
    Returns a list of lists representing Pascal's triangle of size n.

    Args:
        n (int): The size of Pascal's triangle.

    Returns:
        list: List of lists representing Pascal's triangle.

    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        prev_row = triangle[i - 1]
        for j in range(1, i):
            value = prev_row[j - 1] + prev_row[j]
            row.append(value)
        row.append(1)
        triangle.append(row)

    return triangle
