#!/usr/bin/env python3
def uppercase(str):
    new_str = ''
    for letter in str:
        if ord(letter) >= 97 and ord(letter) <= 122:
            new_str += chr(ord(letter) - 32)
        else:
            new_str += letter
    print("{}".format(new_str))
