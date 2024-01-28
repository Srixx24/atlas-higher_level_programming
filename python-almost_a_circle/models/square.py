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
