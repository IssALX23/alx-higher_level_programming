#!/usr/bin/python3
def no_c(my_string):
    new_str = ""
    if not my_string:
        return new_str
    for word in my_string:
        for letter in word:
            if letter != 'c' and letter != 'C':
                new_str += letter
    return new_str
