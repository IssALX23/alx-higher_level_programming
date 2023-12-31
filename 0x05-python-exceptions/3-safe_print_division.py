#!/usr/bin/python3
def safe_print_division(a, b):
    res = None
    try:
        res = a / b
        return res
    except (ZeroDivisionError, ValueError, TypeError):
        return res
    finally:
        print("Inside result: {}".format(res))
