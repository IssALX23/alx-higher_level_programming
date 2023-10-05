#!/usr/bin/python3
import sys
if __name__ == "__main__":
    l = len(sys.argv)
    if l == 1:
        print("0 arguments.")
    elif l == 2:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    else:
        count = 0
        for item in sys.argv[1:]:
            count += 1
        print("{} arguments:".format(count))
        i = 1
        for item in sys.argv[1:]:
            print("{}: {}".format(i, item))
            i += 1
