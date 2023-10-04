#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = ''
    count = 0
    for letter in str:
        if count != n:
            new_str += letter
        count += 1
    return new_str
