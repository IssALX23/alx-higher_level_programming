#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if not my_list:
        return
    copy = my_list.copy()
    if idx < 0 or idx > len(my_list)-1:
        return copy
    copy[idx] = element
    return copy
