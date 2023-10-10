#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    new_list = []
    if my_list is None or not my_list:
        pass
    if idx < 0 or idx >= len(my_list):
        return my_list
    new_list = my_list.copy()
    x = my_list[idx]
    new_list.remove(x)
    return new_list
