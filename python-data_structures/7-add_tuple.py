#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):

    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)

    first = a[0] + b[0]
    second = a[1] + b[1]

    return (first, second)
