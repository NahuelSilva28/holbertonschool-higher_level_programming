#!/usr/bin/python3
"""Square class from rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor method"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter method for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter method for size"""
        self.width = value
        self.height = value

    def __str__(self):
        """String representation of the square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
