#!/usr/bin/python3

def safe_print_integer(value):
    printed = False

    try:
        print("{:d}".format(value))
        printed = True
    except IndexError:
        None
    return printed
