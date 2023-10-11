#!/usr/bin/python3
def search_replace(my_list, search, replace):
    count = 0
    new_list = my_list.copy()
    for number in new_list:
        if number == search:
            new_list.remove(number)
            new_list.insert(count, replace)
        count += 1
    return new_list
