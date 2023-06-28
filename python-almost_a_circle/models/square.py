#!/usr/bin/python3
"""Square class from rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor method"""
        super().__init__(size, size, x, y, id)

    def update(self, *args, **kwargs):
        """Updates the attributes of the square"""
        if args:
            attrs = ['id', 'size', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """String representation of the square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
