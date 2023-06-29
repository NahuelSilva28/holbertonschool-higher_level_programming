#!/usr/bin/python3
"""Rectangle class from base"""

from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor method"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Getter method for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width"""
        self.__width = value

    @property
    def height(self):
        """Getter method for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height"""
        self.__height = value

    @property
    def x(self):
        """Getter method for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter method for x"""
        self.__x = value

    @property
    def y(self):
        """Getter method for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter method for y"""
        self.__y = value

    def area(self):
        """Calculates and returns the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """Prints the rectangle using '#' character"""
        rectangle = "\n" * self.__y + (" " * self.__x + "#" * self.__width + "\n") * self.__height
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
            'width': self.__width,
            'height': self.__height,
            'x': self.__x,
            'y': self.__y
        }

    def __str__(self):
        """String representation of the rectangle"""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"
