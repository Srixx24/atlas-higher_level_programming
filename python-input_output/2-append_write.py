#!/usr/bin/python3
"""
Function that appends a string at the end of a text file
(UTF8) and returns the number of character
"""


def append_write(filename="", text=""):
    """
    Appends a text string
    """
    with open(filename, "a") as ostream:
        return ostream.write(text)
