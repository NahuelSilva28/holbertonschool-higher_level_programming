#!/usr/bin/python3
"""
Write a script that adds all arguments
to a Python list, and then save them to a file:
"""


import sys


# Importing functions from external modules
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    # Load existing data from the file
    data = load_from_json_file(filename)
except FileNotFoundError:
    # Create an empty list if the file doesn't exist
    data = []

# Add command line arguments to the list
data.extend(sys.argv[1:])

# Save the updated data to the file
save_to_json_file(data, filename)
