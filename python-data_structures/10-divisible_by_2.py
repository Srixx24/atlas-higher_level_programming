#!/usr/bin/python3

def divisible_by_2(my_list=[]):

    new =[]
    if my_list:
        for num in my_list:
            new.append(num % 2 == 0)
        return new
