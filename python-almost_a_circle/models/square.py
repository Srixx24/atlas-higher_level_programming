#!/usr/bin/python3
"""
Class Square that inherits from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class Square
    """
    def __init__(self, size, x=0, y=0, id=1):
        """
        Start of instance of class Square
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Start of instance for square
        """
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.size
            )

    def update(self, *args, **kwargs):
        """Attributes updates"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    @property
    def size(self):
        """Getting size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setting size"""
        self.width = value
        self.height = value
