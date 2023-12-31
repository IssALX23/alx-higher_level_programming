#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError) as msg:
        sys.stderr.write(f"Exception: {msg}\n")
        return False
