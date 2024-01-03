#!/usr/bin/python3

def uppercase(str):
    for char in str:
        print(char(ord) & 32), end='')
    print()
