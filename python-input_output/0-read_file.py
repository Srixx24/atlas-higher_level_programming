#!/usr/bin/python3

def read_file(filename=""):
    with open(filename,"r") as istream:
        print (istream.read(), end ="")
