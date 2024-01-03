#!/usr/bin/python3

def uppercase(str):
    uppers = ""
    for char in str:
        uppers += "{}".format(chr(ord(char) & ~32))
    print(uppers)
