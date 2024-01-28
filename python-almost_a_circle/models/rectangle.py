#!/usr/bin/python3
"""
Class Rectangle that inherits from Base
"""
from models.base import Base


class Rectangle(Base):
    """
    Class Rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=1):
        """
        Start of instance for class Rectangle
        """
        super().__init__(id)
        self.id = id
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """String of rectangle"""
        return (
            f"[Rectangle] ({self.id}) {self.x}/{self.y} - "
            f"{self.width}/{self.height}"
        )

    def update(self, *args, **kwargs):
        """Attribute updates"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
             for key, value in kwargs.items():
                setattr(self, key, value)

    @property
    def width(self):
        """Getting width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setting width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getting height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setting height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getting x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setting x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getting y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setting y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Area of Rectangle"""
        return self.width * self.height

    def display(self):
        """Prints the Rectangle to output"""
        print("\n" * self.__y, end="")
        print("\n".join([" " * self.__x + "#" * self.__width] * self.__height))

    def to_dictionary(self):
        """Dictionary representation of a Rectangle"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
            }
