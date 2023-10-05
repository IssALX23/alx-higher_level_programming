#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import hidden_4
    lists = dir(hidden_4)
    new_list = [item for item in lists if not item.startswith('__')]
    for item in new_list:
        print("{}".format(item))
