#!/usr/bin/python3
"""
Function that writes a string to a text file (UTF8) and
returns the number of characters
"""


def write_file(filename="", text=""):
    """
    Write text to a file
    """
    with open(filename, "w") as ostream:
        return ostream.write(text)
