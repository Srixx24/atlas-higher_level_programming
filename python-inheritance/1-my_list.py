#!/usr/bin/python3
"""
class MyList that inherits from list
"""


class MyList(list):
    """
    MyList class that inherits from list
    """
    def print_sorted(self):
        """
        Prints sorted list
        """
        print(sorted(self))
