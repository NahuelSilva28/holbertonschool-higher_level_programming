#!/usr/bin/python3
"""Write a class BaseGeometry (based on 6-base_geometry.py)."""


class BaseGeometry:
    """Calculate the area of a geometric shape.

        Raises:
            Exception: This method is not implemented in the base class.

        """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate the value to be an integer and greater than 0.

        Args:
            name (str): The name of the value.
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.

        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
