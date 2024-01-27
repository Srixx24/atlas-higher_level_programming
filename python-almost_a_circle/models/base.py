#!/usr/bin/python3
"""
Class Base used as base for all other classes in this project.
"""


class Base:
    """
    Class Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Start of class Base instance
        """
        if id is not None:
            self.id = id
        else:
            base.__nb_objects += 1
            self.id = base.__nb_objects
