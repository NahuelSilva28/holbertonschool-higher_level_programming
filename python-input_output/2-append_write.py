#!/usr/bin/python3
"""Write a function that appends a string
at the end of a text file (UTF8) and returns the number of characters added:"""


def append_write(filename="", text=""):
    """
    Args:
        filename (str, optional): The name of the file to append to. Defaults to "".
        text (str, optional): The string to append to the file. Defaults to "".

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, mode='a', encoding='utf-8') as file:
        file.write(text)
        return len(text)
