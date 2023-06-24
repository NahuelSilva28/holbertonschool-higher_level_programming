#!/usr/bin/python3
"""Write a function that creates an Object from a “JSON file"""


import json


def load_from_json_file(filename):
    """Creates an object from a JSON file.

    Args:
        filename (str): The name of the JSON file.

    Returns:
        object: The object created from the JSON file.
    """
    with open(filename, mode='r', encoding='utf-8') as file:
        return json.load(file)
