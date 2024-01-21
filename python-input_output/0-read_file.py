#!/usr/bin/python3
"""Function to read and print a file"""


def read_file(filename=""):
    """
    Print file contents
    
    Args:
        filename: (str) Name of file to be read

    """
    with open(filename, "r") as istream:
        print (istream.read(), end="")
