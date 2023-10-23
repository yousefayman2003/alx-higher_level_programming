#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    printed = True

    try:
        print("{:d}".format(value))
    except Exception as ex:
        print("Exception:", ex, file=sys.stderr)
        printed = False

    return printed
