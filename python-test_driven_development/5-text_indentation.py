#!/usr/bin/python3
"""Write a function that prints a text with 2 new lines after each of these characters: ., ? and :"""


def text_indentation(text):
    """_summary_   prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The input text.

    Raises:
        TypeError: If the text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation_marks = ['.', '?', ':']
    result = ""
    for char in text:
        if char in punctuation_marks:
            result += char + "\n\n"
        else:
            result += char

    print(result.rstrip())
