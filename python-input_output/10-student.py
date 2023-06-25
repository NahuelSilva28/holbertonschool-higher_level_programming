#!/usr/bin/python3
"""Student to JSON with filter Module"""


class Student:
    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of the Student instance.

        Args:
            attrs (list, optional): List of attribute names to retrieve. Defaults to None.

        Returns:
            dict: A dictionary with the requested attributes of the student.
        """
        if attrs is None:
            return self.__dict__
        else:
            json_data = {}
            for attr in attrs:
                if hasattr(self, attr):
                    json_data[attr] = getattr(self, attr)
            return json_data
