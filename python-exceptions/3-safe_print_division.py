#!/usr/bin/python3

def safe_print_division(a, b):

    try:
        result = a / b
    except ZeroDivisionError:
        return none
    finally:
        print("Inside result: {}".format("{:.2f}".format(result))
    return result
