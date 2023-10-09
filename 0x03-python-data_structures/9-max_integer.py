#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    max = 0
    for i in range(len(my_list)):
        max = my_list[i]
        for j in range(len(my_list)):
            if my_list[j] > max:
                max = my_list[j]
    return max
