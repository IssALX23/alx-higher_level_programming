#!/usr/bin/python3
for number in range(0, 99):
    if number < 10:
        number = '0' + str(number)
    print("{}, ".format(number), end='')
print(99)
