#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):

    results = []

    for i in range(list_length):
        try:
            element_1 = my_list_1[i]
            element_2 = my_list_2[i]
            if isinstance(element_1, (int, float)) and isinstance(element_2, (int, float)):
                try:
                    div = my_list_1[i] / my_list_2[i]
                except ZeroDivisionError:
                    print("division by 0")
                    div = 0
                except TypeError:
                    print("wrong type")
                    div = 0
                except IndexError:
                    print("out of range")
                    div = 0
                finally:
                    results.append(div)
    return results
