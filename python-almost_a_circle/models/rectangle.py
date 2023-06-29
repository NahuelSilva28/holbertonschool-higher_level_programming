#!/usr/bin/python3
"""Rectangle class from base"""

from .base import Base

class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor method"""
        super().__init__(id)
        self._width = width
        self._height = height
        self._x = x
        self._y = y

    @property
    def width(self):
        """Getter method for width"""
        return self._width

    @width.setter
    def width(self, value):
        """Setter method for width"""
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        if value <= 0:
            raise ValueError("Width must be > 0")
        self._width = value

    @property
    def height(self):
        """Getter method for height"""
        return self._height

    @height.setter
    def height(self, value):
        """Setter method for height"""
        if not isinstance(value, int):
            raise TypeError("Height must be an integer")
        if value <= 0:
            raise ValueError("Height must be > 0")
        self._height = value

    @property
    def x(self):
        """Getter method for x"""
        return self._x

    @x.setter
    def x(self, value):
        """Setter method for x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self._x = value

    @property
    def y(self):
        """Getter method for y"""
        return self._y

    @y.setter
    def y(self, value):
        """Setter method for y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self._y = value

    def area(self):
        """Calculates and returns the area of the rectangle"""
        return self._width * self._height

    def display(self):
        """Prints the rectangle using '#' character"""
        rectangle = "\n" * self._y + (" " * self._x + "#" * self._width + "\n") * self._height
        print(rectangle, end="")

    def update(self, *args, **kwargs):
        """Updates the attributes of the rectangle"""
        if args:
            attrs = ['id', 'width', 'height', 'x', 'y']
            if len(args) > len(attrs):
                raise ValueError(f"Too many arguments provided. Expected: {len(attrs)}")
            for attr, value in zip(attrs, args):
                setattr(self, attr, value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of the rectangle"""
        return {
            'id': self.id,
            'width': self._width,
            'height': self._height,
            'x': self._x,
            'y': self._y
        }

    def __str__(self):
        """String representation of the rectangle"""
        return f"[Rectangle] ({self.id}) {self._x}/{self._y} - {self._width}/{self._height}"
