#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = my_list.copy()
    val = 0
    for number in new_list:
        while new_list.count(number) > 1:
            new_list.remove(number)
    for number in new_list:
        val += number
    return val
