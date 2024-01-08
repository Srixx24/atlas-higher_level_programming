#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):

    results = []

    for i in range(list_length):
        try:
            element_1 = my_list_1[i]
            element_2 = my_list_2[i]
            if not isinstance(element_1, (int, float)) or not isinstance(element_2, (int, float)):
                raise TypeError('wrong type')
            try:
                div = element_1 / element_2
            except ZeroDivisionError:
                print("division by 0")                    
                div = 0
            except IndexError:
                print("out of range")
                div = 0
            finally:
                results.append(div)
        except TypeError:
            print('wrong type')
            results.append(0)
    return results
