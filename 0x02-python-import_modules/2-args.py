#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    count = len(sys.argv)
    index = 0
    if count == 1:
        print("{} arguments.".format(count - 1))
    elif count == 2:
        index = 1
        print("{} argument:".format(count - 1))
        print("{}: {}".format(index, sys.argv[1]))
    else:
        print("{} arguments:".format(count - 1))
        index = 1
        for item in sys.argv[1:]:
            print("{}: {}".format(index, item))
            index += 1
