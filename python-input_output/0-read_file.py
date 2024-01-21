#!/usr/bin/python3
"""Function to read and print a file"""


def read_file(filename=""):
    """Print file contents"""
    with open(filename,"r") as istream:
        print (istream.read(), end ="")
