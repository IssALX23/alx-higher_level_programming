#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_di = a_dictionary.copy()
    for key in new_di:
        new_di[key] *= 2
    return new_di
