#!/usr/bin/python3
"""
Class Rectangle that inherits from Base
"""
from models.base import Base


class Rectangle(Base):
    """
    Class Rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Start of instance for class Rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getting width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setting width"""
        self.__width = value

    @property
    def height(self):
        """Getting height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setting height"""
        self.__height = value

    @property
    def x(self):
        """Getting x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setting x"""
        self.__x = value

    @property
    def y(self):
        """Getting y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setting y"""
        self.__y = value
