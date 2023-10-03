#!/usr/bin/python3
for number1 in range(0, 11):
    for number2 in range(0, 10):
        if number1 != number2 and number1 < number2:
            print("{}{}".format(number1, number2), end=', ')
            if number1 == 8 and number2 == 9:
                print("\n")
